#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span><ul class="toc-item"><li><span><a href="#Setting-up" data-toc-modified-id="Setting-up-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Setting up</a></span></li></ul></li><li><span><a href="#Good-practices" data-toc-modified-id="Good-practices-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Good practices</a></span><ul class="toc-item"><li><span><a href="#Australia" data-toc-modified-id="Australia-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Australia</a></span><ul class="toc-item"><li><span><a href="#Bus-Factor" data-toc-modified-id="Bus-Factor-2.1.1"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>Bus Factor</a></span></li><li><span><a href="#Transition-plan" data-toc-modified-id="Transition-plan-2.1.2"><span class="toc-item-num">2.1.2&nbsp;&nbsp;</span>Transition plan</a></span></li><li><span><a href="#Version-control" data-toc-modified-id="Version-control-2.1.3"><span class="toc-item-num">2.1.3&nbsp;&nbsp;</span>Version control</a></span></li><li><span><a href="#Testing" data-toc-modified-id="Testing-2.1.4"><span class="toc-item-num">2.1.4&nbsp;&nbsp;</span>Testing</a></span></li><li><span><a href="#Repository" data-toc-modified-id="Repository-2.1.5"><span class="toc-item-num">2.1.5&nbsp;&nbsp;</span>Repository</a></span></li></ul></li><li><span><a href="#Germany" data-toc-modified-id="Germany-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Germany</a></span><ul class="toc-item"><li><span><a href="#Bus-Factor" data-toc-modified-id="Bus-Factor-2.2.1"><span class="toc-item-num">2.2.1&nbsp;&nbsp;</span>Bus Factor</a></span></li><li><span><a href="#Transition-plan" data-toc-modified-id="Transition-plan-2.2.2"><span class="toc-item-num">2.2.2&nbsp;&nbsp;</span>Transition plan</a></span></li><li><span><a href="#Version-control" data-toc-modified-id="Version-control-2.2.3"><span class="toc-item-num">2.2.3&nbsp;&nbsp;</span>Version control</a></span></li><li><span><a href="#Testing" data-toc-modified-id="Testing-2.2.4"><span class="toc-item-num">2.2.4&nbsp;&nbsp;</span>Testing</a></span></li><li><span><a href="#Repository" data-toc-modified-id="Repository-2.2.5"><span class="toc-item-num">2.2.5&nbsp;&nbsp;</span>Repository</a></span></li></ul></li><li><span><a href="#Netherlands" data-toc-modified-id="Netherlands-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Netherlands</a></span><ul class="toc-item"><li><span><a href="#Bus-Factor" data-toc-modified-id="Bus-Factor-2.3.1"><span class="toc-item-num">2.3.1&nbsp;&nbsp;</span>Bus Factor</a></span></li><li><span><a href="#Transition-plan" data-toc-modified-id="Transition-plan-2.3.2"><span class="toc-item-num">2.3.2&nbsp;&nbsp;</span>Transition plan</a></span></li><li><span><a href="#Version-control" data-toc-modified-id="Version-control-2.3.3"><span class="toc-item-num">2.3.3&nbsp;&nbsp;</span>Version control</a></span></li><li><span><a href="#Testing" data-toc-modified-id="Testing-2.3.4"><span class="toc-item-num">2.3.4&nbsp;&nbsp;</span>Testing</a></span></li><li><span><a href="#Repository" data-toc-modified-id="Repository-2.3.5"><span class="toc-item-num">2.3.5&nbsp;&nbsp;</span>Repository</a></span></li></ul></li><li><span><a href="#New-Zealand" data-toc-modified-id="New-Zealand-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>New Zealand</a></span><ul class="toc-item"><li><span><a href="#Bus-Factor" data-toc-modified-id="Bus-Factor-2.4.1"><span class="toc-item-num">2.4.1&nbsp;&nbsp;</span>Bus Factor</a></span></li><li><span><a href="#Transition-plan" data-toc-modified-id="Transition-plan-2.4.2"><span class="toc-item-num">2.4.2&nbsp;&nbsp;</span>Transition plan</a></span></li><li><span><a href="#Version-control" data-toc-modified-id="Version-control-2.4.3"><span class="toc-item-num">2.4.3&nbsp;&nbsp;</span>Version control</a></span></li><li><span><a href="#Testing" data-toc-modified-id="Testing-2.4.4"><span class="toc-item-num">2.4.4&nbsp;&nbsp;</span>Testing</a></span></li><li><span><a href="#Repository" data-toc-modified-id="Repository-2.4.5"><span class="toc-item-num">2.4.5&nbsp;&nbsp;</span>Repository</a></span></li></ul></li><li><span><a href="#South-Africa" data-toc-modified-id="South-Africa-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>South Africa</a></span><ul class="toc-item"><li><span><a href="#Bus-Factor" data-toc-modified-id="Bus-Factor-2.5.1"><span class="toc-item-num">2.5.1&nbsp;&nbsp;</span>Bus Factor</a></span></li><li><span><a href="#Transition-plan" data-toc-modified-id="Transition-plan-2.5.2"><span class="toc-item-num">2.5.2&nbsp;&nbsp;</span>Transition plan</a></span></li><li><span><a href="#Version-control" data-toc-modified-id="Version-control-2.5.3"><span class="toc-item-num">2.5.3&nbsp;&nbsp;</span>Version control</a></span></li><li><span><a href="#Testing" data-toc-modified-id="Testing-2.5.4"><span class="toc-item-num">2.5.4&nbsp;&nbsp;</span>Testing</a></span></li><li><span><a href="#Repository" data-toc-modified-id="Repository-2.5.5"><span class="toc-item-num">2.5.5&nbsp;&nbsp;</span>Repository</a></span></li></ul></li><li><span><a href="#United-Kingdom" data-toc-modified-id="United-Kingdom-2.6"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>United Kingdom</a></span><ul class="toc-item"><li><span><a href="#Bus-Factor" data-toc-modified-id="Bus-Factor-2.6.1"><span class="toc-item-num">2.6.1&nbsp;&nbsp;</span>Bus Factor</a></span></li><li><span><a href="#Transition-plan" data-toc-modified-id="Transition-plan-2.6.2"><span class="toc-item-num">2.6.2&nbsp;&nbsp;</span>Transition plan</a></span></li><li><span><a href="#Version-control" data-toc-modified-id="Version-control-2.6.3"><span class="toc-item-num">2.6.3&nbsp;&nbsp;</span>Version control</a></span></li><li><span><a href="#Testing" data-toc-modified-id="Testing-2.6.4"><span class="toc-item-num">2.6.4&nbsp;&nbsp;</span>Testing</a></span></li><li><span><a href="#Repository" data-toc-modified-id="Repository-2.6.5"><span class="toc-item-num">2.6.5&nbsp;&nbsp;</span>Repository</a></span></li></ul></li><li><span><a href="#United-States" data-toc-modified-id="United-States-2.7"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>United States</a></span><ul class="toc-item"><li><span><a href="#Bus-Factor" data-toc-modified-id="Bus-Factor-2.7.1"><span class="toc-item-num">2.7.1&nbsp;&nbsp;</span>Bus Factor</a></span></li><li><span><a href="#Transition-plan" data-toc-modified-id="Transition-plan-2.7.2"><span class="toc-item-num">2.7.2&nbsp;&nbsp;</span>Transition plan</a></span></li><li><span><a href="#Version-control" data-toc-modified-id="Version-control-2.7.3"><span class="toc-item-num">2.7.3&nbsp;&nbsp;</span>Version control</a></span></li><li><span><a href="#Testing" data-toc-modified-id="Testing-2.7.4"><span class="toc-item-num">2.7.4&nbsp;&nbsp;</span>Testing</a></span></li><li><span><a href="#Repository" data-toc-modified-id="Repository-2.7.5"><span class="toc-item-num">2.7.5&nbsp;&nbsp;</span>Repository</a></span></li></ul></li><li><span><a href="#Rest-of-the-world" data-toc-modified-id="Rest-of-the-world-2.8"><span class="toc-item-num">2.8&nbsp;&nbsp;</span>Rest of the world</a></span><ul class="toc-item"><li><span><a href="#Bus-Factor" data-toc-modified-id="Bus-Factor-2.8.1"><span class="toc-item-num">2.8.1&nbsp;&nbsp;</span>Bus Factor</a></span></li><li><span><a href="#Transition-plan" data-toc-modified-id="Transition-plan-2.8.2"><span class="toc-item-num">2.8.2&nbsp;&nbsp;</span>Transition plan</a></span></li><li><span><a href="#Version-control" data-toc-modified-id="Version-control-2.8.3"><span class="toc-item-num">2.8.3&nbsp;&nbsp;</span>Version control</a></span></li><li><span><a href="#Testing" data-toc-modified-id="Testing-2.8.4"><span class="toc-item-num">2.8.4&nbsp;&nbsp;</span>Testing</a></span></li><li><span><a href="#Repository" data-toc-modified-id="Repository-2.8.5"><span class="toc-item-num">2.8.5&nbsp;&nbsp;</span>Repository</a></span></li></ul></li></ul></li></ul></div>

# # Introduction

# This section comprises sections that focus on the technical and development aspects of the RSEs' work. They aim to understand good practices in developing software.
# 
# We chose two broad measures to provide an insight into sustainability: the **bus factor** and **technical hand over planning**. 
# * The bus factor is a measure of the number of developers who understand a specific software project and could, with only a cursory review of the project, maintain or extend the code. A project with a bus factor of 1 is completely reliant on only one developer. If this developer finds new employment, becomes ill or is hit by the titular bus, then the project will fail. A high bus factor provides some confidence that the project can be sustained even if a developer leaves. 
# 
# * A technical hand over plan is used to introduce a new developer to a software project. These plans cover basic information, such as the license and location of the software, a repository, a description of the software architecture, a summary of development plans and any other information that a new developer would need to understand the software. A project that has written (and maintained) a technical hand over plan can withstand the departure of a developer, even a key developer, significantly better than one without such a plan.
# 
# Developing software requires a set of good practices to ensure the quality of the subsequent analysis as well as the robustness of the developed software, to name a few of important aspects. We wanted to see if the implementation of some simple but essential good practices were a reality beside the bus factor and technical hand over planning. 
# 
# When developing software, **version control** and **testing** can be seen as tool to enhance the quality of the developed software, especially considering the importance of code review and sharing in public funded places such as academia. 
# 
# For testing, we asked the participants to choose any of the following testing methods:
# * Test engineers conduct testing
# * Developers conduct testing
# * Users conduct testing
# * No formal testing
# 
# Obviously, the *test engineers conduct testing* is the most robust testing method but may not be possible in smaller projects while no formal testing should not occur in any ideal scenario, regardless of the size of the project. 
# 
# We also asked the participants if they use any version control tools through a list of choice. And finaly we asked them which repository they are currently using for their most important project. 

# ## Setting up

# In[1]:


get_ipython().run_cell_magic('capture', ' ', '# Import notebook containing the imports the functions and the dataset\n%run "./0. Imports and functions.ipynb"\n\n# Import notebook containing sampled dataset\n%run "./1. Overview and sampling.ipynb"')


# # Good practices

# In[2]:


# Good practices
bus_factor = ['stability1. What is the bus factor of your most important software project? (The bus factor designates the minimal number of developers that have to be hit by a bus (or quit) before a project is incapacitated)']

transition_plan = ['stability2. Do the projects you work on typically have a plan to cope with developers leaving the group?']

version_control = [x for x in df.columns if x[:8] == 'proj5zaf']

testing = [x for x in df.columns if x[:8] == 'proj4can']

order_testing = ['No formal testing', 'No formal testing but users provide feedback', 'The developers do their own testing', 'Test engineers conduct testing']

repo_tool = ['proj6zaf. Which online collaboration tools and open repositories do you use for software development?']


# In[3]:


df[testing]


# ## Australia

# In[4]:


country = 'Australia'


# ### Bus Factor

# In[5]:


category = 'Bus Factor'
results = count_diff(df, bus_factor, country, category, order_index=True)
results


# In[6]:


plot_cat_comparison(results, country=country, category=category, order_index=True)


# ### Transition plan

# In[7]:


category = 'Presence of a transition plan'
results = count_diff(df, transition_plan, country, category, y_n=True)
results


# In[8]:


plot_cat_comparison(results, country=country, category=category)


# ### Version control

# In[9]:


category = 'Use of version control'
results = count_diff(df, version_control, country, category, multi_choice=True)
results


# In[10]:


plot_cat_comparison(results, country=country, category=category)


# ### Testing

# In[11]:


category = 'Testing strategies'
results = count_diff(df, testing, country, category, multi_choice=True, order_index=order_testing)
results


# In[12]:


plot_cat_comparison(results, country=country, category=category, order_index=order_testing)


# ### Repository 

# In[13]:


category = 'Repository'
plot_wordcloud(df, repo_tool, country, category)


# ## Germany

# In[14]:


country = 'Germany'


# ### Bus Factor

# In[15]:


category = 'Bus Factor'
results = count_diff(df, bus_factor, country, category, order_index=True)
results


# In[16]:


plot_cat_comparison(results, country=country, category=category, order_index=True)


# ### Transition plan

# In[17]:


category = 'Presence of a transition plan'
results = count_diff(df, transition_plan, country, category, y_n=True)
results


# In[18]:


plot_cat_comparison(results, country=country, category=category)


# ### Version control

# In[19]:


category = 'Use of version control'
results = count_diff(df, version_control, country, category, multi_choice=True)
results


# In[20]:


plot_cat_comparison(results, country=country, category=category)


# ### Testing

# In[21]:


category = 'Testing strategies'
results = count_diff(df, testing, country, category, multi_choice=True, order_index=order_testing)
results


# In[22]:


plot_cat_comparison(results, country=country, category=category, order_index=order_testing)


# ### Repository 

# In[23]:


category = 'Repository'
plot_wordcloud(df, repo_tool, country, category)


# ## Netherlands

# In[24]:


country = 'Netherlands'


# ### Bus Factor

# In[25]:


category = 'Bus Factor'
results = count_diff(df, bus_factor, country, category, order_index=True)
results


# In[26]:


plot_cat_comparison(results, country=country, category=category, order_index=True)


# ### Transition plan

# In[27]:


category = 'Presence of a transition plan'
results = count_diff(df, transition_plan, country, category, y_n=True)
results


# In[28]:


plot_cat_comparison(results, country=country, category=category)


# ### Version control

# In[29]:


category = 'Use of version control'
results = count_diff(df, version_control, country, category, multi_choice=True)
results


# In[30]:


plot_cat_comparison(results, country=country, category=category)


# ### Testing

# In[31]:


category = 'Testing strategies'
results = count_diff(df, testing, country, category, multi_choice=True, order_index=order_testing)
results


# In[32]:


plot_cat_comparison(results, country=country, category=category, order_index=order_testing)


# ### Repository 

# In[33]:


category = 'Repository'
plot_wordcloud(df, repo_tool, country, category)


# ## New Zealand

# In[34]:


country = 'New Zealand'


# ### Bus Factor

# In[35]:


category = 'Bus Factor'
results = count_diff(df, bus_factor, country, category, order_index=True)
results


# In[36]:


plot_cat_comparison(results, country=country, category=category, order_index=True)


# ### Transition plan

# In[37]:


category = 'Presence of a transition plan'
results = count_diff(df, transition_plan, country, category, y_n=True)
results


# In[38]:


plot_cat_comparison(results, country=country, category=category)


# ### Version control

# In[39]:


category = 'Use of version control'
results = count_diff(df, version_control, country, category, multi_choice=True)
results


# In[40]:


plot_cat_comparison(results, country=country, category=category)


# ### Testing

# In[41]:


category = 'Testing strategies'
results = count_diff(df, testing, country, category, multi_choice=True, order_index=order_testing)
results


# In[42]:


plot_cat_comparison(results, country=country, category=category, order_index=order_testing)


# ### Repository 

# In[43]:


category = 'Repository'
plot_wordcloud(df, repo_tool, country, category)


# ## South Africa

# In[44]:


country = 'South Africa'


# ### Bus Factor

# In[45]:


category = 'Bus Factor'
results = count_diff(df, bus_factor, country, category, order_index=True)
results


# In[46]:


plot_cat_comparison(results, country=country, category=category, order_index=True)


# ### Transition plan

# In[47]:


category = 'Presence of a transition plan'
results = count_diff(df, transition_plan, country, category, y_n=True)
results


# In[48]:


plot_cat_comparison(results, country=country, category=category)


# ### Version control

# In[49]:


category = 'Use of version control'
results = count_diff(df, version_control, country, category, multi_choice=True)
results


# In[50]:


plot_cat_comparison(results, country=country, category=category)


# ### Testing

# In[51]:


category = 'Testing strategies'
results = count_diff(df, testing, country, category, multi_choice=True, order_index=order_testing)
results


# In[52]:


plot_cat_comparison(results, country=country, category=category, order_index=order_testing)


# ### Repository 

# In[53]:


category = 'Repository'
plot_wordcloud(df, repo_tool, country, category)


# ## United Kingdom

# Almost the half of the RSEs' projects have a bus factor of 1 (38%), followed by a bus factor of 2 (35%). Higher bus factor is only marginal with only 9% of the projects having a bus factor of 3 and 6% a bus factor of 4. Higher number are anecdotal. However, it has to be said that, the majority of project are conducted by only one developer, as seen in  Collaboration and training.
# 
# Big or small projects, the presence of a transition plan can mitigate the low bus factor and the risk of project failures. However, only 24% of them are doing so.
# 
# On a better news, 98% of the participants are using version control, with a massive preference for Git (84%). Keep in mind it is a multichoice question. The percentage represents the percentage of participants that have selected that option and it could be alonside other choices. 
# 
# For testing, 7% of the participants confessed they were not implementing any testing at all. It may seems a low number but we think it is still a high percentage considering the specific work of this population. However, it is a big decrease compared to last year (-7%).
# When they are conducting testing, the RSEs seems to prefer (or only able to implement) *Developer testing* (80% of them) or letting the users conduct the testing (22%), while the use of test engineers is marginal (7%).

# In[54]:


country = 'United Kingdom'


# ### Bus Factor

# In[55]:


category = 'Bus Factor'
results = count_diff(df, bus_factor, country, category, order_index=True)
results


# In[56]:


plot_cat_comparison(results, country=country, category=category, order_index=True)


# ### Transition plan

# In[57]:


category = 'Presence of a transition plan'
results = count_diff(df, transition_plan, country, category, y_n=True)
results


# In[58]:


plot_cat_comparison(results, country=country, category=category)


# ### Version control

# In[59]:


category = 'Use of version control'
results = count_diff(df, version_control, country, category, multi_choice=True)
results


# In[60]:


plot_cat_comparison(results, country=country, category=category)


# ### Testing

# In[61]:


category = 'Testing strategies'
results = count_diff(df, testing, country, category, multi_choice=True, order_index=order_testing)
results


# In[ ]:





# In[62]:


plot_cat_comparison(results, country=country, category=category, order_index=order_testing)


# ### Repository 

# In[63]:


category = 'Repository'
plot_wordcloud(df, repo_tool, country, category)


# ## United States

# In[64]:


country = 'United States'


# ### Bus Factor

# In[65]:


category = 'Bus Factor'
results = count_diff(df, bus_factor, country, category, order_index=True)
results


# In[66]:


plot_cat_comparison(results, country=country, category=category, order_index=True)


# ### Transition plan

# In[67]:


category = 'Presence of a transition plan'
results = count_diff(df, transition_plan, country, category, y_n=True)
results


# In[68]:


plot_cat_comparison(results, country=country, category=category)


# ### Version control

# In[69]:


category = 'Use of version control'
results = count_diff(df, version_control, country, category, multi_choice=True)
results


# In[70]:


plot_cat_comparison(results, country=country, category=category)


# ### Testing

# In[71]:


category = 'Testing strategies'
results = count_diff(df, testing, country, category, multi_choice=True, order_index=order_testing)
results


# In[72]:


plot_cat_comparison(results, country=country, category=category, order_index=order_testing)


# ### Repository 

# In[73]:


category = 'Repository'
plot_wordcloud(df, repo_tool, country, category)


# ## Rest of the world

# In[74]:


country = 'World'


# ### Bus Factor

# In[75]:


category = 'Bus Factor'
results = count_diff(df, bus_factor, country, category, order_index=True)
results


# In[76]:


plot_cat_comparison(results, country=country, category=category, order_index=True)


# ### Transition plan

# In[77]:


category = 'Presence of a transition plan'
results = count_diff(df, transition_plan, country, category, y_n=True)
results


# In[78]:


plot_cat_comparison(results, country=country, category=category)


# ### Version control

# In[79]:


category = 'Use of version control'
results = count_diff(df, version_control, country, category, multi_choice=True)
results


# In[80]:


plot_cat_comparison(results, country=country, category=category)


# ### Testing

# In[81]:


category = 'Testing strategies'
results = count_diff(df, testing, country, category, multi_choice=True, order_index=order_testing)
results


# In[82]:


plot_cat_comparison(results, country=country, category=category, order_index=order_testing)


# ### Repository 

# In[83]:


category = 'Repository'
plot_wordcloud(df, repo_tool, country, category)

