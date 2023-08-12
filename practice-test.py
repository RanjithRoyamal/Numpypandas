#!/usr/bin/env python
# coding: utf-8

# # practice-test
# 
# Use the "Run" button to execute the code.

# In[1]:


import pandas as pd


# In[2]:


import matplotlib.pyplot as plt


# In[38]:


import numpy as np


# In[4]:


car_data = pd.read_csv('mtcars.csv')


# In[8]:


import seaborn as sns


# In[14]:


MPG = car_data['mpg']
WT = car_data['wt']


# In[15]:


plt.plot(MPG, WT)


# In[16]:


dimond_data = pd.read_csv('diamond.csv')


# In[18]:


sns.boxplot(x= dimond_data["cut"], y= dimond_data["price"])


# In[ ]:





# In[22]:


df_cocoa = pd.read_csv('flavors_of_cocoa.csv')


# In[24]:


df_cocoa.isna().sum()


# In[28]:


df_cocoa


# In[30]:


countries = df_cocoa['Company Location'] 


# In[35]:


countries.value_counts()



# In[36]:


Rating_df = df_cocoa['Rating']


# In[37]:


Rating_df.max()


# In[39]:


B =[True ,2, 3.0, np.nan, "False"]
[type(i) for i in B]


# In[40]:


jovian.commit


# In[ ]:




