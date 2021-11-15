#!/usr/bin/env python
# coding: utf-8

# # COVID-19 Analysis in Saudi Arabia [EDA & Visualization]

# Hi in this case study, I am exploring the case of covid 19 in the world and especially in Saudi Arabia and I want to recommend all who see this project to vote and leave a comment to improve the quality of the case study, thanks again and wish you all good health and safety.  osama refay
# - You can find the full project at: https://ourworldindata.org/coronavirus
# - Daily-updated dataset link: https://covid.ourworldindata.org/data/owid-covid-data.csv
# - We'll be exploring the dataset from: https://covid.ourworldindata.org
# - Dashboard Example: https://coronavirus.jhu.edu/map.html

# ## DATA UNDERSTANDING

# ### Importing libraries & data

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set()


# In[2]:


df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')


# In[3]:


df


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.columns


# In[7]:


df.shape


# In[8]:


df.info()


# In[9]:


df.describe()


# In[ ]:





# ==========

# ## EXPLORING WORLD DATA

# ### Listinf all countries / regions in our data

# In[10]:


df['location'].unique()


# In[11]:


df['location'].nunique()


# ### Selecting the 'World' data

# In[12]:


df_world = df[df['location'] == 'World']
df_world


# ### Finding the date of the maximum number of deaths all over the world

# In[13]:


df_world[df_world['new_deaths'] == df_world['new_deaths'].max()]#['date']


# In[14]:


df_world.loc[df_world['new_deaths'].idxmax()]['date']


# ### Creating a summary table for the most recent date all over the world

# In[15]:


df_world_recent = df_world[df_world['date'] == df_world['date'].max()]
df_world_recent


# In[16]:


df_world_recent.groupby("date")[["total_cases","new_cases","new_deaths","total_deaths",'people_vaccinated']].sum()


# ### Calculating the percentage of confirmed cases regarding the world population

# In[17]:


df_world['total_cases'].max()


# In[18]:


df_world['population'].max()


# In[19]:


df_world_cases_ratio = df_world['total_cases'].max() / df_world['population'].max()
df_world_cases_ratio


# #### **The results here is changeable over the time and the results now are 3%**

# ## VISUALLIZING WORLD DATA

# ### Confirmed cases (Total Cases) all over the world

# In[20]:


df_world_AllTime = df_world.groupby('date')[[ 'total_cases', 'new_cases', 'total_deaths', 'new_deaths','people_vaccinated']].sum().reset_index()
df_world_AllTime


# In[21]:


df_world_AllTime.info()


# **I find problem here with date it's a object type and i need to change it to date type**

# In[22]:


df_world_AllTime['date'] = pd.to_datetime(df_world_AllTime['date'])


# **let's check now**

# In[23]:


df_world_AllTime.info()


# **Great problem solved, now let's ploting**

# In[24]:


# Using line-plot
plt.figure(figsize=(20,10))
plt.plot(df_world_AllTime['date'], df_world_AllTime['total_cases'], c='black')
plt.title('Evolution of Confirmed Covid-19 cases over time in the word', fontsize=16)
plt.xlabel('Months', fontsize=16)
plt.ylabel('Confirmed cases', fontsize=16)


# ### Total deaths cases evolution over time

# In[25]:


# Using line-plot
plt.figure(figsize=(20,10))
plt.plot(df_world_AllTime['date'], df_world_AllTime['total_deaths'], c='red')
plt.title('Evolution of Confirmed Covid-19 Deaths over time in the world', fontsize=16)
plt.xlabel('Months', fontsize=16)
plt.ylabel('Confirmed Deaths', fontsize=16)


# ### New cases all over the world

# In[26]:


# Using line-plot
plt.figure(figsize=(20,10))
plt.plot(df_world_AllTime['date'], df_world_AllTime['new_cases'])
plt.title('Evolution of Covid-19 New Cases over time in the world', fontsize=16)
plt.xlabel('Months', fontsize=16)
plt.ylabel('New Cases', fontsize=16)


# ### People vaccinated all over the world

# In[27]:


# Using line-plot
plt.figure(figsize=(20,10))
plt.plot(df_world_AllTime['date'], df_world_AllTime['people_vaccinated'], c='green')
plt.title('Evolution of people vaccinated against Covid-19 over time in the world', fontsize=16)
plt.xlabel('Months', fontsize=16)
plt.ylabel('People vaccinated', fontsize=16)


