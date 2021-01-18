#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span><ul class="toc-item"><li><span><a href="#Questions-in-this-section" data-toc-modified-id="Questions-in-this-section-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Questions in this section</a></span></li><li><span><a href="#Setting-up" data-toc-modified-id="Setting-up-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Setting up</a></span></li></ul></li><li><span><a href="#Socio-demographic" data-toc-modified-id="Socio-demographic-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Socio demographic</a></span><ul class="toc-item"><li><span><a href="#Australia" data-toc-modified-id="Australia-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Australia</a></span><ul class="toc-item"><li><span><a href="#Age" data-toc-modified-id="Age-2.1.1"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>Age</a></span></li><li><span><a href="#Gender" data-toc-modified-id="Gender-2.1.2"><span class="toc-item-num">2.1.2&nbsp;&nbsp;</span>Gender</a></span></li></ul></li><li><span><a href="#Germany" data-toc-modified-id="Germany-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Germany</a></span><ul class="toc-item"><li><span><a href="#Age" data-toc-modified-id="Age-2.2.1"><span class="toc-item-num">2.2.1&nbsp;&nbsp;</span>Age</a></span></li><li><span><a href="#Gender" data-toc-modified-id="Gender-2.2.2"><span class="toc-item-num">2.2.2&nbsp;&nbsp;</span>Gender</a></span></li></ul></li><li><span><a href="#Netherlands" data-toc-modified-id="Netherlands-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Netherlands</a></span><ul class="toc-item"><li><span><a href="#Age" data-toc-modified-id="Age-2.3.1"><span class="toc-item-num">2.3.1&nbsp;&nbsp;</span>Age</a></span></li><li><span><a href="#Gender" data-toc-modified-id="Gender-2.3.2"><span class="toc-item-num">2.3.2&nbsp;&nbsp;</span>Gender</a></span></li></ul></li><li><span><a href="#New-Zealand" data-toc-modified-id="New-Zealand-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>New Zealand</a></span><ul class="toc-item"><li><span><a href="#Age" data-toc-modified-id="Age-2.4.1"><span class="toc-item-num">2.4.1&nbsp;&nbsp;</span>Age</a></span></li><li><span><a href="#Gender" data-toc-modified-id="Gender-2.4.2"><span class="toc-item-num">2.4.2&nbsp;&nbsp;</span>Gender</a></span></li></ul></li><li><span><a href="#South-Africa" data-toc-modified-id="South-Africa-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>South Africa</a></span><ul class="toc-item"><li><span><a href="#Age" data-toc-modified-id="Age-2.5.1"><span class="toc-item-num">2.5.1&nbsp;&nbsp;</span>Age</a></span></li><li><span><a href="#Gender" data-toc-modified-id="Gender-2.5.2"><span class="toc-item-num">2.5.2&nbsp;&nbsp;</span>Gender</a></span></li></ul></li><li><span><a href="#United-Kingdom" data-toc-modified-id="United-Kingdom-2.6"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>United Kingdom</a></span><ul class="toc-item"><li><span><a href="#Age" data-toc-modified-id="Age-2.6.1"><span class="toc-item-num">2.6.1&nbsp;&nbsp;</span>Age</a></span></li><li><span><a href="#Gender" data-toc-modified-id="Gender-2.6.2"><span class="toc-item-num">2.6.2&nbsp;&nbsp;</span>Gender</a></span></li><li><span><a href="#Ethnicity" data-toc-modified-id="Ethnicity-2.6.3"><span class="toc-item-num">2.6.3&nbsp;&nbsp;</span>Ethnicity</a></span></li><li><span><a href="#Disability" data-toc-modified-id="Disability-2.6.4"><span class="toc-item-num">2.6.4&nbsp;&nbsp;</span>Disability</a></span></li></ul></li><li><span><a href="#United-States" data-toc-modified-id="United-States-2.7"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>United States</a></span><ul class="toc-item"><li><span><a href="#Age" data-toc-modified-id="Age-2.7.1"><span class="toc-item-num">2.7.1&nbsp;&nbsp;</span>Age</a></span></li><li><span><a href="#Gender" data-toc-modified-id="Gender-2.7.2"><span class="toc-item-num">2.7.2&nbsp;&nbsp;</span>Gender</a></span></li><li><span><a href="#Ethnicity" data-toc-modified-id="Ethnicity-2.7.3"><span class="toc-item-num">2.7.3&nbsp;&nbsp;</span>Ethnicity</a></span></li><li><span><a href="#Hispano-or-Latino" data-toc-modified-id="Hispano-or-Latino-2.7.4"><span class="toc-item-num">2.7.4&nbsp;&nbsp;</span>Hispano or Latino</a></span></li></ul></li><li><span><a href="#Rest-of-the-world" data-toc-modified-id="Rest-of-the-world-2.8"><span class="toc-item-num">2.8&nbsp;&nbsp;</span>Rest of the world</a></span><ul class="toc-item"><li><span><a href="#Age" data-toc-modified-id="Age-2.8.1"><span class="toc-item-num">2.8.1&nbsp;&nbsp;</span>Age</a></span></li><li><span><a href="#Gender" data-toc-modified-id="Gender-2.8.2"><span class="toc-item-num">2.8.2&nbsp;&nbsp;</span>Gender</a></span></li></ul></li></ul></li></ul></div>

# # Introduction

# Here we asked questions to know the socio-demographic composition of our participants, including the age, the gender and the disability and Ethnicity for specific countries

# ## Questions in this section
# 
# * `Please select your age`: one choice
# * `Please select your gender`: one choice
# * `Do you have a condition that is defined as a disability by your country?`: yes-no

# ## Setting up

# In[1]:


get_ipython().run_cell_magic('capture', ' ', '# Import notebook containing the imports the functions and the dataset\n%run "./0. Imports and functions.ipynb"\n\n# Import notebook containing sampled dataset\n%run "./1. Overview and sampling.ipynb"')


# # Socio demographic

# In[2]:


age = ['socio3. Please select your age']

age_order = ['18 to 24 years', '25 to 34 years', '35 to 44 years', '45 to 54 years', '55 to 64 years', 'Age 65 or older', 'Prefer not to say']

gender = ["socio2. Please select your gender"]

ethnicity = [x for x in df.columns if x[:7] == 'socio5.']
ethn_us = ['socio5us. Do you consider yourself Hispanic or Latino']

disability = ['disa1. Do you have a condition that is defined as a disability by your country?']


# ## Australia

# In[3]:


country = 'Australia'


# ### Age

# In[4]:


category = 'Age'
results = count_diff(df, age, country, category, order_index=age_order)
results


# In[5]:


plot_cat_comparison(results, country=country, category=category, order_index=age_order)


# ### Gender

# In[6]:


category = 'Gender'
results = count_diff(df, gender, country, category)
results


# In[7]:


plot_cat_comparison(results, country=country, category=category)


# ## Germany

# In[8]:


country = 'Germany'


# ### Age

# In[9]:


category = 'Age'
results = count_diff(df, age, country, category, order_index=age_order)
results


# In[10]:


plot_cat_comparison(results, country=country, category=category, order_index=age_order)


# ### Gender

# In[11]:


category = 'Gender'
results = count_diff(df, gender, country, category)
results


# In[12]:


plot_cat_comparison(results, country=country, category=category)


# ## Netherlands

# In[13]:


country = 'Netherlands'


# ### Age

# In[14]:


category = 'Age'
results = count_diff(df, age, country, category, order_index=age_order)
results


# In[15]:


plot_cat_comparison(results, country=country, category=category, order_index=age_order)


# ### Gender

# In[16]:


category = 'Gender'
results = count_diff(df, gender, country, category)
results


# In[17]:


plot_cat_comparison(results, country=country, category=category)


# ## New Zealand

# In[18]:


country = 'New Zealand'


# ### Age

# In[19]:


category = 'Age'
results = count_diff(df, age, country, category, order_index=age_order)
results


# In[20]:


plot_cat_comparison(results, country=country, category=category, order_index=age_order)


# ### Gender

# In[21]:


category = 'Gender'
results = count_diff(df, gender, country, category)
results


# In[22]:


plot_cat_comparison(results, country=country, category=category)


# ## South Africa

# In[23]:


country = 'South Africa'


# ### Age

# In[24]:


category = 'Age'
results = count_diff(df, age, country, category, order_index=age_order)
results


# In[25]:


plot_cat_comparison(results, country=country, category=category, order_index=age_order)


# ### Gender

# In[26]:


category = 'Gender'
results = count_diff(df, gender, country, category)
results


# In[27]:


plot_cat_comparison(results, country=country, category=category)


# ## United Kingdom

# Our participants are in vast majority younger than 45 years old (76%) and reflect the previous tendency.
# 
# About the gender, in the 2016 UK survey of RSEs we found a significant gender imbalance in the RSE Community: of the respondents who provided answers (n=263), 88% were male, 11% female and less than 1% described their gender as "other". In the 2017 UK survey, we find that these figures are shifted slightly to 84% male, 15% female and less than 1% who describe their gender as "other". In 2018, the tendency seems to follow the same trend as the proportion of male is 79%. However this lower proportion is due to the fact that this year, the category `Prefer not to say` is included. When we calculate the proportion of male and female only, it remains at 84%. The RSE community in the UK is predominantly male.
# 
# Not surprise either about the ethnicity with a majority of participants being white.

# In[28]:


country = 'United Kingdom'


# ### Age

# In[29]:


category = 'Age'
results = count_diff(df, age, country, category, order_index=age_order)
results


# In[30]:


plot_cat_comparison(results, country=country, category=category, order_index=age_order)


# ### Gender

# In[31]:


category = 'Gender'
results = count_diff(df, gender, country, category)
results


# In[32]:


plot_cat_comparison(results, country=country, category=category)


# ### Ethnicity

# In[33]:


category = 'Ethnicity'
results = count_diff(df, ethnicity, country, category, multi_choice=True)
results


# In[34]:


plot_cat_comparison(results, country=country, category=category)


# ### Disability

# In[35]:


category = "Officially recognised disability"
results = count_diff(df, disability, country, category, y_n=True)


# In[36]:


plot_cat_comparison(results, country=country, category=category)


# ## United States

# In[37]:


country = 'United States'


# ### Age

# In[38]:


category = 'Age'
results = count_diff(df, age, country, category, order_index=age_order)
results


# In[39]:


plot_cat_comparison(results, country=country, category=category, order_index=age_order)


# ### Gender

# In[40]:


category = 'Gender'
results = count_diff(df, gender, country, category)
results


# In[41]:


plot_cat_comparison(results, country=country, category=category)


# ### Ethnicity

# In[42]:


category = 'Ethnicity'
results = count_diff(df, ethnicity, country, category, multi_choice=True)
results


# In[43]:


plot_cat_comparison(results, country=country, category=category)


# ### Hispano or Latino

# In[44]:


category = 'Ethnicity USA'
results = count_diff(df, ethn_us, country, category, y_n=True)
results


# In[45]:


plot_cat_comparison(results, country=country, category=category)


# ## Rest of the world

# In[46]:


country = 'World'


# ### Age

# In[47]:


category = 'Age'
results = count_diff(df, age, country, category, order_index=age_order)
results


# In[48]:


plot_cat_comparison(results, country=country, category=category, order_index=age_order)


# ### Gender

# In[49]:


category = 'Gender'
results = count_diff(df, gender, country, category)
results


# In[50]:


plot_cat_comparison(results, country=country, category=category)

