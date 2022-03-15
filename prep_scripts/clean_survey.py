"""Cleaning tool to do basic cleaning and amend the column names in a survey data CSV file to match the 2018 survey data."""

import sys
import re
import numpy as np
import pandas as pd

# So we can load the survey and lib stuff
sys.path.insert(1, '.')

from survey.overview_and_sampling import read_salary
from survey.sociodemography import read_anonymised_data


SALARY_COL = 'socio4. Please select the range of your salary'
DEVEXP_COL = 'soft1can. How many years of software development experience do you have?'

# Pre-cleaning
with open('cache/2022-precleaned.csv', 'w') as fout:
    with open('data/2022-raw.csv', 'r') as fin:
        for line in fin:
            line = line.replace('&amp;', '&')
            fout.write(line)

# The precleaned new (2022) survey data
fix_df = pd.read_csv('cache/2022-precleaned.csv', dtype=str, encoding='utf-8')
fix_df['Year'] = 2022

# The reference (2018) data to use
# We need to assemble it from its different parts
ref_df = pd.read_csv('data/2018.csv', encoding='utf-8')
ref_df = ref_df.merge(read_salary('data/2018_salary.csv'), on='startdate. Date started')


def search_replace_column_name(fix_df, col, ref_df, arg):
    ref_cols = [c for c in ref_df.columns if re.match('^' + arg, c)]
    if len(ref_cols) == 0:
        print("**** Zero column matches on replace", arg, len(ref_cols), ref_cols[:2])
        sys.exit(1)
    elif len(ref_cols) > 1:
        print("**** Multiple column matches on replace", arg, len(ref_cols), ref_cols[:2])
        sys.exit(1)
    print("Replacing", col, "with", ref_cols[0] + '...')
    fix_df.columns = [ref_cols[0] if c.startswith(col + '.') else c for c in fix_df.columns]


def rename_column_name(fix_df, col, arg):
    col_to_rename = [c for c in fix_df.columns if c.startswith(col + '.')]
    if len(col_to_rename) == 0:
        print("**** Couldn't find column to rename", col)
        sys.exit(1)
    print("Renaming", col, "with", arg + '...')
    fix_df.rename(columns={col_to_rename[0]: arg}, inplace=True)


def delete_column(fix_df, col):
    col_to_delete = [c for c in fix_df.columns if c.startswith(col + '.')]
    if len(col_to_delete) == 1:
        print("Deleting", col)
        fix_df.drop(columns=[col_to_delete[0]], inplace=True)
    else:
        print("**** Incorrect column matching:", col, col_to_delete)
        sys.exit()


# Column processing
# Go through mapping CSV which indicates what to do with each 2022 column
# to make the 2022 data compatible with the 2018 data
# For each 2022 column, this could be Delete the column, Ignore it, a direct Rename, or SearchReplace it
# which renames the column to match one in the 2018 data
mapping_df = pd.read_csv('prep_scripts/survey_column_mapping.csv')
for _, row in mapping_df.iterrows():
    column = row.loc['QID_2022']
    action = row.loc['Action']
    argument = row.loc['Argument']

    if action == 'SearchReplace':
        # Uses a given pattern in the mapping CSV to identify a matching column name
        # in the 2018 data to replace it with
        search_replace_column_name(fix_df, column, ref_df, argument)
    elif action == 'Rename':
        rename_column_name(fix_df, column, argument)
    elif action == 'Delete':
        delete_column(fix_df, column)
    elif action == 'Ignore':
        pass

# Cleaning

# Drop all nan's in software dev experience column
fix_df[DEVEXP_COL] = fix_df[DEVEXP_COL].replace({'15+': '15'})

# Merge socio4 into single column, as per 2018_salary.csv
fix_df[SALARY_COL] = (
    fix_df.loc[:, fix_df.columns.str.startswith("socio4")]
    .fillna("")
    .agg("".join, axis=1)
    .map(str.strip)
)
fix_df = fix_df.loc[:, ~fix_df.columns.str.startswith("socio4q")]

# Clean all prefer not to answer type answers
fix_df.replace('Prefer not to answer', np.NaN, inplace=True)
fix_df.replace('Do not wish to declare', np.NaN, inplace=True)
fix_df.replace('Do not wish to answer', np.NaN, inplace=True)
fix_df.replace("I don't know", np.NaN, inplace=True)
fix_df.replace("Don't want to answer", np.NaN, inplace=True)

# Clean all 'Other' answers, collapse them all into 'Yes'
# This also applies to a single socio5usqus question
# Applies to multiple-choice and single answer style questions
for col in fix_df.columns:
    if col[-7:] == '[Other]':
        # Replace all the values with 'Yes'
        fix_df[col] = fix_df[col].apply(lambda x: 'Yes' if not pd.isnull(x) else np.nan)

fix_df.to_csv('data/2022.csv', index=False)
