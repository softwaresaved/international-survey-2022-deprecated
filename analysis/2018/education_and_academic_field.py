#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span><ul class="toc-item"><li><span><a href="#Questions-in-this-section" data-toc-modified-id="Questions-in-this-section-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Questions in this section</a></span></li><li><span><a href="#Setting-up" data-toc-modified-id="Setting-up-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Setting up</a></span></li></ul></li><li><span><a href="#Levels-of-education" data-toc-modified-id="Levels-of-education-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Levels of education</a></span><ul class="toc-item"><li><span><a href="#Australia" data-toc-modified-id="Australia-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Australia</a></span></li><li><span><a href="#Germany" data-toc-modified-id="Germany-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Germany</a></span></li><li><span><a href="#Netherlands" data-toc-modified-id="Netherlands-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Netherlands</a></span></li><li><span><a href="#New-Zealand" data-toc-modified-id="New-Zealand-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>New Zealand</a></span></li><li><span><a href="#South-Africa" data-toc-modified-id="South-Africa-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>South Africa</a></span></li><li><span><a href="#United-Kingdom" data-toc-modified-id="United-Kingdom-2.6"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>United Kingdom</a></span></li><li><span><a href="#United-States" data-toc-modified-id="United-States-2.7"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>United States</a></span></li><li><span><a href="#Rest-of-the-World" data-toc-modified-id="Rest-of-the-World-2.8"><span class="toc-item-num">2.8&nbsp;&nbsp;</span>Rest of the World</a></span></li><li><span><a href="#Comparison-between-countries" data-toc-modified-id="Comparison-between-countries-2.9"><span class="toc-item-num">2.9&nbsp;&nbsp;</span>Comparison between countries</a></span></li></ul></li><li><span><a href="#Academic-field-for-education-and-professional-development" data-toc-modified-id="Academic-field-for-education-and-professional-development-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Academic field for education and professional development</a></span><ul class="toc-item"><li><span><a href="#Australia" data-toc-modified-id="Australia-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Australia</a></span></li><li><span><a href="#Germany" data-toc-modified-id="Germany-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Germany</a></span></li><li><span><a href="#Netherlands" data-toc-modified-id="Netherlands-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Netherlands</a></span></li><li><span><a href="#New-Zealand" data-toc-modified-id="New-Zealand-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>New Zealand</a></span></li><li><span><a href="#South-Africa" data-toc-modified-id="South-Africa-3.5"><span class="toc-item-num">3.5&nbsp;&nbsp;</span>South Africa</a></span></li><li><span><a href="#United-Kingdom" data-toc-modified-id="United-Kingdom-3.6"><span class="toc-item-num">3.6&nbsp;&nbsp;</span>United Kingdom</a></span></li><li><span><a href="#United-States" data-toc-modified-id="United-States-3.7"><span class="toc-item-num">3.7&nbsp;&nbsp;</span>United States</a></span></li><li><span><a href="#Rest-of-the-world" data-toc-modified-id="Rest-of-the-world-3.8"><span class="toc-item-num">3.8&nbsp;&nbsp;</span>Rest of the world</a></span></li><li><span><a href="#Comparison-between-countries" data-toc-modified-id="Comparison-between-countries-3.9"><span class="toc-item-num">3.9&nbsp;&nbsp;</span>Comparison between countries</a></span></li></ul></li><li><span><a href="#Academic-field-of-work" data-toc-modified-id="Academic-field-of-work-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Academic field of work</a></span><ul class="toc-item"><li><span><a href="#Australia" data-toc-modified-id="Australia-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Australia</a></span></li><li><span><a href="#Germany" data-toc-modified-id="Germany-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Germany</a></span></li><li><span><a href="#Netherlands" data-toc-modified-id="Netherlands-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>Netherlands</a></span></li><li><span><a href="#New-Zealand" data-toc-modified-id="New-Zealand-4.4"><span class="toc-item-num">4.4&nbsp;&nbsp;</span>New Zealand</a></span></li><li><span><a href="#South-Africa" data-toc-modified-id="South-Africa-4.5"><span class="toc-item-num">4.5&nbsp;&nbsp;</span>South Africa</a></span></li><li><span><a href="#United-Kingdom" data-toc-modified-id="United-Kingdom-4.6"><span class="toc-item-num">4.6&nbsp;&nbsp;</span>United Kingdom</a></span></li><li><span><a href="#United-States" data-toc-modified-id="United-States-4.7"><span class="toc-item-num">4.7&nbsp;&nbsp;</span>United States</a></span></li><li><span><a href="#Rest-of-the-World" data-toc-modified-id="Rest-of-the-World-4.8"><span class="toc-item-num">4.8&nbsp;&nbsp;</span>Rest of the World</a></span></li></ul></li></ul></div>

# # Introduction

# This section contains the information about the type of education the participants have, as well as their highest degree obtained.
# 
# We asked the participants, in which field they are working. With that question, it is possible to see which current field employed the most of RSE/RSD. The questions was specific to each country and was multiple choice. Each participant could choose several fields. We then calculate the different proportion by dividing each field by the total of participants that have selected at least one option. 

# ## Questions in this section
# 
# * `What is the highest level of education you have attained?`: one choice list
# * `In which discipline is your highest academic qualification?`: one choice list
# * `Which professional qualification do you hold?`: free text

# ## Setting up

# In[1]:


get_ipython().run_cell_magic('capture', '', '\n# Import notebook containing the imports the functions and the dataset\n%run "./0. Imports and functions.ipynb"\n\n# Import notebook containing sampled dataset\n%run "./1. Overview and sampling.ipynb"')


# In[2]:


plt.rcParams['figure.figsize'] = [20.0, 10.0]


# # Levels of education 

# In[3]:


education_column = 'edu1. What is the highest level of education you have attained?'


# ## Australia

# In[4]:


# Set up variables
country = 'Australia'
category = 'Highest level of education'

# Get the count
result = count_diff(df, columns=education_column, category=category, country=country)

# Showing the results
result


# In[5]:


plot_cat_comparison(result, country, category)


# ## Germany

# In[6]:


# Set up variables
country = 'Germany'
category = 'Highest level of education'

# Get the count
result = count_diff(df, columns=education_column, category=category, country=country)

# Showing the results
result


# In[7]:


plot_cat_comparison(result, country, category)


# ## Netherlands

# In[8]:


# Set up variables
country = 'Netherlands'
category = 'Highest level of education'

# Get the count
result = count_diff(df, columns=education_column, category=category, country=country)

# Showing the results
result


# In[9]:


plot_cat_comparison(result, country, category)


# ## New Zealand

# In[10]:


# Set up variables
country = 'New Zealand'
category = 'Highest level of education'

# Get the count
result = count_diff(df, columns=education_column, category=category, country=country)

# Showing the results
result


# In[11]:


plot_cat_comparison(result, country, category)


# ## South Africa

# In[12]:


# Set up variables
country = 'South Africa'
category = 'Highest level of education'

# Get the count
result = count_diff(df, columns=education_column, category=category, country=country)

# Showing the results
result


# In[13]:


plot_cat_comparison(result, country, category)


# ## United Kingdom

# In 2018, the proportion of participants that hold a PhD is 70%. This majority confirm the tendency from last year with an increase of 2%. 
# Only 20% holds a Master degree as the highest education, and 8% an Undergraduate degree.

# In[14]:


# Get the count for the 2017 year
country = 'United Kingdom'
category = 'Highest level of education'

# Get the count
result = count_diff(df, columns=education_column, category=category, country=country)

# Showing the results
result


# In[15]:


plot_cat_comparison(result, country, category)


# ## United States

# In[16]:


# Set up variables
country = 'United States'
category = 'Highest level of education'

# Get the count
result = count_diff(df, columns=education_column, category=category, country=country)

# Showing the results
result


# In[17]:


plot_cat_comparison(result, country, category)


# ## Rest of the World

# For the rest of the world, the question is a `free text` type. Therefore, some cleaning are needed to render the results intelligible. 
# After manually cleaning the data, it appears that a vast majority of participants hold a PhD (64%), while 14% have a Master degree and only 9% have an Undergraduate degree.

# In[18]:


dict_values = {'phd': 'Doctorate', 
               'phd in progress': 'Doctorate',
               'mphil to phd transfer': 'Doctorate',
               'dr phil': 'Doctorate',
               'master of science': 'Master degree',
               'master': 'Master degree',
               'masters': 'Master degree',
               'master in science': 'Master degree',
               'postgraduate': 'Master degree',
               'msc': 'Master degree',
               'bachelors degree': 'Undergraduate degree',
               'bachelors  in computer science': 'Undergraduate degree',
               'bachelor': 'Undergraduate degree',
               'bachelors': 'Undergraduate degree',
               'nan': np.NaN
               }
df.loc[df['Country'] == 'World', education_column] = df.loc[df['Country'] == 'World', education_column].str.replace('.', '').str.replace("'", "").str.replace('degree', '').str.strip().str.lower()
df.loc[df['Country'] == 'World', education_column] = df.loc[df['Country'] == 'World', education_column].replace(dict_values)


# In[19]:


# Set up variables
country = 'World'
category = 'Highest level of education'

# Get the count
result = count_diff(df, columns=education_column, category=category, country=country)

# Showing the results
result


# In[20]:


plot_cat_comparison(result, country, category)


# ## Comparison between countries

# Even if the countries have different education levels, it is possible to match them on the common "Doctorate" and "Master degree". 
# Therefore we compare them with these two equivalent levels and merge all others under the category "other".

# In[21]:


# Create dictionary to replace values. These values may not be present in the current df but are present in the
# potential answers
dict_values = {'PhD': 'Doctorate', 
               'AQF 10 - Doctoral Degree': 'Doctorate',
               'HBO (Hoger beroepsonderwijs) Master': 'Master degree',
               'WO (Wetenschappelijk onderwijs) Master': 'Master degree',
               'AQF 9 - Masters Degree': 'Master degree'}
list_value_to_keep = ['Doctorate', 'Master degree', np.NaN]

# Replace the value in education
df['education comparison'] = df[education_column].replace(dict_values)

# Create a new columns if "World" if the country is not in the list
def merge_edu(x):
    if x in list_value_to_keep:
        return x
    elif x == np.NaN:
        return x
    else:
        return 'Other'
    
# Apply the function to a new columns
df['education comparison'] = df['education comparison'].apply(merge_edu)

# Count the values per countries
df_edu_comparison = df[['Country', 'education comparison']].groupby('Country')['education comparison'].value_counts().rename('Total count').reset_index()

# Add a percentage of each type of diploma per countries
df_edu_comparison['Percentage per countries'] = (df_edu_comparison['Total count'] / df_edu_comparison.groupby('Country')['Total count'].transform('sum')*100).round(2)

# Display the results
df_edu_comparison


# In[22]:


fig, ax = plt.subplots()
df_plot = df_edu_comparison.pivot(index='Country', 
                        columns='education comparison', 
                        values='Percentage per countries')
df_plot.plot(kind='barh',
                  title='Percentage of Doctorate and Master per country',
                  grid=False, ax=ax)

ax.set(xlabel="Percentage", ylabel="Country")

ax.invert_yaxis()  # when barh option, the bars are inverted 
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False) 
for p in ax.patches:
    if int(round(p.get_width())) > 0:
        ax.annotate('{}%'.format(str(int(round(p.get_width())))), 
                                 (p.get_x() + p.get_width(), p.get_y()), 
                                  xytext=(5, -9),
                                  textcoords='offset points')
plt.show();


# # Academic field for education and professional development

# Alongside of question about education level we also asked the participants in which field they finished their highest level of education. 
# Here again the propositions were specific to each countries so the comparison is difficult despite lot of overlapping in the categories. 

# In[23]:


# Create a column that merge all education columns
df_edu_field = df[['Year', 'Country']].copy()

# There are numbers in some of the fields, removing them as they are not needed
def remove_digit(s):
    try:
        return ''.join([i for i in s if not i.isdigit()])
    except TypeError:
        return s

df['Academic field'] = df['edu2. In which discipline is your highest academic qualification?'].apply(remove_digit)
columns = 'Academic field'

prof_qual = ['edu4. List any professional qualifications you hold (eg. P. Eng, PMP, …)?']


# ## Australia

# In[24]:


# Set up variables
country = 'Australia'
category = 'Field of education'
result = count_diff(df, columns, country, category)
result


# In[25]:


plot_cat_comparison(result, country, 'Field of education')


# In[26]:


plot_wordcloud(df, country=country, category='Professional qualification', columns=prof_qual)


# ## Germany

# In[27]:


# Set up variables
country = 'Germany'
category = 'Field of education'
result = count_diff(df, columns, country, category)
result


# In[28]:


plot_cat_comparison(result, country, category)


# In[29]:


plot_wordcloud(df, country=country, category='Professional qualification', columns=prof_qual)


# ## Netherlands

# In[30]:


# Set up variables
country = 'Netherlands'
category = 'Field of education'
result = count_diff(df, columns, country, category)
result


# In[31]:


plot_cat_comparison(result, country, category)


# In[32]:


plot_wordcloud(df, country=country, category='Professional qualification', columns=prof_qual)


# ## New Zealand

# In[33]:


# Set up variables
country = 'New Zealand'
category = 'Field of education'
result = count_diff(df, columns, country, category)
result


# In[34]:


plot_cat_comparison(result, country, category)


# In[35]:


plot_wordcloud(df, country=country, category='Professional qualification', columns=prof_qual)


# ## South Africa

# In[36]:


# Set up variables
country = 'South Africa'
category = 'Field of education'
result = count_diff(df, columns, country, category)
result


# In[37]:


plot_cat_comparison(result, country, category)


# In[38]:


plot_wordcloud(df, country=country, category='Professional qualification', columns=prof_qual)


# ## United Kingdom

# In[39]:


# Set up variables
country = 'United Kingdom'
category = 'Field of education'
result = count_diff(df, columns, country, category)
result


# In[40]:


plot_cat_comparison(result, country, category)


# In[41]:


plot_wordcloud(df, country=country, category='Professional qualification', columns=prof_qual)


# ## United States

# In[42]:


# Set up variables
country = 'United States'
category = 'Field of education'
result = count_diff(df, columns, country, category)
result


# In[43]:


plot_cat_comparison(result, country, category)


# In[44]:


plot_wordcloud(df, country=country, category='Professional qualification', columns=prof_qual)


# ## Rest of the world

# In[45]:


# Set up variables
country = 'World'
category = 'Field of education'
result = count_diff(df, columns, country, category)
result


# In[46]:


plot_cat_comparison(result, country, category)


# In[47]:


plot_wordcloud(df, country=country, category='Professional qualification', columns=prof_qual)


# ## Comparison between countries

# In[48]:


# Count the values per countries
#df_edu_comparison = df_edu_field.groupby('Country')['Academic field'].value_counts().rename('Total count').reset_index()

# Add a percentage of each type of diploma per countries
#df_edu_comparison['Percentage per countries'] = (df_edu_comparison['Total count'] / df_edu_comparison.groupby('Country')['Total count'].transform('sum')*100)

# Display the results
#df_edu_comparison


# In[49]:


#fig, ax = plt.subplots()
#df_plot = df_edu_comparison.pivot(index='Country', 
#                        columns='Academic field', 
#                        values='Percentage per countries')

#df_plot.plot(kind='barh',
#                  title='Percentage of academic field per country',
#                  grid=False, ax=ax, stacked=True)

#ax.set(xlabel="Country", ylabel="Percentage")

#ax.invert_yaxis()  # when barh option, the bars are inverted 
#ax.spines['top'].set_visible(False)
#ax.spines['right'].set_visible(False)
#ax.spines['left'].set_visible(False) 
# Put a legend below current axis
#ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
#          fancybox=True, shadow=True, ncol=5)
#for p in ax.patches:
#    if int(round(p.get_width())) >= 5:
#        ax.annotate('{}%'.format(str(int(round(p.get_width())))), 
#                    (p.get_x() + int(p.get_width())/2., p.get_y()+ int(p.get_height())/2.),
#                    ha='center')

#plt.show();


# # Academic field of work

# In[50]:


# Getting all the questions about the academic field of the current employment. 
to_sub = [x for x in df.columns if x[:12] == 'currentEmp13']


# ## Australia

# In[51]:


country = 'Australia'


# In[52]:


category = 'field of work'

# Get the count
result = count_diff(df, columns=to_sub, category=category, country=country, multi_choice=True)

# Showing the results
result


# In[53]:


plot_cat_comparison(result, country, category)


# ## Germany

# In[54]:


country = 'Germany'


# In[55]:


category = 'field of work'

# Get the count
result = count_diff(df, columns=to_sub, category=category, country=country, multi_choice=True)

# Showing the results
result


# ## Netherlands

# In[56]:


country = 'Netherlands'


# In[57]:


category = 'field of work'

# Get the count
result = count_diff(df, columns=to_sub, category=category, country=country, multi_choice=True)

# Showing the results
result


# ## New Zealand

# In[58]:


country = 'New Zealand'


# In[59]:


category = 'field of work'

# Get the count
result = count_diff(df, columns=to_sub, category=category, country=country, multi_choice=True)

# Showing the results
result


# ## South Africa

# In[60]:


country = 'South Africa'


# In[61]:


category = 'field of work'

# Get the count
result = count_diff(df, columns=to_sub, category=category, country=country, multi_choice=True)

# Showing the results
result


# ## United Kingdom

# Most RSEs derive from a background in Physics and Astronomy (38%), followed by Computer science (37%) and finally by Biological sciences (28%). This top three is very different than the results in 2017, while Computer science was the first academic field (42%) and second was Physics and Astronomy (33%).

# In[62]:


country = 'United Kingdom'


# In[63]:


category = 'field of work'

# Get the count
result = count_diff(df, columns=to_sub, category=category, country=country, multi_choice=True)

# Showing the results
result


# ## United States

# In[64]:


country = 'United States'


# In[65]:


category = 'field of work'

# Get the count
result = count_diff(df, columns=to_sub, category=category, country=country, multi_choice=True)

# Showing the results
result


# ## Rest of the World

# In[66]:


country = 'World'


# In[67]:


category = 'field of work'

# Get the count
result = count_diff(df, columns=to_sub, category=category, country=country, multi_choice=True)

# Showing the results
result

