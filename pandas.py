#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
obj=pd.Series([4,7,-5,3])
obj


# In[3]:


s = pd.Series([0,1,2,3,4,5],index=['a','b','c','d','e','f'])
s


# In[4]:


sadd = pd.Series([6],index=['g'])
sadd


# In[5]:


s = s.append(sadd)
s


# In[6]:


jisyo = {"apple":10,"bravo":11,"charlie":12,"dom":13,"emperor":14}
jisyo


# In[7]:


ss = pd.Series


# In[8]:


ss = jisyo.copy()
ss


# In[9]:


absentkeylist = ["apple","bravo","charlie","dom","emperor","full"]
absentkeylist


# In[10]:


jisyo[absentkeylist[0]]


# In[11]:


jisyo[absentkeylist[1]]


# In[12]:


jisyo[absentkeylist[2]]


# In[13]:


for i in range(4):
    print(jisyo[absentkeylist[i]]) 


# In[14]:


valuelist=[10,11,12,13]
valuelist


# In[15]:


for i in range(4):
    print(jisyo[valuelist[i]]) 


# In[18]:


sss = pd.Series(jisyo,index=absentkeylist)
sss


# In[19]:


sdata={'Ohio':35000, 'Texas':70000, 'Oragon':16000, 'Utah':5000}
obj3=pd.Series(sdata)
states=['California', 'Ohio', 'Oragon', 'Texas']
obj4=pd.Series(sdata, index=states)
obj4


# In[20]:


data=pd.date_range('2019/1/1',periods=10,freq='D')
data


# In[21]:


data=pd.date_range('2019/1/1',periods=10,freq='D')
data


# In[22]:


data.weekday


# In[23]:


data.year


# In[24]:


data.hour


# In[25]:


data=pd.date_range('2019/1/1',periods=10,freq='1H')
data


# In[26]:


data.hour


# In[27]:


data=pd.date_range('2019/1/1',periods=10,freq='D')
data


# In[28]:


import numpy as np
vlist = np.arange(10)
vlist


# In[29]:


lol = pd.Series(vlist,index = data)
lol


# In[30]:


d5 = lol['2019-01-05']
d5


# In[31]:


loll = pd.Series(np.arange(10),index = data)
loll


# In[32]:


ydata=pd.date_range('2019',periods=10,freq='Y')
ydata


# In[33]:


ydata=pd.date_range('2019/1/1',periods=10,freq='Y')
ydata


# In[34]:


ydata=pd.date_range('2019',periods=10,freq='Y')
ydata


# In[35]:


yse = pd.Series(np.arange(10),index = ydata)
yse


# In[36]:


ysdata=pd.date_range('2019',periods=10,freq='YS')
ysdata


# In[37]:


ywdata = pd.date_range('2019/4/25',periods=10,freq='W-THU')
ywdata


# In[38]:


ywse = pd.Series(np.arange(10),index = ywdata)
ywse


# In[39]:


ymedata = pd.date_range('2019/1/1',periods=12,freq='M')
ymedata


# In[40]:


ddata = pd.date_range('2019/04/25',periods=10,freq='D')
ddata


# In[41]:


dse = pd.Series(np.arange(10),index=ddata)
dse


# In[42]:


dse = dse+10
dse


# In[43]:


sum(dse)


# In[44]:


np.sum(dse)


# In[45]:


dse.describe()


# In[46]:


np.std(dse)


# In[ ]:





# In[ ]:





# In[ ]:




