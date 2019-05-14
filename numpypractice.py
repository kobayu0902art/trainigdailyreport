#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
abc = np.array([
[
    [1,2,3],
    [4,5,6],
    [7,8,9]
],
[
    [10,11,12],
    [13,14,15],
    [16,17,18]
],
[
    [19,20,21],
    [22,23,24],
    [25,26,27]
]
    
]
)


# In[47]:


abc


# In[ ]:


tbyt = np.array(
[
    [0,1,2],
    [3,4,5],
    [6,7,8]
]
)


# In[ ]:


tbytbyt = (
[
    [0,1,2],
    [3,4,5],
    [6,7,8]
],
[
    [9,10,11],
    [12,13,14],
    [15,16,17]
],
[
    [18,19,20],
    [21,22,23],
    [24,25,26]
]
)


# In[ ]:


n = tbyt + tbyt 


# In[42]:


n


# In[43]:


n = tbyt + tbytbyt
n


# In[44]:


n = tbytbyt + tbyt
n


# In[45]:


tenbyten = np.array(
[
    [i,i,i,i,i,i,i,i,i,i]
        for i in range(10)
]
)
    
tenbyten


# In[46]:


tenbytenbyorder = np.array(
[
    [i,i+1,i+2,i+3,i+4,i+5,i+6,i+7,i+8,i+9]
            for i in range(10)
]
)
tenbytenbyorder


# In[ ]:


int_array=np.arange(9)
arr_3d=int_array.reshape(3,3)


# In[41]:


arr_3d


# In[52]:


tenbythund = np.arange(3000)
arr_100d = hundbyhund.reshape(300,10)
arr_100d


# In[ ]:


for i in range(2):
    print(arr_3d[1][i]) 


# In[83]:


dis = arr_3d[0:2:,1:3]
dis


# In[90]:


dis1 = arr_3d[]
dis1


# In[91]:


arr_3d[:2,1:]


# In[94]:


arr_3d[1:2,0:2]


# In[95]:


int_array=np.arange(9)
arr_3d=int_array.reshape(3,3)
arr_3d = arr_3d+arr_3d
arr_3d


# In[96]:


int_array=np.arange(9)
arr_3d=int_array.reshape(3,3)
arr_3d = arr_3d*2
arr_3d


# In[98]:


arr_3d < 7
arr_3d


# In[99]:


bool = arr_3d < 7
bool


# In[103]:


arr_3d*2 < 7


# In[ ]:




