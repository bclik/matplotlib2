#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd


# In[12]:


oluler = pd.read_csv("oluler.csv")


# In[13]:


oluler.head()


# In[14]:



import matplotlib.pyplot as plt
plt.figure(figsize=(15,10))
plt.plot(oluler.age, color="blue")
plt.ylabel("Yaşlar")
plt.title("ilk grafik")
plt.show()




# In[16]:


import matplotlib.pyplot as plt
plt.figure(figsize=(15,10))
plt.plot(oluler.city.head(),oluler.age.head() , color="green")
plt.ylabel("şehirler")
plt.title("ikinci grafik")
plt.show()


# In[ ]:





# In[ ]:




