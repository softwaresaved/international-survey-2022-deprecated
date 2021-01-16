#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span><ul class="toc-item"><li><span><a href="#Questions-in-this-section" data-toc-modified-id="Questions-in-this-section-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Questions in this section</a></span></li><li><span><a href="#Setting-up" data-toc-modified-id="Setting-up-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Setting up</a></span></li></ul></li><li><span><a href="#Tools-and-programing-languages" data-toc-modified-id="Tools-and-programing-languages-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Tools and programing languages</a></span><ul class="toc-item"><li><span><a href="#Australia" data-toc-modified-id="Australia-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Australia</a></span><ul class="toc-item"><li><span><a href="#Programing-languages" data-toc-modified-id="Programing-languages-2.1.1"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>Programing languages</a></span></li><li><span><a href="#Operating-System" data-toc-modified-id="Operating-System-2.1.2"><span class="toc-item-num">2.1.2&nbsp;&nbsp;</span>Operating System</a></span></li></ul></li><li><span><a href="#Germany" data-toc-modified-id="Germany-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Germany</a></span><ul class="toc-item"><li><span><a href="#Programing-languages" data-toc-modified-id="Programing-languages-2.2.1"><span class="toc-item-num">2.2.1&nbsp;&nbsp;</span>Programing languages</a></span></li><li><span><a href="#Operating-System" data-toc-modified-id="Operating-System-2.2.2"><span class="toc-item-num">2.2.2&nbsp;&nbsp;</span>Operating System</a></span></li></ul></li><li><span><a href="#Netherlands" data-toc-modified-id="Netherlands-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Netherlands</a></span><ul class="toc-item"><li><span><a href="#Programing-languages" data-toc-modified-id="Programing-languages-2.3.1"><span class="toc-item-num">2.3.1&nbsp;&nbsp;</span>Programing languages</a></span></li><li><span><a href="#Operating-System" data-toc-modified-id="Operating-System-2.3.2"><span class="toc-item-num">2.3.2&nbsp;&nbsp;</span>Operating System</a></span></li></ul></li><li><span><a href="#New-Zealand" data-toc-modified-id="New-Zealand-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>New Zealand</a></span><ul class="toc-item"><li><span><a href="#Programing-languages" data-toc-modified-id="Programing-languages-2.4.1"><span class="toc-item-num">2.4.1&nbsp;&nbsp;</span>Programing languages</a></span></li><li><span><a href="#Operating-System" data-toc-modified-id="Operating-System-2.4.2"><span class="toc-item-num">2.4.2&nbsp;&nbsp;</span>Operating System</a></span></li></ul></li><li><span><a href="#South-Africa" data-toc-modified-id="South-Africa-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>South Africa</a></span><ul class="toc-item"><li><span><a href="#Programing-languages" data-toc-modified-id="Programing-languages-2.5.1"><span class="toc-item-num">2.5.1&nbsp;&nbsp;</span>Programing languages</a></span></li><li><span><a href="#Operating-System" data-toc-modified-id="Operating-System-2.5.2"><span class="toc-item-num">2.5.2&nbsp;&nbsp;</span>Operating System</a></span></li></ul></li><li><span><a href="#United-Kingdom" data-toc-modified-id="United-Kingdom-2.6"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>United Kingdom</a></span><ul class="toc-item"><li><span><a href="#Programing-languages" data-toc-modified-id="Programing-languages-2.6.1"><span class="toc-item-num">2.6.1&nbsp;&nbsp;</span>Programing languages</a></span></li><li><span><a href="#Operating-System" data-toc-modified-id="Operating-System-2.6.2"><span class="toc-item-num">2.6.2&nbsp;&nbsp;</span>Operating System</a></span></li></ul></li><li><span><a href="#United-States" data-toc-modified-id="United-States-2.7"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>United States</a></span><ul class="toc-item"><li><span><a href="#Programing-languages" data-toc-modified-id="Programing-languages-2.7.1"><span class="toc-item-num">2.7.1&nbsp;&nbsp;</span>Programing languages</a></span></li><li><span><a href="#Operating-System" data-toc-modified-id="Operating-System-2.7.2"><span class="toc-item-num">2.7.2&nbsp;&nbsp;</span>Operating System</a></span></li></ul></li><li><span><a href="#Rest-of-the-world" data-toc-modified-id="Rest-of-the-world-2.8"><span class="toc-item-num">2.8&nbsp;&nbsp;</span>Rest of the world</a></span><ul class="toc-item"><li><span><a href="#Programing-languages" data-toc-modified-id="Programing-languages-2.8.1"><span class="toc-item-num">2.8.1&nbsp;&nbsp;</span>Programing languages</a></span></li><li><span><a href="#Operating-System" data-toc-modified-id="Operating-System-2.8.2"><span class="toc-item-num">2.8.2&nbsp;&nbsp;</span>Operating System</a></span></li></ul></li></ul></li></ul></div>

# # Introduction

# On technical details we wanted to know which of the programming languages are mostly used by the RSEs. We give them a multi-choice list inspired by the [results](https://insights.stackoverflow.com/survey/2017#most-popular-technologies) published by Stackoverflow.
# 
# We also wanted to know which is their Operating System for working.

# ## Questions in this section
# 
# * Which operating system do you primarily use for development?`: one choice
# * `What programming languages do you use at work? Please select all that apply.`: multiple choice

# ## Setting up

# In[1]:


get_ipython().run_cell_magic('capture', ' ', '# Import notebook containing the imports the functions and the dataset\n%run "./0. Imports and functions.ipynb"\n\n# Import notebook containing sampled dataset\n%run "./1. Overview and sampling.ipynb"')


# # Tools and programing languages

# In[2]:


# Tools and languages
os = ['tool2. Which operating system do you primarily use for development?']

prog_lang = [x for x in df.columns if x[:8] == 'tool4can']


# ## Australia

# In[3]:


country = 'Australia'


# ### Programing languages

# In[4]:


category = 'Programing language'
results = count_diff(df, prog_lang, country, category, multi_choice=True)
results


# In[5]:


plot_cat_comparison(results, country=country, category=category)


# ### Operating System

# In[6]:


category = 'Operating systen'
results = count_diff(df, os, country=country, category=category)
results


# In[7]:


plot_cat_comparison(results, country=country, category=category)


# ## Germany

# In[8]:


country = 'Germany'


# ### Programing languages

# In[9]:


category = 'Programing language'
results = count_diff(df, prog_lang, country, category, multi_choice=True)
results


# In[10]:


plot_cat_comparison(results, country=country, category=category)


# ### Operating System

# In[11]:


category = 'Operating systen'
results = count_diff(df, os, country=country, category=category)
results


# In[12]:


plot_cat_comparison(results, country=country, category=category)


# ## Netherlands

# In[13]:


country = 'Netherlands'


# ### Programing languages

# In[14]:


category = 'Programing language'
results = count_diff(df, prog_lang, country, category, multi_choice=True)
results


# In[15]:


plot_cat_comparison(results, country=country, category=category)


# ### Operating System

# In[16]:


category = 'Operating systen'
results = count_diff(df, os, country=country, category=category)
results


# In[17]:


plot_cat_comparison(results, country=country, category=category)


# ## New Zealand

# In[18]:


country = 'New Zealand'


# ### Programing languages

# In[19]:


category = 'Programing language'
results = count_diff(df, prog_lang, country, category, multi_choice=True)
results


# In[20]:


plot_cat_comparison(results, country=country, category=category)


# ### Operating System

# In[21]:


category = 'Operating systen'
results = count_diff(df, os, country=country, category=category)
results


# In[22]:


plot_cat_comparison(results, country=country, category=category)


# ## South Africa

# In[23]:


country = 'South Africa'


# ### Programing languages

# In[24]:


category = 'Programing language'
results = count_diff(df, prog_lang, country, category, multi_choice=True)
results


# In[25]:


plot_cat_comparison(results, country=country, category=category)


# ### Operating System

# In[26]:


category = 'Operating systen'
results = count_diff(df, os, country=country, category=category)
results


# In[27]:


plot_cat_comparison(results, country=country, category=category)


# ## United Kingdom

# About programing language, Python is clearly the most used language with 77%. It is even more than last year with an increase of 1%. C++ follows with 37% and C with 35%. R, while being in 4th position, get an increase of 6%, and he is used by 29% of the participants. 
# The biggest negative difference is form Mathlab, decreasing of more than 7% and being used by only 17% of the participants. 
# 
# On Operating Systems, GNU/Linux is still ahead with 61%, followed by OS X and Windows (respectively 19 and 18%).

# In[28]:


country = 'United Kingdom'


# ### Programing languages

# In[29]:


category = 'Programing language'
results = count_diff(df, prog_lang, country, category, multi_choice=True)
results


# In[30]:


plot_cat_comparison(results, country=country, category=category)


# ### Operating System

# In[31]:


category = 'Operating systen'
results = count_diff(df, os, country=country, category=category)
results


# In[32]:


plot_cat_comparison(results, country=country, category=category)


# ## United States

# In[33]:


country = 'United States'


# ### Programing languages

# In[34]:


category = 'Programing language'
results = count_diff(df, prog_lang, country, category, multi_choice=True)
results


# In[35]:


plot_cat_comparison(results, country=country, category=category)


# ### Operating System

# In[36]:


category = 'Operating systen'
results = count_diff(df, os, country=country, category=category)
results


# In[37]:


plot_cat_comparison(results, country=country, category=category)


# ## Rest of the world

# In[38]:


country = 'World'


# ### Programing languages

# In[39]:


category = 'Programing language'
results = count_diff(df, prog_lang, country, category, multi_choice=True)
results


# In[40]:


plot_cat_comparison(results, country=country, category=category)


# ### Operating System

# In[41]:


category = 'Operating systen'
results = count_diff(df, os, country=country, category=category)
results


# In[42]:


plot_cat_comparison(results, country=country, category=category)

