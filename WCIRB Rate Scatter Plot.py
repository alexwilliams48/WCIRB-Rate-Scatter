#!/usr/bin/env python
# coding: utf-8

# In[157]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime


# In[158]:


all_files = (r"C:\Users\alexw\OneDrive\Desktop\approved_01012018_pure_premium_rates.csv", 
             r"C:\Users\alexw\OneDrive\Desktop\approved_7_1_2018_pure_premium_rates.csv",    
            r"C:\Users\alexw\OneDrive\Desktop\jan_1_2019_approved_pure_premium_rates.csv",
            r"C:\Users\alexw\OneDrive\Desktop\approved_01012020_pure_premium_rates.csv",
            r"C:\Users\alexw\OneDrive\Desktop\approved_09012021_pure_premium_rates.csv")
rate_dict = {}
for f in all_files:
    df = pd.read_csv(f, header = None)
    for i in df.index:    
        rate_dict.setdefault(df.loc[i, 0], []).append(df.loc[i, 1])
        


# In[159]:


def rate_scat(x):
    
    dates = ["2018-01-10", "2018-01-07", "2019-01-10", "2020-01-10", "2021-01-10"]
    

    y = rate_dict[x]
    plt.scatter(dates, y)
    plt.xlabel("Date")
    plt.ylabel("Premium Rate")
    plt.show()


# In[160]:


rate_scat(2727)
rate_scat(8810)

