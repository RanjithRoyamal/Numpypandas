#!/usr/bin/env python
# coding: utf-8

# # missing-data
# 
# Use the "Run" button to execute the code.

# In[1]:


print('Hello World')


# In[2]:


import os


# In[3]:


import pandas as pd


# In[8]:


cars_data = pd.read_csv("Toyota.csv", index_col=0,na_values = ["??", "????"])


# In[9]:


cars_data2 = cars_data.copy()


# In[19]:


cars_data2.shape


# In[10]:


cars_data3 = cars_data2.copy()


# In[11]:


cars_data2.isna().sum()


# In[14]:


missing = cars_data2[cars_data2.isnull().any(axis=1)]


# In[18]:


missing.shape


# In[20]:


cars_data2.describe()


# In[21]:


cars_data2['Age'].mean()


# In[25]:


cars_data2['Age'].fillna(cars_data2['Age'].mean(),inplace = True)


# In[26]:


cars_data2['KM'].median()


# In[27]:


cars_data2['KM'].fillna(cars_data2['KM'].median(),inplace = True)


# In[28]:


cars_data2['HP'].mean()


# In[29]:


cars_data2['HP'].fillna(cars_data2['HP'].mean(),inplace = True)


# In[30]:


cars_data2.isnull().sum()


# In[32]:


cars_data2['FuelType'].value_counts()


# In[36]:


cars_data2['FuelType'].value_counts().index[0]


# In[37]:


cars_data2['FuelType'].fillna(cars_data2['FuelType'].value_counts().index[0],inplace = True)


# In[41]:


cars_data2['MetColor'].mode()


# In[42]:


cars_data2['MetColor'].fillna(cars_data2['MetColor'].mode()[0],inplace = True)


# In[43]:


cars_data2.isnull().sum()


# In[44]:


cars_data3.isnull().sum()


# # Filling the missing Values at one shot using if statements.

# In[45]:


cars_data3 = cars_data3.apply(lambda x:x.fillna(x.mean())if x.dtype=='float' else x.fillna(x.value_counts().index[0]))


# In[46]:


cars_data3.isnull().sum()


# In[47]:


cars_data3


# In[48]:


import jovian


# In[51]:


jovian.commit


# In[ ]:




