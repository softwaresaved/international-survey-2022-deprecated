#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span><ul class="toc-item"><li><span><a href="#Questions-in-this-section" data-toc-modified-id="Questions-in-this-section-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Questions in this section</a></span></li><li><span><a href="#Setting-up" data-toc-modified-id="Setting-up-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Setting up</a></span></li></ul></li><li><span><a href="#Open-source-and-DOI" data-toc-modified-id="Open-source-and-DOI-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Open source and DOI</a></span><ul class="toc-item"><li><span><a href="#Australia" data-toc-modified-id="Australia-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Australia</a></span><ul class="toc-item"><li><span><a href="#Open-source-use" data-toc-modified-id="Open-source-use-2.1.1"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>Open source use</a></span></li><li><span><a href="#Referencing-software" data-toc-modified-id="Referencing-software-2.1.2"><span class="toc-item-num">2.1.2&nbsp;&nbsp;</span>Referencing software</a></span></li><li><span><a href="#Use-of-Digital-Object-Identifier-(DOI)" data-toc-modified-id="Use-of-Digital-Object-Identifier-(DOI)-2.1.3"><span class="toc-item-num">2.1.3&nbsp;&nbsp;</span>Use of Digital Object Identifier (DOI)</a></span></li><li><span><a href="#Tools-used-for-DOI" data-toc-modified-id="Tools-used-for-DOI-2.1.4"><span class="toc-item-num">2.1.4&nbsp;&nbsp;</span>Tools used for DOI</a></span></li><li><span><a href="#ORCID" data-toc-modified-id="ORCID-2.1.5"><span class="toc-item-num">2.1.5&nbsp;&nbsp;</span>ORCID</a></span></li></ul></li><li><span><a href="#Germany" data-toc-modified-id="Germany-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Germany</a></span><ul class="toc-item"><li><span><a href="#Open-source-use" data-toc-modified-id="Open-source-use-2.2.1"><span class="toc-item-num">2.2.1&nbsp;&nbsp;</span>Open source use</a></span></li><li><span><a href="#Referencing-software" data-toc-modified-id="Referencing-software-2.2.2"><span class="toc-item-num">2.2.2&nbsp;&nbsp;</span>Referencing software</a></span></li><li><span><a href="#Use-of-Digital-Object-Identifier-(DOI)" data-toc-modified-id="Use-of-Digital-Object-Identifier-(DOI)-2.2.3"><span class="toc-item-num">2.2.3&nbsp;&nbsp;</span>Use of Digital Object Identifier (DOI)</a></span></li><li><span><a href="#Tools-used-for-DOI" data-toc-modified-id="Tools-used-for-DOI-2.2.4"><span class="toc-item-num">2.2.4&nbsp;&nbsp;</span>Tools used for DOI</a></span></li><li><span><a href="#ORCID" data-toc-modified-id="ORCID-2.2.5"><span class="toc-item-num">2.2.5&nbsp;&nbsp;</span>ORCID</a></span></li></ul></li><li><span><a href="#Netherlands" data-toc-modified-id="Netherlands-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Netherlands</a></span><ul class="toc-item"><li><span><a href="#Open-source-use" data-toc-modified-id="Open-source-use-2.3.1"><span class="toc-item-num">2.3.1&nbsp;&nbsp;</span>Open source use</a></span></li><li><span><a href="#Referencing-software" data-toc-modified-id="Referencing-software-2.3.2"><span class="toc-item-num">2.3.2&nbsp;&nbsp;</span>Referencing software</a></span></li><li><span><a href="#Use-of-Digital-Object-Identifier-(DOI)" data-toc-modified-id="Use-of-Digital-Object-Identifier-(DOI)-2.3.3"><span class="toc-item-num">2.3.3&nbsp;&nbsp;</span>Use of Digital Object Identifier (DOI)</a></span></li><li><span><a href="#Tools-used-for-DOI" data-toc-modified-id="Tools-used-for-DOI-2.3.4"><span class="toc-item-num">2.3.4&nbsp;&nbsp;</span>Tools used for DOI</a></span></li><li><span><a href="#ORCID" data-toc-modified-id="ORCID-2.3.5"><span class="toc-item-num">2.3.5&nbsp;&nbsp;</span>ORCID</a></span></li></ul></li><li><span><a href="#New-Zealand" data-toc-modified-id="New-Zealand-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>New Zealand</a></span><ul class="toc-item"><li><span><a href="#Open-source-use" data-toc-modified-id="Open-source-use-2.4.1"><span class="toc-item-num">2.4.1&nbsp;&nbsp;</span>Open source use</a></span></li><li><span><a href="#Referencing-software" data-toc-modified-id="Referencing-software-2.4.2"><span class="toc-item-num">2.4.2&nbsp;&nbsp;</span>Referencing software</a></span></li><li><span><a href="#Use-of-Digital-Object-Identifier-(DOI)" data-toc-modified-id="Use-of-Digital-Object-Identifier-(DOI)-2.4.3"><span class="toc-item-num">2.4.3&nbsp;&nbsp;</span>Use of Digital Object Identifier (DOI)</a></span></li><li><span><a href="#Tools-used-for-DOI" data-toc-modified-id="Tools-used-for-DOI-2.4.4"><span class="toc-item-num">2.4.4&nbsp;&nbsp;</span>Tools used for DOI</a></span></li><li><span><a href="#ORCID" data-toc-modified-id="ORCID-2.4.5"><span class="toc-item-num">2.4.5&nbsp;&nbsp;</span>ORCID</a></span></li></ul></li><li><span><a href="#South-Africa" data-toc-modified-id="South-Africa-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>South Africa</a></span><ul class="toc-item"><li><span><a href="#Open-source-use" data-toc-modified-id="Open-source-use-2.5.1"><span class="toc-item-num">2.5.1&nbsp;&nbsp;</span>Open source use</a></span></li><li><span><a href="#Referencing-software" data-toc-modified-id="Referencing-software-2.5.2"><span class="toc-item-num">2.5.2&nbsp;&nbsp;</span>Referencing software</a></span></li><li><span><a href="#Use-of-Digital-Object-Identifier-(DOI)" data-toc-modified-id="Use-of-Digital-Object-Identifier-(DOI)-2.5.3"><span class="toc-item-num">2.5.3&nbsp;&nbsp;</span>Use of Digital Object Identifier (DOI)</a></span></li><li><span><a href="#Tools-used-for-DOI" data-toc-modified-id="Tools-used-for-DOI-2.5.4"><span class="toc-item-num">2.5.4&nbsp;&nbsp;</span>Tools used for DOI</a></span></li><li><span><a href="#ORCID" data-toc-modified-id="ORCID-2.5.5"><span class="toc-item-num">2.5.5&nbsp;&nbsp;</span>ORCID</a></span></li></ul></li><li><span><a href="#United-Kingdom" data-toc-modified-id="United-Kingdom-2.6"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>United Kingdom</a></span><ul class="toc-item"><li><span><a href="#Open-source-use" data-toc-modified-id="Open-source-use-2.6.1"><span class="toc-item-num">2.6.1&nbsp;&nbsp;</span>Open source use</a></span></li><li><span><a href="#Referencing-software" data-toc-modified-id="Referencing-software-2.6.2"><span class="toc-item-num">2.6.2&nbsp;&nbsp;</span>Referencing software</a></span></li><li><span><a href="#Use-of-Digital-Object-Identifier-(DOI)" data-toc-modified-id="Use-of-Digital-Object-Identifier-(DOI)-2.6.3"><span class="toc-item-num">2.6.3&nbsp;&nbsp;</span>Use of Digital Object Identifier (DOI)</a></span></li><li><span><a href="#Tools-used-for-DOI" data-toc-modified-id="Tools-used-for-DOI-2.6.4"><span class="toc-item-num">2.6.4&nbsp;&nbsp;</span>Tools used for DOI</a></span></li><li><span><a href="#ORCID" data-toc-modified-id="ORCID-2.6.5"><span class="toc-item-num">2.6.5&nbsp;&nbsp;</span>ORCID</a></span></li></ul></li><li><span><a href="#United-States" data-toc-modified-id="United-States-2.7"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>United States</a></span><ul class="toc-item"><li><span><a href="#Open-source-use" data-toc-modified-id="Open-source-use-2.7.1"><span class="toc-item-num">2.7.1&nbsp;&nbsp;</span>Open source use</a></span></li><li><span><a href="#Referencing-software" data-toc-modified-id="Referencing-software-2.7.2"><span class="toc-item-num">2.7.2&nbsp;&nbsp;</span>Referencing software</a></span></li><li><span><a href="#Use-of-Digital-Object-Identifier-(DOI)" data-toc-modified-id="Use-of-Digital-Object-Identifier-(DOI)-2.7.3"><span class="toc-item-num">2.7.3&nbsp;&nbsp;</span>Use of Digital Object Identifier (DOI)</a></span></li><li><span><a href="#Tools-used-for-DOI" data-toc-modified-id="Tools-used-for-DOI-2.7.4"><span class="toc-item-num">2.7.4&nbsp;&nbsp;</span>Tools used for DOI</a></span></li><li><span><a href="#ORCID" data-toc-modified-id="ORCID-2.7.5"><span class="toc-item-num">2.7.5&nbsp;&nbsp;</span>ORCID</a></span></li></ul></li><li><span><a href="#Rest-of-the-world" data-toc-modified-id="Rest-of-the-world-2.8"><span class="toc-item-num">2.8&nbsp;&nbsp;</span>Rest of the world</a></span><ul class="toc-item"><li><span><a href="#Open-source-use" data-toc-modified-id="Open-source-use-2.8.1"><span class="toc-item-num">2.8.1&nbsp;&nbsp;</span>Open source use</a></span></li><li><span><a href="#Referencing-software" data-toc-modified-id="Referencing-software-2.8.2"><span class="toc-item-num">2.8.2&nbsp;&nbsp;</span>Referencing software</a></span></li><li><span><a href="#Use-of-Digital-Object-Identifier-(DOI)" data-toc-modified-id="Use-of-Digital-Object-Identifier-(DOI)-2.8.3"><span class="toc-item-num">2.8.3&nbsp;&nbsp;</span>Use of Digital Object Identifier (DOI)</a></span></li><li><span><a href="#Tools-used-for-DOI" data-toc-modified-id="Tools-used-for-DOI-2.8.4"><span class="toc-item-num">2.8.4&nbsp;&nbsp;</span>Tools used for DOI</a></span></li><li><span><a href="#ORCID" data-toc-modified-id="ORCID-2.8.5"><span class="toc-item-num">2.8.5&nbsp;&nbsp;</span>ORCID</a></span></li></ul></li></ul></li></ul></div>

# # Introduction

# RSEs is an hybrid role between a researcher and a software developer. We investigated both of these aspects concerning publication and dissemination of their work, one on the traditional aspect of it (publications and conference) and, as developed here, on the more software aspect (open source and DOI).
# 
# We asked the participants if they have ever released their work under open source licence but also questions about the referencing system. We asked them how often they reference software, and if they use DOI for it, and which tools for it. 
# 
# We also asked them if they have an ORCID ID, a system that gives a unique reference ID for the researcher. 

# ## Questions in this section
# 
# * `How often do you use an open-source licence for your software?`: likert scale
# * `How often do you reference software directly or the papers describing the software?`: likert scale
# * `How often do you associate your software with a Digital Object Identifier (DOI)?`: likert scale 
# * `Which tools do you use to mint a DOI (e.g. local library, Zenodo)?`: free text
# * `Do you have an ORCID ID?`: yes-no

# ## Setting up

# In[1]:


get_ipython().run_cell_magic('capture', ' ', '# Import notebook containing the imports the functions and the dataset\n%run "./0. Imports and functions.ipynb"\n\n# Import notebook containing sampled dataset\n%run "./1. Overview and sampling.ipynb"')


# # Open source and DOI

# In[2]:


# Open source and DOI
open_use = ['open1can. How often do you use an open-source licence for your software?']

order_open = ['1 (None at all)', '2', '3', '4', '5', '6', '7', '8', '9', '10 (All the time)']

ref_soft = ['open2de. How often do you reference software directly or the papers describing the software?']

doi = ['open3can. How often do you associate your software with a Digital Object Identifier (DOI)?']

doi_tools = ['open3de. Which tools do you use to mint a DOI (e.g. local library, Zenodo)?']

orcid = ['open1de. Do you have an ORCID ID?']


# ## Australia

# In[3]:


country = 'Australia'


# ### Open source use

# In[4]:


category = 'Open source use'
results = count_diff(df, open_use, country, category, order_index=order_open)
results


# In[5]:


plot_cat_comparison(results, country=country, category=category, order_index=order_open)


# ### Referencing software

# In[6]:


category = 'Citation of software'
results = count_diff(df, ref_soft, country, category, order_index=order_open)
results


# In[7]:


plot_cat_comparison(results, country=country, category=category, order_index=order_open)


# ### Use of Digital Object Identifier (DOI)

# In[8]:


category = 'Use of Digital Object Identifier'
results = count_diff(df, doi, country, category, order_index=order_open)
results


# In[9]:


plot_cat_comparison(results, country=country, category=category, order_index=order_open)


# ### Tools used for DOI

# In[10]:


category = 'Which tool is used for Digital Object Identifier'
plot_wordcloud(df, doi_tools, country, category)


# ### ORCID

# In[11]:


category = 'Using ORCID'
results = count_diff(df, orcid, country, category, y_n=True)
results


# In[12]:


plot_cat_comparison(results, country=country, category=category)


# ## Germany

# In[13]:


country = 'Germany'


# ### Open source use

# In[14]:


category = 'Open source use'
results = count_diff(df, open_use, country, category, order_index=order_open)
results


# In[15]:


plot_cat_comparison(results, country=country, category=category, order_index=order_open)


# ### Referencing software

# In[16]:


category = 'Citation of software'
results = count_diff(df, ref_soft, country, category, order_index=order_open)
results


# In[17]:


plot_cat_comparison(results, country=country, category=category, order_index=order_open)


# ### Use of Digital Object Identifier (DOI)

# In[18]:


category = 'Use of Digital Object Identifier'
results = count_diff(df, doi, country, category, order_index=order_open)
results


# In[19]:


plot_cat_comparison(results, country=country, category=category, order_index=order_open)


# ### Tools used for DOI

# In[20]:


category = 'Which tool is used for Digital Object Identifier'
plot_wordcloud(df, doi_tools, country, category)


# ### ORCID

# In[21]:


category = 'Using ORCID'
results = count_diff(df, orcid, country, category, y_n=True)
results


# In[22]:


plot_cat_comparison(results, country=country, category=category)


# ## Netherlands

# In[23]:


country = 'Netherlands'


# ### Open source use

# In[24]:


category = 'Open source use'
results = count_diff(df, open_use, country, category, order_index=order_open)
results


# In[25]:


plot_cat_comparison(results, country=country, category=category, order_index=order_open)


# ### Referencing software

# In[26]:


category = 'Citation of software'
results = count_diff(df, ref_soft, country, category, order_index=order_open)
results


# In[27]:


plot_cat_comparison(results, country=country, category=category, order_index=order_open)


# ### Use of Digital Object Identifier (DOI)

# In[28]:


category = 'Use of Digital Object Identifier'
results = count_diff(df, doi, country, category, order_index=order_open)
results


# In[29]:


plot_cat_comparison(results, country=country, category=category, order_index=order_open)


# ### Tools used for DOI

# In[30]:


category = 'Which tool is used for Digital Object Identifier'
plot_wordcloud(df, doi_tools, country, category)


# ### ORCID

# In[31]:


category = 'Using ORCID'
results = count_diff(df, orcid, country, category, y_n=True)
results


# In[32]:


plot_cat_comparison(results, country=country, category=category)


# ## New Zealand

# In[33]:


country = 'New Zealand'


# ### Open source use

# In[34]:


category = 'Open source use'
results = count_diff(df, open_use, country, category, order_index=order_open)
results


# In[35]:


plot_cat_comparison(results, country=country, category=category, order_index=order_open)


# ### Referencing software

# In[36]:


category = 'Citation of software'
results = count_diff(df, ref_soft, country, category, order_index=order_open)
results


# In[37]:


plot_cat_comparison(results, country=country, category=category, order_index=order_open)


# ### Use of Digital Object Identifier (DOI)

# In[38]:


category = 'Use of Digital Object Identifier'
results = count_diff(df, doi, country, category, order_index=order_open)
results


# In[39]:


plot_cat_comparison(results, country=country, category=category, order_index=order_open)


# ### Tools used for DOI

# In[40]:


category = 'Which tool is used for Digital Object Identifier'
plot_wordcloud(df, doi_tools, country, category)


# ### ORCID

# In[41]:


category = 'Using ORCID'
results = count_diff(df, orcid, country, category, y_n=True)
results


# In[42]:


plot_cat_comparison(results, country=country, category=category)


# ## South Africa

# In[43]:


country = 'South Africa'


# ### Open source use

# In[44]:


category = 'Open source use'
results = count_diff(df, open_use, country, category, order_index=order_open)
results


# In[45]:


plot_cat_comparison(results, country=country, category=category, order_index=order_open)


# ### Referencing software

# In[46]:


category = 'Citation of software'
results = count_diff(df, ref_soft, country, category, order_index=order_open)
results


# In[47]:


plot_cat_comparison(results, country=country, category=category, order_index=order_open)


# ### Use of Digital Object Identifier (DOI)

# In[48]:


category = 'Use of Digital Object Identifier'
results = count_diff(df, doi, country, category, order_index=order_open)
results


# In[49]:


plot_cat_comparison(results, country=country, category=category, order_index=order_open)


# ### Tools used for DOI

# In[50]:


category = 'Which tool is used for Digital Object Identifier'
plot_wordcloud(df, doi_tools, country, category)


# ### ORCID

# In[51]:


category = 'Using ORCID'
results = count_diff(df, orcid, country, category, y_n=True)
results


# In[52]:


plot_cat_comparison(results, country=country, category=category)


# ## United Kingdom

# Good news for the open source use, 43% of the participants claims they release their software under open source license all the time. None of them reported to never use it. These results can partially be compared with last year results. Last year we first asked them if they release software under open source license and only 68% of them say the do (but among them 48% are doing it all the time and 43% Very often). It can be seen as a dramatic change on the popularity of open source license. 
# 
# Referencing software is an important issue for academic and RSE in particular. From a scale from 1 (not at all) to 10 (all the time), more than 95% of the participants declared 5 or higher.
# 
# The use of Digital Object Identifier is relatively spread and there is no clear tendency of using or not while the ORCID is much more well-known and used by the participants, 73% of them reported to have and use one. 

# In[53]:


country = 'United Kingdom'


# ### Open source use

# In[54]:


category = 'Open source use'
results = count_diff(df, open_use, country, category, order_index=order_open)
results


# In[55]:


plot_cat_comparison(results, country=country, category=category, order_index=order_open)


# ### Referencing software

# In[56]:


category = 'Citation of software'
results = count_diff(df, ref_soft, country, category, order_index=order_open)
results


# In[57]:


plot_cat_comparison(results, country=country, category=category, order_index=order_open)


# ### Use of Digital Object Identifier (DOI)

# In[58]:


category = 'Use of Digital Object Identifier'
results = count_diff(df, doi, country, category, order_index=order_open)
results


# In[59]:


plot_cat_comparison(results, country=country, category=category, order_index=order_open)


# ### Tools used for DOI

# In[60]:


category = 'Which tool is used for Digital Object Identifier'
plot_wordcloud(df, doi_tools, country, category)


# ### ORCID

# In[61]:


category = 'Using ORCID'
results = count_diff(df, orcid, country, category, y_n=True)
results


# In[62]:


plot_cat_comparison(results, country=country, category=category)


# ## United States

# In[63]:


country = 'United States'


# ### Open source use

# In[64]:


category = 'Open source use'
results = count_diff(df, open_use, country, category, order_index=order_open)
results


# In[65]:


plot_cat_comparison(results, country=country, category=category, order_index=order_open)


# ### Referencing software

# In[66]:


category = 'Citation of software'
results = count_diff(df, ref_soft, country, category, order_index=order_open)
results


# In[67]:


plot_cat_comparison(results, country=country, category=category, order_index=order_open)


# ### Use of Digital Object Identifier (DOI)

# In[68]:


category = 'Use of Digital Object Identifier'
results = count_diff(df, doi, country, category, order_index=order_open)
results


# In[69]:


plot_cat_comparison(results, country=country, category=category, order_index=order_open)


# ### Tools used for DOI

# In[70]:


category = 'Which tool is used for Digital Object Identifier'
plot_wordcloud(df, doi_tools, country, category)


# ### ORCID

# In[71]:


category = 'Using ORCID'
results = count_diff(df, orcid, country, category, y_n=True)
results


# In[72]:


plot_cat_comparison(results, country=country, category=category)


# ## Rest of the world

# In[73]:


country = 'World'


# ### Open source use

# In[74]:


category = 'Open source use'
results = count_diff(df, open_use, country, category, order_index=order_open)
results


# In[75]:


plot_cat_comparison(results, country=country, category=category, order_index=order_open)


# ### Referencing software

# In[76]:


category = 'Citation of software'
results = count_diff(df, ref_soft, country, category, order_index=order_open)
results


# In[77]:


plot_cat_comparison(results, country=country, category=category, order_index=order_open)


# ### Use of Digital Object Identifier (DOI)

# In[78]:


category = 'Use of Digital Object Identifier'
results = count_diff(df, doi, country, category, order_index=order_open)
results


# In[79]:


plot_cat_comparison(results, country=country, category=category, order_index=order_open)


# ### Tools used for DOI

# In[80]:


category = 'Which tool is used for Digital Object Identifier'
plot_wordcloud(df, doi_tools, country, category)


# ### ORCID

# In[81]:


category = 'Using ORCID'
results = count_diff(df, orcid, country, category, y_n=True)
results


# In[82]:


plot_cat_comparison(results, country=country, category=category)

