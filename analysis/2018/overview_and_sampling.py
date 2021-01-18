#!/usr/bin/env python
import sys
import chevron
import numpy as np
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path

FN = Path(__file__).stem
TEMPLATE = Path("../templates/") / (FN + ".md")
OUTPUT = Path(FN + ".md")

if not TEMPLATE.exists():
    print("E: Did not find template corresponding to file in ../templates")
    sys.exit(1)


YEAR = 2018
PREV_YEAR = YEAR - 1
DATA = {}

# Ensure these paths are present
PATHS = [Path(x) for x in ["csv", "fig"]]

for p in PATHS:
    if not p.exists():
        p.mkdir()

df = pd.read_csv("./data/public_merged.csv")

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

# Create a list of all countries of interest
list_countries = [
    "United Kingdom",
    "Australia",
    "United States",
    "Germany",
    "New Zealand",
    "Netherlands",
    "South Africa",
]

# Create a new columns if "World" if the country is not in the list
df["Country"] = df["socio1. In which country do you work?"].apply(
    lambda x: x if x in list_countries else "World"
)

# This is the total of participants. A participants is defined as a person
# that have reached, at least the second section in the survey.

DATA["n_participants"] = len(df[df["Year"] == YEAR])


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
# We can see the distribution of participants among the countries as follow:

# Output the count per countries
df[df["Year"] == 2018][
    "socio1. In which country do you work?"
].value_counts().to_frame()


# ## Visual representation of countries repartition


def add_table(name, data):
    csv = "csv/%s.csv" % name
    DATA["t_" + name] = data.to_markdown() + "\n\n[Download CSV](%s)" % csv
    data.to_csv(csv, index=False)


def add_figure(name, plt):
    figpath = "fig/%s.png" % name
    plt.savefig(figpath)
    DATA["f_" + name] = "![%s][%s]" % (name, figpath)


df_countries = (
    df[df["Year"] == 2018]["socio1. In which country do you work?"]
    .value_counts()
    .to_frame()
    .reset_index()
)
add_table("participant", df_countries)
df_countries.columns = ["name", "count"]


def convert_time(x):
    try:
        return datetime.datetime.strptime(str(x), "%Y-%m-%d %H:%M:%S").date()
    except ValueError:
        return x


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

    axes[a, b].xaxis.set_major_locator(mdates.DayLocator(interval=10))  # every 10 days
    axes[a, b].xaxis.set_minor_locator(mdates.DayLocator(interval=1))  # every day
    for label in axes[a, b].get_xticklabels():
        label.set_rotation(45)
    list_plots.append(axes[a, b])

for ax in list_plots:
    ax.set(xlabel="Date of submission", ylabel="Count")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

add_figure("participation_date", plt)

# Difference with the previous year

# Several countries did the survey last year, here a summary of the
# difference in the amount of participants.

results = dict()
for country in df[df["Year"] == 2017]["Country"].unique():
    current_year = df[df["Year"] == 2018]["Country"].value_counts()[country]
    previous_year = df[df["Year"] == 2017]["Country"].value_counts()[country]
    results[country] = {"2017": previous_year, "2018": current_year}
diff_year_participants = pd.DataFrame.from_dict(results, orient="index")
diff_year_participants["Difference between 2017 and 2018"] = (
    diff_year_participants["2018"] - diff_year_participants["2017"]
)
add_table("difference_with_previous_year", diff_year_participants)


# Plotting the difference
ax = diff_year_participants.plot(kind="bar")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
add_figure("difference_with_previous_year", plt)


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
1
# Rename columns
result.columns = [
    "Write software",
    "Lead a team of software developers",
    "At least one of the two",
]
add_table("valid_participants", result)


# For any further analysis, we remove the participants that answered 'No'
# at both of the question to only keep the ones that have work involving
# software development for both year to ensure a proper comparison.

# Filtering the df
df = df[df["any_rse"] == "Yes"]
# drop the column `any_rse` as no use anymore
df.drop(["any_rse"], axis=1, inplace=True)


# This brings the number of participants analysed to:

# In[20]:


results = pd.DataFrame.from_dict(
    [
        {
            "Participants in 2017": len(df[df["Year"] == 2017]),
            "Participants in 2018": len(df[df["Year"] == 2018]),
        }
    ]
)
add_table("participant_analysed", results)

with TEMPLATE.open() as fp:
    OUTPUT.write_text(chevron.render(fp, DATA))
