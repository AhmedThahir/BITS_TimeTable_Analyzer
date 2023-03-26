#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


import tabula as tb
from tabula.io import read_pdf


# In[27]:


dfs = read_pdf(
    "FD_Timetable_First Semester 2022-23.pdf",
    pages = "all"
)
dfs


# In[43]:


combined = pd.DataFrame()
for df in dfs[1:2]:
    pd.concat([combined, df], ignore_index=True)


# In[47]:


df = dfs[3]
pd.concat([combined, df], ignore_index=True)

