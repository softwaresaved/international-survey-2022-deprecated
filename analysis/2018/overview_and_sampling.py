#!/usr/bin/env python
import sys
import chevron
import numpy as np
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path

# List of all countries of interest
COUNTRIES = [
    "United Kingdom",
    "Australia",
    "United States",
    "Germany",
    "New Zealand",
    "Netherlands",
    "South Africa",
]


def table(name, data):
    csv = "csv/%s.csv" % name
    data.to_csv(csv, index=False)
    return {"t_" + name: data.to_markdown() + "\n\n[Download CSV](%s)" % csv}


def figure(name, plt):
    figpath = "fig/%s.png" % name
    plt.savefig(figpath)
    return {"f_" + name: "![%s](%s)" % (name, figpath)}


def first_existing(paths):
    for p in paths:
        if p.exists():
            return p
    return None


def make_report(generator):
    def func(**kwargs):
        base = Path(__file__).stem
        year = int(Path(__file__).resolve().parent.stem)
        filename = base + ".md"
        template = first_existing(
            [Path("templates") / filename, Path("../templates") / filename]
        )
        if template is None:
            print("E: No template found for:", base)
            print("   Put a corresponding template in the appropriate folder")
            print("   For this year, in a 'template' subfolder of this folder")
            print("   For all years, in a 'template' subfolder of the parent folder")
            sys.exit(1)

        # Ensure these paths are present
        for p in map(Path, ["csv", "fig"]):
            if not p.exists():
                p.mkdir()

        report, extra_data = generator(year=year, **kwargs)
        with template.open() as fp:
            Path(filename).write_text(chevron.render(fp, report))
        return extra_data


def convert_time(x):
    try:
        return datetime.datetime.strptime(str(x), "%Y-%m-%d %H:%M:%S").date()
    except ValueError:
        return x


@make_report
def run(data="data/public_merged.csv", year=None):
    """Prepares overview report and sampling.

    This function creates the figures and tables, as well as doing data
    transformations that are used in the other sections.
    """
    year = year or datetime.datetime.utcnow().year
    df = pd.read_csv(data)

    # The cleaning is about renaming some countries and create a globa category
    # for all countries that are not from one of the participating countries.

    # Rename the Uk and US
    df["socio1. In which country do you work?"].replace(
        {
            "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
            "United States of America": "United States",
        },
        inplace=True,
    )
    df = df[df["socio1. In which country do you work?"] != "Canada"]

    # Create a category world

    # As said, we are concerned about some countries specifically. However, we
    # collected information about other countries as well. To avoid any
    # confusion and having too much countries to plot, we group all of them
    # into one category "world"

    # Create a new columns if "World" if the country is not in the list
    df["Country"] = df["socio1. In which country do you work?"].apply(
        lambda x: x if x in COUNTRIES else "World"
    )

    # This is the total of participants. A participants is defined as a person
    # that have reached, at least the second section in the survey.

    report = {"n_participants": len(df[df["Year"] == year])}

    # Repartition per country

    # We developed specific questions for the following countries:
    # * Australia
    # * Canada (but host their own version of the survey so they will not be analysed here)
    # * Germany
    # * Netherlands
    # * New Zealand
    # * South Africa
    # * United Kingdom
    # * United States
    #
    # We can see the distribution of participants among the countries as follow

    df_countries = (
        df[df["Year"] == year]["socio1. In which country do you work?"]
        .value_counts()
        .to_frame()
        .reset_index()
    )
    report.update(table("participant", df_countries))
    df_countries.columns = ["name", "count"]

    df["Date"] = df["startdate. Date started"].apply(lambda x: convert_time(x))
    df_submission_per_country = df[["Country", "Date"]]  # .dropna()
    total_per_country = (
        df_submission_per_country.groupby(["Country"])["Date"].value_counts().to_frame()
    )
    total_per_country.columns = ["Count"]
    total_per_country = total_per_country.reset_index().sort_values(
        ["Date", "Country"], ascending=True
    )

    fig, axes = plt.subplots(2, 4, figsize=(20, 10))
    fig.tight_layout()
    fig.subplots_adjust(hspace=0.5)
    list_plots = list()
    for i, name in enumerate(total_per_country["Country"].unique()):
        if i < 4:
            a = 0
            b = i
        else:
            a = 1
            b = 5 - i
        axes[a, b] = total_per_country[total_per_country.Country == name].plot(
            x="Date", y="Count", legend=False, ax=axes[a, b]
        )
        axes[a, b].set_title("{}".format(name))
        # axes[a, b].set_xticklabels(labels=idx)

        axes[a, b].xaxis.set_major_locator(
            mdates.DayLocator(interval=10)
        )  # every 10 days
        axes[a, b].xaxis.set_minor_locator(mdates.DayLocator(interval=1))  # every day
        for label in axes[a, b].get_xticklabels():
            label.set_rotation(45)
        list_plots.append(axes[a, b])

    for ax in list_plots:
        ax.set(xlabel="Date of submission", ylabel="Count")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)

    report.update(figure("participation_date", plt))

    # Difference with the previous year

    # Several countries did the survey last year, here a summary of the
    # difference in the amount of participants.

    results = dict()
    for country in df[df["Year"] == year - 1]["Country"].unique():
        current_year = df[df["Year"] == year]["Country"].value_counts()[country]
        previous_year = df[df["Year"] == year - 1]["Country"].value_counts()[country]
        results[country] = {"%d" % (year - 1): previous_year, "%d" % year: current_year}
    diff_year_participants = pd.DataFrame.from_dict(results, orient="index")
    diff_year_participants["Difference between %d and %d" % (year - 1, year)] = (
        diff_year_participants["%d" % year] - diff_year_participants["%d" % (year - 1)]
    )
    report.update(table("difference_with_previous_year", diff_year_participants))

    # Plotting the difference
    ax = diff_year_participants.plot(kind="bar")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    report.update(figure("difference_with_previous_year", plt))

    # Subsetting: selecting valid participants only

    # On the total of participants, we only want the participants that code
    # software during their work. We had a specific question for this purpose.
    # We asked the participants if they are writing software or if they are
    # leading a group of software developers. Each of these questions had the
    # possibility of Yes/No answer. Here the exact wording of the questions:
    #
    # * Do you write software for academic research as part of your job
    #
    # * Does the majority of your role comprise leading a group of software
    # developers or RSEs?
    #
    # We will only select the participants who answered `Yes` to at least one
    # question.

    # Get the count of Y/N for the software developers

    soft_dev = (
        df.groupby(["Year"])[
            "rse1. Do you write software for academic research as part of your job"
        ]
        .value_counts()
        .to_frame()
    )
    # Get the count of Y/N for the leader developers
    soft_lead = (
        df.groupby(["Year"])[
            "rse4de. Does the majority of your role comprise leading a group of software developers or RSEs?"
        ]
        .value_counts()
        .to_frame()
    )
    # Get the count for Y/N to any of the question
    df["any_rse"] = np.where(
        (
            df["rse1. Do you write software for academic research as part of your job"]
            == "Yes"
        )
        | (
            df[
                "rse4de. Does the majority of your role comprise leading a group of software developers or RSEs?"
            ]
        ),
        "Yes",
        "No",
    )
    soft_any = df.groupby(["Year"])["any_rse"].value_counts().to_frame()
    # Create one df
    result = pd.concat([soft_dev, soft_lead, soft_any], axis=1, sort=False)

    # Rename columns
    result.columns = [
        "Write software",
        "Lead a team of software developers",
        "At least one of the two",
    ]
    report.update(table("valid_participants", result))

    # For any further analysis, we remove the participants that answered 'No'
    # at both of the question to only keep the ones that have work involving
    # software development for both year to ensure a proper comparison.

    # Filtering the df
    df = df[df["any_rse"] == "Yes"]
    # drop the column `any_rse` as no use anymore
    df.drop(["any_rse"], axis=1, inplace=True)

    # This brings the number of participants analysed to:
    results = pd.DataFrame.from_dict(
        [
            {
                "Participants in %d" % (year - 1): len(df[df["Year"] == year - 1]),
                "Participants in %d" % year: len(df[df["Year"] == year]),
            }
        ]
    )
    report.update(table("participant_analysed", results))
    return report, None
