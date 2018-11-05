#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import regex as re
import numpy as np
import os

# Read in a plain text file
with open(os.path.join("trial1.txt"), "r") as f:
    text = f.read()
with open(os.path.join("trial2.txt"), "r") as f:
    text1= f.read()
with open(os.path.join("trial3.txt"), "r") as f:
    text2= f.read()


# In[11]:


t = [text,text1]
print(text)


# In[12]:


print(text1)


# In[3]:


justices = re.findall('JUSTICE[A-Z\s]+:',text)


# In[5]:


def unique(lst):
    uni = []
    for i in lst:
        if i not in uni:
            uni += [i]
    return uni


# In[18]:


unique(re.findall('JUSTICE[A-Z\s]+:',text2))


# In[16]:


unique(re.findall('JUSTICE[A-Z\s]+:',text1))


# In[6]:


unique(justices)


# In[23]:


unique(re.findall('No.\s\d+-\d+',text))[0]


# In[9]:


def case_no(txt):
    return unique(re.findall('No.\s\d+-\d+',text))


# In[10]:


case_no(text1)


# In[32]:


def justices(texts):
    d = {}
    for txt in texts:
        j = re.findall('JUSTICE[A-Z\s]+:',txt)
        justice = unique(j)
        num = case_no(txt)[0]
    for n in num:
        d[n] = justice
    return justice


# In[ ]:





# In[33]:


justices(t)


# In[ ]:





# In[ ]:




