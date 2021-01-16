#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span><ul class="toc-item"><li><span><a href="#Questions-in-this-section" data-toc-modified-id="Questions-in-this-section-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Questions in this section</a></span></li><li><span><a href="#Setting-up" data-toc-modified-id="Setting-up-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Setting up</a></span></li></ul></li><li><span><a href="#Professional-developers" data-toc-modified-id="Professional-developers-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Professional developers</a></span><ul class="toc-item"><li><span><a href="#Australia" data-toc-modified-id="Australia-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Australia</a></span></li><li><span><a href="#Germany" data-toc-modified-id="Germany-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Germany</a></span></li><li><span><a href="#Netherlands" data-toc-modified-id="Netherlands-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Netherlands</a></span></li><li><span><a href="#New-Zealand" data-toc-modified-id="New-Zealand-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>New Zealand</a></span></li><li><span><a href="#South-Africa" data-toc-modified-id="South-Africa-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>South Africa</a></span></li><li><span><a href="#United-Kingdom" data-toc-modified-id="United-Kingdom-2.6"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>United Kingdom</a></span></li><li><span><a href="#United-States" data-toc-modified-id="United-States-2.7"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>United States</a></span></li><li><span><a href="#Rest-of-the-World" data-toc-modified-id="Rest-of-the-World-2.8"><span class="toc-item-num">2.8&nbsp;&nbsp;</span>Rest of the World</a></span></li></ul></li></ul></div>

# # Introduction

# In this section we investigate the relationship between RSEs/RSDs and their own experience in software development
# Understandably, we expect them having several years of software development experience. However, as shown in previous years, it is not necessarily reflected upon their own feeling of being considered as professional. 

# ## Questions in this section
# * `Do you consider yourself a professional software developer?`: Yes-No
# * `How many years of software development experience do you have?`: numeric

# ## Setting up

# In[1]:


get_ipython().run_cell_magic('capture', ' ', '# Import notebook containing the imports the functions and the dataset\n%run "./0. Imports and functions.ipynb"\n\n# Import notebook containing sampled dataset\n%run "./1. Overview and sampling.ipynb"')


# # Professional developers

# In[2]:


prof_dev= ['soft2can. Do you consider yourself a professional software developer?']
year_dev = ['soft1can. How many years of software development experience do you have?']


# ## Australia

# In[3]:


# Plotting the reported 'professional software developer'
country = 'Australia'
category = 'Professional developer'
# Get the count
result = count_diff(df, prof_dev, category=category, country=country, y_n=True)
result


# In[4]:


plot_cat_comparison(result, country, category)


# In[5]:


country = 'Australia'
category = 'How many years of software development experience'
result = describe_diff(df, year_dev, country=country, category=category)
result


# In[6]:


plot_density_func(df, year_dev, country=country, category=category)


# ## Germany

# In[7]:


# Plotting the reported 'professional software developer'
country = 'Germany'
category = 'Professional developer'
# Get the count
result = count_diff(df, prof_dev, category=category, country=country, y_n=True)
result


# In[8]:


plot_cat_comparison(result, country, category)


# In[9]:


# Plotting the reported 'professional software developer'
country = 'Germany'
category = 'How many years of software development experience'
result = describe_diff(df, year_dev, country=country, category=category)
result


# In[10]:


plot_density_func(df, year_dev, country=country, category=category)


# ## Netherlands

# In[11]:


# Plotting the reported 'professional software developer'
country = 'Netherlands'
category = 'Do you consider yourself a professional software developer'
# Get the count
result = count_diff(df, prof_dev, category=category, country=country, y_n=True)
result


# In[12]:


plot_cat_comparison(result, country, category)


# In[13]:


# Plotting the reported 'professional software developer'
country = 'Netherlands'
category = 'How many years of software development experience'
result = describe_diff(df, year_dev, country=country, category=category)
result


# In[14]:


plot_density_func(df, year_dev, country=country, category=category)


# ## New Zealand

# In[15]:


# Plotting the reported 'professional software developer'
country = 'New Zealand'
category = 'Do you consider yourself a professional software developer'
# Get the count
result = count_diff(df, prof_dev, category=category, country=country, y_n=True)
result


# In[16]:


plot_cat_comparison(result, country, category)


# In[17]:


# Software Development experience
country = 'New Zealand'
category = 'How many years of software development experience'
result = describe_diff(df, year_dev, country=country, category=category)
result


# In[18]:


plot_density_func(df, year_dev, country=country, category=category)


# ## South Africa

# In[19]:


# Plotting the reported 'professional software developer'
country = 'South Africa'
category = 'Do you consider yourself a professional software developer'
# Get the count
result = count_diff(df, prof_dev, category=category, country=country, y_n=True)
result


# In[20]:


plot_cat_comparison(result, country, category)


# In[21]:


# Software Development experience
country = 'South Africa'
category = 'How many years of software development experience'
result = describe_diff(df, year_dev, country=country, category=category)
result


# In[22]:


plot_density_func(df, year_dev, country=country, category=category)


# ## United Kingdom

# This year, 63% of participants are self-confident about their status of "professional developer", it is an increase of almost 4% compared to 2017. 
# 
# The number of years as software developers however seems to diminish compare to 2017, from an average of 13 years in 2017, it is an average of 12 years in 2018.

# In[23]:


# Plotting the reported 'professional software developer'
country = 'United Kingdom'
category = 'Do you consider yourself a professional software developer'
# Get the count
result = count_diff(df, prof_dev, category=category, country=country, y_n=True)
result


# In[24]:


plot_cat_comparison(result, country, category)


# In[25]:


# Software Development experience
country = 'United Kingdom'
category = 'How many years of software development experience'
result = describe_diff(df, year_dev, country=country, category=category)
result


# In[26]:


plot_density_func(df, year_dev, country=country, category=category)


# ## United States

# In[27]:


# Plotting the reported 'professional software developer'
country = 'United States'
category = 'Do you consider yourself a professional software developer'
# Get the count
result = count_diff(df, prof_dev, category=category, country=country, y_n=True)
result


# In[28]:


plot_cat_comparison(result, country, category)


# In[29]:


# Software Development experience
country = 'United States'
category = 'How many years of software development experience'
result = describe_diff(df, year_dev, country=country, category=category)
result


# In[30]:


plot_density_func(df, year_dev, country=country, category=category)


# ## Rest of the World

# In[31]:


# Plotting the reported 'professional software developer'
country = 'World'
category = 'Do you consider yourself a professional software developer'
# Get the count
result = count_diff(df, prof_dev, category=category, country=country, y_n=True)
result


# In[32]:


plot_cat_comparison(result, country, category)


# In[33]:


# Software Development experience
country = 'World'
category = 'How many years of software development experience'
result = describe_diff(df, year_dev, country=country, category=category)
result


# In[34]:


plot_density_func(df, year_dev, country=country, category=category)

