# Sociodemography
import sys
import matplotlib
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from lib.analysis import count_diff, plot_cat_comparison
from lib.report import (
    slugify,
    make_report,
    read_cache,
    table_country,
    figure_country,
    COUNTRIES_WITH_WORLD,
)

age = ["socio3. Please select your age"]

age_order = [
    "18 to 24 years",
    "25 to 34 years",
    "35 to 44 years",
    "45 to 54 years",
    "55 to 64 years",
    "Age 65 or older",
    "Prefer not to say",
]

gender = ["socio2. Please select your gender"]

ethn_us = ["socio5usqus._.Do you consider yourself Hispanic or Latino"]

disability = [
    "disa1._.Do you have a condition that is defined as a disability by your country?"
]


def read_anonymised_data(survey_year, data, fillna='No'):
    df = pd.read_csv(data).fillna(fillna)
    df["socio1._.In which country do you work?"].replace(
        {
            "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
            "United States of America": "United States",
        },
        inplace=True,
    )

    df['Year'] = survey_year
    return df.rename({'socio1._.In which country do you work?': 'Country'}, axis=1)


@make_report(__file__)
def run(survey_year, data="data/public_merged.csv"):
    df = read_cache("processed_data").fillna('')
    ethnicity_df = read_anonymised_data(survey_year, 'data/2018_ethnicity.csv')
    disability_df = read_anonymised_data(survey_year, 'data/2018_disability.csv')
    countries = []
    for country in COUNTRIES_WITH_WORLD:
        countries.append({"country": country})
        for category, columns, order_index in [
            ("Age", age, age_order),
            ("Gender", gender, False),
        ]:
            results = count_diff(
                df, columns, country, category, survey_year, order_index=order_index
            )
            countries[-1].update(table_country(country, slugify(category), results))
            plot_cat_comparison(
                results, country=country, category=category, order_index=order_index
            )
            countries[-1].update(figure_country(country, slugify(category), plt))
        if country == "United Kingdom":
            category = 'Ethnicity'
            ethnicity_data = count_diff(
                ethnicity_df,
                [x for x in ethnicity_df.columns if x.startswith('socio5quk')],
                country, category, survey_year, multi_choice=True, disable_past_year=True
            )
            countries[-1].update(table_country(country, "ethnicity", ethnicity_data))
            plot_cat_comparison(results, country=country, category=category)
            countries[-1].update(figure_country(country, "ethnicity", plt))

            disability_data = count_diff(
                disability_df,
                disability,
                country,
                "Officially recognised disability",
                survey_year,
                y_n=True,
                disable_past_year=True
            )
            plot_cat_comparison(disability_data, country=country, category=category)
            countries[-1].update(figure_country(country, "disability", plt))
        if country == "United States":
            hispanic_latino_data = count_diff(
                ethnicity_df, ethn_us, country, category, survey_year, y_n=True
            )
            countries[-1].update(
                table_country(country, "hispanic-or-latino", hispanic_latino_data)
            )
            plot_cat_comparison(
                hispanic_latino_data, country=country, category=category
            )
            countries[-1].update(figure_country(country, "hispanic-or-latino", plt))
    return {"countries": countries}


if __name__ == "__main__":
    run()
