#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span><ul class="toc-item"><li><span><a href="#Setup" data-toc-modified-id="Setup-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Setup</a></span></li><li><span><a href="#Cleaning" data-toc-modified-id="Cleaning-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Cleaning</a></span><ul class="toc-item"><li><span><a href="#Rename-US-and-UK" data-toc-modified-id="Rename-US-and-UK-1.2.1"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Rename US and UK</a></span></li><li><span><a href="#Create-a-category-world" data-toc-modified-id="Create-a-category-world-1.2.2"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>Create a category world</a></span></li></ul></li></ul></li><li><span><a href="#Overview" data-toc-modified-id="Overview-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Overview</a></span><ul class="toc-item"><li><span><a href="#Total-participants" data-toc-modified-id="Total-participants-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Total participants</a></span></li><li><span><a href="#Repartition-per-country" data-toc-modified-id="Repartition-per-country-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Repartition per country</a></span></li><li><span><a href="#Visual-representation-of-countries-repartition" data-toc-modified-id="Visual-representation-of-countries-repartition-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Visual representation of countries repartition</a></span></li><li><span><a href="#Date-of-participation" data-toc-modified-id="Date-of-participation-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Date of participation</a></span></li><li><span><a href="#Difference-with-the-previous-year" data-toc-modified-id="Difference-with-the-previous-year-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Difference with the previous year</a></span></li></ul></li><li><span><a href="#Subsetting" data-toc-modified-id="Subsetting-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Subsetting</a></span><ul class="toc-item"><li><span><a href="#Selecting-valid-participants-only" data-toc-modified-id="Selecting-valid-participants-only-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Selecting valid participants only</a></span></li></ul></li></ul></div>

# # Introduction

# This notebook gives an overview of the participants per country. From
# where they come from and when they started the survey. It also gives the
# difference with the previous year for the countries that participated in
# 2017.
# 
# Alongside this information, it also subset the relevant participants for
# future analysis. Only the participants that have finished at least the
# first section and the ones that report to develop program for their work,
# or lead research developers, are kept.

# ## Setup

# In[1]:


get_ipython().run_cell_magic('capture', ' ', '# Import notebook containing the imports the functions and the dataset\n%run "./0. Imports and functions.ipynb"')


# In[2]:


get_ipython().magic('matplotlib inline')  # Activate that line to use in Jupyter 
matplotlib.rcParams['figure.figsize'] = (20.0, 10.0)
plt.rcParams['figure.figsize'] = (20.0, 10.0)


# In[3]:


# Loading dataset
try:
    df =  pd.read_csv('./data/clean_merged.csv')
except FileNotFoundError:
    df =  pd.read_csv('./../data/clean_merged.csv')


# ## Cleaning

# The cleaning is about renaming some countries and create a globa category for all countries that are not from one of the participating countries. 

# ### Rename US and UK

# In[4]:


# Rename the Uk and US
df['socio1. In which country do you work?'].replace({'United Kingdom of Great Britain and Northern Ireland': "United Kingdom",
            'United States of America': 'United States'}, inplace=True)

# Drop Canada
df = df[df['socio1. In which country do you work?'] != 'Canada']


# ### Create a category world

# As said, we are concerned about some countries specifically. However, we collected information about other countries as well. To avoid any confusion and having too much countries to plot, we group all of them into one category "world"

# In[5]:


# Create a list of all countries of interest
list_countries = ['United Kingdom', 'Australia', 'United States', 'Germany', 'New Zealand', 'Netherlands', 'South Africa']

# Create a new columns if "World" if the country is not in the list
df['Country'] = df['socio1. In which country do you work?'].apply(lambda x: x if x in list_countries else 'World')


# # Overview

# ## Total participants

# This is the total of participants. A participants is defined as a person that have reached, at least the second section in the survey.

# In[6]:


len(df[df['Year']== 2018])


# ## Repartition per country

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

# In[7]:


# Output the count per countries
df[df['Year']== 2018]['socio1. In which country do you work?'].value_counts().to_frame()


# ## Visual representation of countries repartition

# In[8]:


df_countries = df[df['Year']== 2018]['socio1. In which country do you work?'].value_counts().to_frame().reset_index()
df_countries.columns = ['name', 'count'] 


# In[9]:


df_map = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# Merge datasets together and replace nan with 0
df_map = df_map.merge(df_countries, on='name', how='outer')
df_map.fillna(0, inplace=True)


# In[10]:


def transform_int_to_cat(x):
    if x == 0:
        return '0'
    elif x > 0 and x <= 5:
        return '1 - 5'
    elif x >5 and x <10:
        return '6 - 10'
    elif x >10 and x <=25:
        return '11 - 25'
    elif x > 25 and x <= 50:
        return '26 - 50'
    elif x > 50 and x <=100:
        return '51 - 100'
    elif x > 100 and x <=200:
        return '101 - 200'
    elif x > 200:
        return '200+'
    else:
        raise
df_map['count_cat'] = df_map['count'].apply(lambda x: transform_int_to_cat(x))


# In[11]:


list_ordering = ['0', '1 - 5', '6 - 10', '11 - 25', '26 - 50', '51 - 100', '101 - 200', '200+']  
df_map['count_cat'] = pd.Categorical(df_map['count_cat'], categories=list_ordering)
df_map = df_map.sort_values(['count'])


# In[12]:


fig, ax = plt.subplots(1)
ax = df_map.plot(ax=ax, column='count', cmap='Reds', linewidth=0.8, edgecolor='0.8', legend=False, categorical=True)

# Add the description
description = """"Number of participants per country"""
#ax.annotate(description, xy=(0.1, .08), xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
# Remove axis
ax.axis('off')
plt.show();


# ## Date of participation

# In[13]:


def convert_time(x):
    """"""
    try:
        return datetime.datetime.strptime(str(x),'%Y-%m-%d %H:%M:%S').date()

    except ValueError:
        return x

df['Date'] = df['startdate. Date started'].apply(lambda x: convert_time(x))
df_submission_per_country = df[['Country', 'Date']]#.dropna()
total_per_country = df_submission_per_country.groupby(['Country'])['Date'].value_counts().to_frame()
total_per_country.columns = ['Count']
total_per_country = total_per_country.reset_index().sort_values(['Date', 'Country'], ascending=True)


# In[14]:


fig, axes = plt.subplots(2, 4, figsize=(20, 10))
fig.tight_layout()
fig.subplots_adjust(hspace=0.5)
list_plots = list()
for i, name in enumerate(total_per_country['Country'].unique()):
    if i < 4:
        a = 0
        b = i
    else:
        a = 1
        b = 5 - i    
    axes[a, b] = total_per_country[total_per_country.Country == name].plot(x='Date', y='Count', legend=False, ax=axes[a, b])
    axes[a, b].set_title('{}'.format(name))
    #axes[a, b].set_xticklabels(labels=idx)

    axes[a, b].xaxis.set_major_locator(mdates.DayLocator(interval=10))   # every 10 days
    axes[a, b].xaxis.set_minor_locator(mdates.DayLocator(interval=1))    # every day
    for label in axes[a, b].get_xticklabels():
        label.set_rotation(45) 
    list_plots.append(axes[a, b])

for ax in list_plots:
    ax.set(xlabel="Date of submission", ylabel="Count")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

plt.show();


# ## Difference with the previous year

# Several countries did the survey last year, here a summary of the difference in the amount of participants.

# In[15]:


results = dict()
for country in df[df['Year']== 2017]['Country'].unique():
    current_year = df[df['Year']== 2018]['Country'].value_counts()[country]
    previous_year = df[df['Year']== 2017]['Country'].value_counts()[country]
    results[country] = {'2017': previous_year, '2018': current_year}
diff_year_participants = pd.DataFrame.from_dict(results, orient='index')
diff_year_participants['Difference between 2017 and 2018'] = diff_year_participants['2018'] - diff_year_participants['2017']

# Displaying the results
diff_year_participants


# In[16]:


# Plotting the difference
ax = diff_year_participants.plot(kind='bar')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False) 

plt.show();


# # Subsetting

# ## Selecting valid participants only

# On the total of participants, we only want the participants that code software during their work. 
# We had a specific question for this purpose. We asked the participants if they are writing software or if they are leading a group of software developers. Each of these questions had the possibility of Yes/No answer. Here the exact wording of the questions:
# 
# * Do you write software for academic research as part of your job
# * Does the majority of your role comprise leading a group of software developers or RSEs?
# 
# We will only select the participants who answered `Yes` to at least one question.

# In[17]:


# Get the count of Y/N for the software developers

soft_dev = df.groupby(['Year'])['rse1. Do you write software for academic research as part of your job'].value_counts().to_frame()
# Get the count of Y/N for the leader developers
soft_lead = df.groupby(['Year'])['rse4de. Does the majority of your role comprise leading a group of software developers or RSEs?'].value_counts().to_frame()
# Get the count for Y/N to any of the question
df['any_rse'] = np.where((df['rse1. Do you write software for academic research as part of your job'] == 'Yes') | (df['rse4de. Does the majority of your role comprise leading a group of software developers or RSEs?']), 'Yes', 'No')
soft_any = df.groupby(['Year'])['any_rse'].value_counts().to_frame()
# Create one df
result = pd.concat([soft_dev, soft_lead, soft_any], axis=1, sort=False)
1
# Rename columns
result.columns = ['Write software', 'Lead a team of software developers', 'At least one of the two']
result


# For any further analysis, we remove the participants that answered 'No' at both of the question to only keep the ones that have work involving software development for both year to ensure a proper comparison. 

# In[18]:


# Filtering the df
df = df[df['any_rse'] == 'Yes']
# drop the column `any_rse` as no use anymore
df.drop(['any_rse'], axis=1, inplace=True)


# This brings the number of participants analysed to:

# In[20]:


results = pd.DataFrame.from_dict([{'Participants in 2017': len(df[df['Year'] == 2017]), 
 'Participants in 2018': len(df[df['Year'] == 2018])}])
results