# ### Putting it all together

# In[28]:


# Using line-plot
plt.figure(figsize=(20,10))
plt.plot(df_world_AllTime['date'], df_world_AllTime['total_cases'], c='black')
plt.plot(df_world_AllTime['date'], df_world_AllTime['total_deaths'], c='red')
plt.plot(df_world_AllTime['date'], df_world_AllTime['people_vaccinated'], c='green')
plt.legend(loc=0)
plt.show()
# Notice i ignore new cases in this figure because it cause duplication with total deaths


# **=============**

# ### Now let's explore the covid status in Saudi Arabia

# ## Exploring Saudi Arabia Data

# ### Let's first get 'Saudi Arabia' data

# In[29]:


df_ksa = df[df['location'] == 'Saudi Arabia']
df_ksa


# ### Creating a summary table for the most recent 'Saudi Arabia' data

# In[30]:


df_ksa.groupby("date")[["total_cases","new_cases","new_deaths","total_deaths",'people_vaccinated']].sum()


# In[31]:


df_ksa_recent_date = df_ksa[df_ksa['date'] == df_ksa.date.max()]
df_ksa_recent_date # notice the outcome here is chaneble over the time you run the code


# In[32]:


df_ksa_recent_date[["total_cases","new_cases","new_deaths","total_deaths",'people_vaccinated']].reset_index()


# ### Calculating the maximum values of 'Saudi Arabia' data

# In[33]:


df_ksa[['total_cases', 'new_cases', 'total_deaths', 'new_deaths','people_vaccinated']].max()


# ### The highest date recorded for death in Saudi Arabia

# In[34]:


df_ksa[df_ksa['new_deaths'] == df_ksa['new_deaths'].max()]['date']


# ### The average value(s) of daily-recorded data in Saudi Arabia

# In[35]:


df_ksa['new_cases'].mean()


# ## **Now let's visualize the data of Saudi Arabia**

# In[36]:


df_ksa_viz = df_ksa.groupby('date')[[ 'total_cases', 'new_cases', 'total_deaths', 'new_deaths','people_vaccinated']].sum().reset_index()
df_ksa_viz['date'] = pd.to_datetime(df_ksa_viz['date'])
df_ksa_viz


# ### Confirmed cases (Total Cases

# In[37]:


plt.figure(figsize=(20,10))
plt.plot(df_ksa_viz['date'], df_ksa_viz['total_cases'], c='black')
plt.title('Evolution of Confirmed Covid-19 cases over time in the Saudi Arabia', fontsize=16)
plt.xlabel('Months', fontsize=16)
plt.ylabel('Confirmed cases', fontsize=16)


# ### Total deaths cases evolution over time

# In[38]:


plt.figure(figsize=(20,10))
plt.plot(df_ksa_viz['date'], df_ksa_viz['total_deaths'], c='red')
plt.title('Evolution of Confirmed Covid-19 deaths over time in the Saudi Arabia', fontsize=16)
plt.xlabel('Months', fontsize=16)
plt.ylabel('Confirmed deaths', fontsize=16)


# ### New cases all over the world

# In[39]:


plt.figure(figsize=(20,10))
plt.plot(df_ksa_viz['date'], df_ksa_viz['new_deaths'], c='blue')
plt.title('Evolution of Covid-19 new cases over time in the Saudi Arabia', fontsize=16)
plt.xlabel('Months', fontsize=16)
plt.ylabel('New Cases', fontsize=16)


# ### People vaccinated all over the world

# In[40]:


plt.figure(figsize=(20,10))
plt.plot(df_ksa_viz['date'], df_ksa_viz['people_vaccinated'], c='green')
plt.title('Evolution of People vaccinated against Covid-19 in the Saudi Arabia', fontsize=16)
plt.xlabel('Months', fontsize=16)
plt.ylabel('People vaccinated', fontsize=16)


# ### Putting it all together

# In[41]:


plt.figure(figsize=(20,10))
plt.plot(df_ksa_viz['date'], df_ksa_viz['total_cases'], c='black')
plt.plot(df_ksa_viz['date'], df_ksa_viz['total_deaths'], c='red')
plt.plot(df_ksa_viz['date'], df_ksa_viz['people_vaccinated'], c='green')
plt.legend(loc=0)
plt.show()


# ==========

# #### **Last words: Please leave a comment or upvote and notice the data are changeable over the time. Thanks for your interesting.   OSAMA REFAY**
