#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
reserve = pd.read_csv(rf'C:\Users\kobay\Python3kobayu\reserve.csv',encoding='UTF-8')
reserve


# In[ ]:





# In[ ]:





# In[63]:


res5 = reserve[:5]
res5


# In[52]:


import numpy as np
zf = np.array(res5)
zf


# In[42]:


resind = reserve.columns
resind


# In[ ]:





# In[64]:


b = pd.DataFrame(zf,columns=resind)
b


# In[59]:


h75=reserve[reserve.hotel_id=='h_75']
h75


# In[68]:


h75price = reserve['h75.total_price'/(('h75.checkin_date'-'h75.checkout_date')*'h75.people_num')]
h75price


# In[70]:


reserve.describe()


# In[79]:


reserve.sort_values(['hotel_id','customer_id'])


# In[80]:


reserve.sort_values(['checkin_time','people_num'])


# In[81]:


reserve.sort_values(['checkin_time'])


# In[83]:


reserve[reserve.people_num==4]


# In[84]:


reserve.sort_values(['total_price'])


# In[87]:


solo=reserve[reserve.people_num==1]
solo


# In[90]:


solo.sort_values(['total_price','hotel_id'])


# In[92]:


df_val1=reserve.iloc[0:5].values
df_val1


# In[103]:


reserve[(reserve.checkout_date=='2016-10-13')|(reserve.checkout_date=='2016-10-14')]


# In[104]:


reserve[(reserve.checkout_date=='2016-10-13'):(reserve.checkout_date=='2016-10-14')]


# In[119]:


rese=reserve.sort_values(['checkout_date','reserve_id'])
rese


# In[120]:


rese.query('"2016-10-13" <= checkout_date <= "2016-10-14"')


# In[121]:


reserveb = reserve.query('"2016-10-13" <= checkout_date <= "2016-10-14"')
reserveb


# In[ ]:




