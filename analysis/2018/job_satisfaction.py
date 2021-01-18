#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#References" data-toc-modified-id="References-1.0.1"><span class="toc-item-num">1.0.1&nbsp;&nbsp;</span>References</a></span></li></ul></li><li><span><a href="#Questions-in-this-section" data-toc-modified-id="Questions-in-this-section-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Questions in this section</a></span></li><li><span><a href="#Setting-up" data-toc-modified-id="Setting-up-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Setting up</a></span></li></ul></li><li><span><a href="#Job-Satisfaction" data-toc-modified-id="Job-Satisfaction-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Job Satisfaction</a></span><ul class="toc-item"><li><span><a href="#Australia" data-toc-modified-id="Australia-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Australia</a></span><ul class="toc-item"><li><span><a href="#General-satisfaction" data-toc-modified-id="General-satisfaction-2.1.1"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>General satisfaction</a></span></li><li><span><a href="#Recognition" data-toc-modified-id="Recognition-2.1.2"><span class="toc-item-num">2.1.2&nbsp;&nbsp;</span>Recognition</a></span></li><li><span><a href="#Turn-over-intention" data-toc-modified-id="Turn-over-intention-2.1.3"><span class="toc-item-num">2.1.3&nbsp;&nbsp;</span>Turn-over intention</a></span></li><li><span><a href="#Perceived-employability" data-toc-modified-id="Perceived-employability-2.1.4"><span class="toc-item-num">2.1.4&nbsp;&nbsp;</span>Perceived employability</a></span></li><li><span><a href="#Progression-in-the-current-role" data-toc-modified-id="Progression-in-the-current-role-2.1.5"><span class="toc-item-num">2.1.5&nbsp;&nbsp;</span>Progression in the current role</a></span></li></ul></li><li><span><a href="#Germany" data-toc-modified-id="Germany-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Germany</a></span><ul class="toc-item"><li><span><a href="#General-satisfaction" data-toc-modified-id="General-satisfaction-2.2.1"><span class="toc-item-num">2.2.1&nbsp;&nbsp;</span>General satisfaction</a></span></li><li><span><a href="#Recognition" data-toc-modified-id="Recognition-2.2.2"><span class="toc-item-num">2.2.2&nbsp;&nbsp;</span>Recognition</a></span></li><li><span><a href="#Turn-over-intention" data-toc-modified-id="Turn-over-intention-2.2.3"><span class="toc-item-num">2.2.3&nbsp;&nbsp;</span>Turn-over intention</a></span></li><li><span><a href="#Perceived-employability" data-toc-modified-id="Perceived-employability-2.2.4"><span class="toc-item-num">2.2.4&nbsp;&nbsp;</span>Perceived employability</a></span></li><li><span><a href="#Progression-in-the-current-role" data-toc-modified-id="Progression-in-the-current-role-2.2.5"><span class="toc-item-num">2.2.5&nbsp;&nbsp;</span>Progression in the current role</a></span></li></ul></li><li><span><a href="#Netherlands" data-toc-modified-id="Netherlands-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Netherlands</a></span><ul class="toc-item"><li><span><a href="#General-satisfaction" data-toc-modified-id="General-satisfaction-2.3.1"><span class="toc-item-num">2.3.1&nbsp;&nbsp;</span>General satisfaction</a></span></li></ul></li><li><span><a href="#New-Zealand" data-toc-modified-id="New-Zealand-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>New Zealand</a></span><ul class="toc-item"><li><span><a href="#General-satisfaction" data-toc-modified-id="General-satisfaction-2.4.1"><span class="toc-item-num">2.4.1&nbsp;&nbsp;</span>General satisfaction</a></span></li><li><span><a href="#Recognition" data-toc-modified-id="Recognition-2.4.2"><span class="toc-item-num">2.4.2&nbsp;&nbsp;</span>Recognition</a></span></li><li><span><a href="#Turn-over-intention" data-toc-modified-id="Turn-over-intention-2.4.3"><span class="toc-item-num">2.4.3&nbsp;&nbsp;</span>Turn-over intention</a></span></li><li><span><a href="#Perceived-employability" data-toc-modified-id="Perceived-employability-2.4.4"><span class="toc-item-num">2.4.4&nbsp;&nbsp;</span>Perceived employability</a></span></li><li><span><a href="#Progression-in-the-current-role" data-toc-modified-id="Progression-in-the-current-role-2.4.5"><span class="toc-item-num">2.4.5&nbsp;&nbsp;</span>Progression in the current role</a></span></li></ul></li><li><span><a href="#South-Africa" data-toc-modified-id="South-Africa-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>South Africa</a></span><ul class="toc-item"><li><span><a href="#General-satisfaction" data-toc-modified-id="General-satisfaction-2.5.1"><span class="toc-item-num">2.5.1&nbsp;&nbsp;</span>General satisfaction</a></span></li><li><span><a href="#Recognition" data-toc-modified-id="Recognition-2.5.2"><span class="toc-item-num">2.5.2&nbsp;&nbsp;</span>Recognition</a></span></li><li><span><a href="#Turn-over-intention" data-toc-modified-id="Turn-over-intention-2.5.3"><span class="toc-item-num">2.5.3&nbsp;&nbsp;</span>Turn-over intention</a></span></li><li><span><a href="#Perceived-employability" data-toc-modified-id="Perceived-employability-2.5.4"><span class="toc-item-num">2.5.4&nbsp;&nbsp;</span>Perceived employability</a></span></li><li><span><a href="#Progression-in-the-current-role" data-toc-modified-id="Progression-in-the-current-role-2.5.5"><span class="toc-item-num">2.5.5&nbsp;&nbsp;</span>Progression in the current role</a></span></li></ul></li><li><span><a href="#United-Kingdom" data-toc-modified-id="United-Kingdom-2.6"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>United Kingdom</a></span><ul class="toc-item"><li><span><a href="#General-satisfaction" data-toc-modified-id="General-satisfaction-2.6.1"><span class="toc-item-num">2.6.1&nbsp;&nbsp;</span>General satisfaction</a></span></li><li><span><a href="#Recognition" data-toc-modified-id="Recognition-2.6.2"><span class="toc-item-num">2.6.2&nbsp;&nbsp;</span>Recognition</a></span></li><li><span><a href="#Turn-over-intention" data-toc-modified-id="Turn-over-intention-2.6.3"><span class="toc-item-num">2.6.3&nbsp;&nbsp;</span>Turn-over intention</a></span></li><li><span><a href="#Perceived-employability" data-toc-modified-id="Perceived-employability-2.6.4"><span class="toc-item-num">2.6.4&nbsp;&nbsp;</span>Perceived employability</a></span></li><li><span><a href="#Progression-in-the-current-role" data-toc-modified-id="Progression-in-the-current-role-2.6.5"><span class="toc-item-num">2.6.5&nbsp;&nbsp;</span>Progression in the current role</a></span></li></ul></li><li><span><a href="#United-States" data-toc-modified-id="United-States-2.7"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>United States</a></span><ul class="toc-item"><li><span><a href="#General-satisfaction" data-toc-modified-id="General-satisfaction-2.7.1"><span class="toc-item-num">2.7.1&nbsp;&nbsp;</span>General satisfaction</a></span></li><li><span><a href="#Recognition" data-toc-modified-id="Recognition-2.7.2"><span class="toc-item-num">2.7.2&nbsp;&nbsp;</span>Recognition</a></span></li><li><span><a href="#Turn-over-intention" data-toc-modified-id="Turn-over-intention-2.7.3"><span class="toc-item-num">2.7.3&nbsp;&nbsp;</span>Turn-over intention</a></span></li><li><span><a href="#Perceived-employability" data-toc-modified-id="Perceived-employability-2.7.4"><span class="toc-item-num">2.7.4&nbsp;&nbsp;</span>Perceived employability</a></span></li><li><span><a href="#Progression-in-the-current-role" data-toc-modified-id="Progression-in-the-current-role-2.7.5"><span class="toc-item-num">2.7.5&nbsp;&nbsp;</span>Progression in the current role</a></span></li></ul></li><li><span><a href="#Rest-of-the-world" data-toc-modified-id="Rest-of-the-world-2.8"><span class="toc-item-num">2.8&nbsp;&nbsp;</span>Rest of the world</a></span><ul class="toc-item"><li><span><a href="#General-satisfaction" data-toc-modified-id="General-satisfaction-2.8.1"><span class="toc-item-num">2.8.1&nbsp;&nbsp;</span>General satisfaction</a></span></li><li><span><a href="#Recognition" data-toc-modified-id="Recognition-2.8.2"><span class="toc-item-num">2.8.2&nbsp;&nbsp;</span>Recognition</a></span></li><li><span><a href="#Turn-over-intention" data-toc-modified-id="Turn-over-intention-2.8.3"><span class="toc-item-num">2.8.3&nbsp;&nbsp;</span>Turn-over intention</a></span></li><li><span><a href="#Perceived-employability" data-toc-modified-id="Perceived-employability-2.8.4"><span class="toc-item-num">2.8.4&nbsp;&nbsp;</span>Perceived employability</a></span></li><li><span><a href="#Progression-in-the-current-role" data-toc-modified-id="Progression-in-the-current-role-2.8.5"><span class="toc-item-num">2.8.5&nbsp;&nbsp;</span>Progression in the current role</a></span></li></ul></li></ul></li></ul></div>

# # Introduction

# The job satisfaction is an essential pulse to take about a community's health. It helps to track the evolution and the current state of the RSEs within their role and to catch any sign of structural or organisational dysfunction that are translated into well-being. There are a lot of different metrics to measure the quality of a job on a personal and psychological level [1]. Several models exist to understand the link between different factors of job satisfaction and turnover intention [2]–[6]. Turnover intention is an important measure that is highly associated with the risk of employees leaving the organisation [3]. Job satisfaction is important in retaining RSEs. Perceived employability provides information on how workers values their own skills in regard of the market. To measure the different attitudes toward the RSE role, we used scales that have been created in [5], [6], [7], [8]. These are Likert scale [7], which are 5 point ordinal scales graduated from Strongly disagree to Strongly agree. Each scale is composed of several so called items (i.e. questions) that each measure one attitude.
# 
# Beside these specific concepts we asked more general question about their satisfaction in their current position and their satisfaction with their career in general with a range of answers from *0 - Not at all satisfied* to *10 - Completely satisfied*.
# 
# The specific questions about their job satisfaction reflect, in general, the same opinion as the two more generic questions. However, the granularity helps to identify a couple of issues that would not appears with generic questions:
# 
# * **Recognition**: These questions ask if the RSEs feel that they receive enough information about their work and their performance.
# 
# * **The turnover intention**: These questions aim to measure the desire to quit their current position.
# 
# * **The perceived employability**: This concept is linked to the previous one. People may not have the intention to leave their jobs, not because they like it, but because they fear they are not employable. 
# 
# * **The possibility of progression**: This question aims to study the possibility of evolution for the RSEs, if information is available and if they see a possibility of evolution within their current career. This is the only questions that clearly received negative answers.
# 
# 
# We used to ask for more questions in the previous years. But the results were not showing anything interesting. In consequence, we decided to remove them for this year, helping to reduce the size of the survey. 
# 
# ### References
# 
# * [1] B. Aziri, “Job satisfaction: A literature review,” vol. 3, no. 4, pp. 77–86.
# * [2] N. De Cuyper, S. Mauno, U. Kinnunen, and A. Mkikangas, “The role of job resources in the relation between perceived employability and turnover intention: A prospective two-sample study,” vol. 78, no. 2, pp. 253–263.
# * [3] A. B. Bakker and E. Demerouti, “The job demands-resources model: State of the art,” vol. 22, no. 3, pp. 309–328.
# * [4] G. H. L. Cheng and D. K. S. Chan, “Who Suffers More from Job Insecurity? A Meta-Analytic Review.” vol. 57, no. 2, p. 272.
# * [5] E. R. Thompson and F. T. Phua, “A brief index of affective job satisfaction,” vol. 37, no. 3, pp. 275–307.
# * [6] L. Greenhalgh and Z. Rosenblatt, “Job insecurity: Toward conceptual clarity,” pp. 438–448.
# * [7] R. Likert, “A technique for the measurement of attitudes.” vol. 22, no. 140, p. 55.

# ## Questions in this section
# 
# * `In general, how satisfied are you with your current position`: likert scale
# * `In general, how satisfied are you with your career`: likert scale
# 
# * `Do you feel that your contribution to research is recognised by your supervisor/line manager`: likert scale
# * `Do you feel that your contribution to research is recognised by the researchers you work with`: likert scale
# * `Do you feel that your contribution to research is recognised by your institution?`: likert scale
# 
# * `How often do you consider leaving your job?`: likert scale
# * `I would accept another job at the same compensation level if I was offered it`: likert scale
# 
# * `It would not be very difficult for me to get an equivalent job in a different institution`: likert scale
# * `My experience is in demand on the labour market`: likert scale
# 
# * `It is likely that I will gain a promotion within my current group`: likert scale
# * `The process I have to complete to gain a promotion is clear and understandable`: likert scale
# * `There are many opportunities within my chosen career plan`: likert scale
# * `It is likely that my next position will be an Research Software Engineer / Research`: likert scale

# ## Setting up

# In[1]:


get_ipython().run_cell_magic('capture', ' ', '# Import notebook containing the imports the functions and the dataset\n%run "./0. Imports and functions.ipynb"\n\n# Import notebook containing sampled dataset\n%run "./1. Overview and sampling.ipynb"')


# # Job Satisfaction

# In[2]:


satis_gen = ['satisGen1. In general, how satisfied are you with your current position', 'satisGen2. In general, how satisfied are you with your career']

recog = ['recog1. Do you feel that your contribution to research is recognised by your supervisor/line manager',
         'recog2. Do you feel that your contribution to research is recognised by the researchers you work with',
         'recog3. Do you feel that your contribution to research is recognised by your institution?']

turn_over1 = ['turnOver3. How often do you consider leaving your job?']
turn_over2 = ['turnOver6. I would accept another job at the same compensation level if I was offered it']

perc_emp =['percEmp1. It would not be very difficult for me to get an equivalent job in a different institution',
           'percEmp3. My experience is in demand on the labour market']

prog_rse = ['progRSE1. It is likely that I will gain a promotion within my current group',
            'progRSE2. The process I have to complete to gain a promotion is clear and understandable',
            'progRSE3. There are many opportunities within my chosen career plan',
            'progRSE5. It is likely that my next position will be an Research Software Engineer / Research Software Developer role']


#agree_scale = ['Strongly Agree', 'Agree', 'Neither agree or disagree',
 #              'Strongly disagree', 'Disagree']
agree_scale = ['Strongly disagree', 'Disagree', 'Neither agree or disagree', 'Agree','Strongly Agree']

number_scale = [str(i) for i in range(11)[1:]]


# ## Australia

# In[3]:


country = 'Australia'


# ### General satisfaction

# In[4]:


category = 'General satisfaction'
plotting_likert(df, country, category, satis_gen, order_scale=number_scale)


# ### Recognition

# In[5]:


recog_cat = 'Recognition'
plotting_likert(df, country, category, recog, order_scale=agree_scale)


# ### Turn-over intention

# In[6]:


category = 'Intention of changing position'
plotting_likert(df, country, category, turn_over1, order_scale=number_scale)


# In[7]:


category = 'Intention of changing position'
plotting_likert(df, country, category, turn_over2, order_scale=agree_scale)


# ### Perceived employability

# In[8]:


category = 'Perceived employability'
plotting_likert(df, country, category, perc_emp, order_scale=agree_scale)


# ### Progression in the current role

# In[9]:


category = 'Progression in the current position'
plotting_likert(df, country, category, prog_rse, order_scale=agree_scale)


# ## Germany

# In[10]:


country = 'Germany'


# ### General satisfaction

# In[11]:


category = 'General satisfaction'
plotting_likert(df, country, category, satis_gen, order_scale=number_scale)


# ### Recognition

# In[12]:


recog_cat = 'Recognition'
plotting_likert(df, country, category, recog, order_scale=agree_scale)


# ### Turn-over intention

# In[13]:


category = 'Intention of changing position'
plotting_likert(df, country, category, turn_over1, order_scale=number_scale)


# In[14]:


category = 'Intention of changing position'
plotting_likert(df, country, category, turn_over2, order_scale=agree_scale)


# ### Perceived employability

# In[15]:


category = 'Perceived employability'
plotting_likert(df, country, category, perc_emp, order_scale=agree_scale)


# ### Progression in the current role

# In[16]:


category = 'Progression in the current position'
plotting_likert(df, country, category, prog_rse, order_scale=agree_scale)


# ## Netherlands

# In[17]:


country = 'Netherlands'


# ### General satisfaction

# In[18]:


category = 'General satisfaction'
plotting_likert(df, country, category, satis_gen, order_scale=number_scale)


# ## New Zealand

# In[19]:


country = 'New Zealand'


# ### General satisfaction

# In[20]:


category = 'General satisfaction'
plotting_likert(df, country, category, satis_gen, order_scale=number_scale)


# ### Recognition

# In[21]:


recog_cat = 'Recognition'
plotting_likert(df, country, category, recog, order_scale=agree_scale)


# ### Turn-over intention

# In[22]:


category = 'Intention of changing position'
plotting_likert(df, country, category, turn_over1, order_scale=number_scale)


# In[23]:


category = 'Intention of changing position'
plotting_likert(df, country, category, turn_over2, order_scale=agree_scale)


# ### Perceived employability

# In[24]:


category = 'Perceived employability'
plotting_likert(df, country, category, perc_emp, order_scale=agree_scale)


# ### Progression in the current role

# In[25]:


category = 'Progression in the current position'
plotting_likert(df, country, category, prog_rse, order_scale=agree_scale)


# ## South Africa

# In[26]:


country = 'South Africa'


# ### General satisfaction

# In[27]:


category = 'General satisfaction'
plotting_likert(df, country, category, satis_gen, order_scale=number_scale)


# ### Recognition

# In[28]:


recog_cat = 'Recognition'
plotting_likert(df, country, category, recog, order_scale=agree_scale)


# ### Turn-over intention

# In[29]:


category = 'Intention of changing position'
plotting_likert(df, country, category, turn_over1, order_scale=number_scale)


# In[30]:


category = 'Intention of changing position'
plotting_likert(df, country, category, turn_over2, order_scale=agree_scale)


# ### Perceived employability

# In[31]:


category = 'Perceived employability'
plotting_likert(df, country, category, perc_emp, order_scale=agree_scale)


# ### Progression in the current role

# In[32]:


category = 'Progression in the current position'
plotting_likert(df, country, category, prog_rse, order_scale=agree_scale)


# ## United Kingdom

# Starting with the good news. The participants are satisfied with their career and their current position. 
# They report a strong recognition from their supervisors and their colleagues. However, the recognition on the institutional level is less strong and even negative with 30% of negative reports. 
# This year, the participants reported more turn-over intention than before. 41% are indecisive, up to 20% would accept another position with the same compensations. 
# This is probably helped by their perceived employability. 74% of the participants think their skills are in demand on the market and 53% thinks it will be easier for them to find another position.
# 
# Another factor of this turn-over intention could be the progression in their current position. While the participants think their next position will probably be as RSE (51% agree or strongly agree), they seems less positive about the possibility in long term. They do not think there is a lot of opportunities in their career plan (46% disagree or completely disagree), 53% think the process to gain a promotion is not clear or understandable and 53% that it is unlikely they will gain a promotion in their current group.

# In[33]:


country = 'United Kingdom'


# ### General satisfaction

# In[34]:


category = 'General satisfaction'
plotting_likert(df, country, category, satis_gen, order_scale=number_scale)


# ### Recognition

# In[35]:


recog_cat = 'Recognition'
plotting_likert(df, country, category, recog, order_scale=agree_scale)


# ### Turn-over intention

# In[36]:


category = 'Intention of changing position'
plotting_likert(df, country, category, turn_over1, order_scale=number_scale)


# In[37]:


category = 'Intention of changing position'
plotting_likert(df, country, category, turn_over2, order_scale=agree_scale)


# ### Perceived employability

# In[38]:


category = 'Perceived employability'
plotting_likert(df, country, category, perc_emp, order_scale=agree_scale)


# ### Progression in the current role

# In[39]:


category = 'Progression in the current position'
plotting_likert(df, country, category, prog_rse, order_scale=agree_scale)


# ## United States

# In[40]:


country = 'United States'


# ### General satisfaction

# In[41]:


category = 'General satisfaction'
plotting_likert(df, country, category, satis_gen, order_scale=number_scale)


# ### Recognition

# In[42]:


recog_cat = 'Recognition'
plotting_likert(df, country, category, recog, order_scale=agree_scale)


# ### Turn-over intention

# In[43]:


category = 'Intention of changing position'
plotting_likert(df, country, category, turn_over1, order_scale=number_scale)


# In[44]:


category = 'Intention of changing position'
plotting_likert(df, country, category, turn_over2, order_scale=agree_scale)


# ### Perceived employability

# In[45]:


category = 'Perceived employability'
plotting_likert(df, country, category, perc_emp, order_scale=agree_scale)


# ### Progression in the current role

# In[46]:


category = 'Progression in the current position'
plotting_likert(df, country, category, prog_rse, order_scale=agree_scale)


# ## Rest of the world

# In[47]:


country = 'World'


# ### General satisfaction

# In[48]:


category = 'General satisfaction'
plotting_likert(df, country, category, satis_gen, order_scale=number_scale)


# ### Recognition

# In[49]:


recog_cat = 'Recognition'
plotting_likert(df, country, category, recog, order_scale=agree_scale)


# ### Turn-over intention

# In[50]:


category = 'Intention of changing position'
plotting_likert(df, country, category, turn_over1, order_scale=number_scale)


# In[51]:


category = 'Intention of changing position'
plotting_likert(df, country, category, turn_over2, order_scale=agree_scale)


# ### Perceived employability

# In[52]:


category = 'Perceived employability'
plotting_likert(df, country, category, perc_emp, order_scale=agree_scale)


# ### Progression in the current role

# In[53]:


category = 'Progression in the current position'
plotting_likert(df, country, category, prog_rse, order_scale=agree_scale)

