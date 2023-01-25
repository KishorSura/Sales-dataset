#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[73]:


df=pd.read_csv("C:/Users/DELL/Desktop/P6-SuperStoreUS-2015.csv",parse_dates=["Order Date","Ship_Date"])
df.head()


# In[15]:


df.columns


# In[16]:


#Total_profits
df["Profit"].sum()


# In[17]:


#Region wise profit
a=df[["Region","Profit"]].groupby("Region").sum()
a


# In[18]:


a.plot.bar()


# In[19]:


#unquie values of ship mode
df["Ship Mode"].unique()


# In[20]:


#counts
a=df["Ship Mode"].value_counts()


# In[21]:


a.plot()


# In[22]:


#start date
df["Order Date"].min()


# In[23]:


#End date 
df["Order Date"].max()


# In[24]:


#total number of days 
df["Order Date"].max()-df["Order Date"].min()


# In[ ]:





# In[25]:


#I want to had month column 
df["month"]=df["Order Date"].dt.month 
df.head()


# In[83]:


z=df.groupby(df["Order Date"].dt.month)["Profit"].sum()
z.plot()


# In[27]:


#profit per month
x=df.groupby("month")["Profit"].sum()


# In[28]:


z=df.groupby(df["Order Date"].dt.month_name())["Profit"].sum()
z


# In[29]:


#profits of weekdays on basis of regions
day_per_profits=df.groupby([df["Order Date"].dt.weekday,"Region"])["Profit"].sum()
day_per_profits


# In[30]:


a=df["Order Date"].dt.weekday.unique()
a


# In[31]:


day_per_profits.plot()


# In[32]:


df.head()


# In[33]:


#unique values of customer segment column
df["Customer Segment"].unique()


# In[34]:


a=df["Order Date"].dt.weekday.unique()
a


# In[35]:


#total profit of weekdays
b=df.groupby(df["Order Date"].dt.weekday)["Profit"].sum()
b


# In[36]:


c=np.array(b.index)
c


# In[37]:


d=np.array(["Mon","Tue","Wed","Thur","Fri","Sat","Sun"])
d


# In[38]:


plt.xticks(c,d)
plt.bar(d,b,label="Profit")
plt.legend()


# In[39]:


#month list
c=np.array(df["Order Date"].dt.month.unique())
c


# In[40]:


#month name
c=np.array(df["Order Date"].dt.month_name().unique())
c


# In[41]:


df.head()


# In[42]:


#month profits with groupby Customer Segment

Month_profits=df.groupby([df["Order Date"].dt.month_name(),"Customer Segment"])["Profit"].sum()
Month_profits


# In[43]:


Month_profits.plot.line()


# In[80]:


#difference between Order date and Ship date
df["Difference"]=(df["Order Date"]-df["Ship_Date"]).dt.days
df["Difference"]


# In[90]:


#average time for shipping
aveage_days_shipping=df.groupby("Ship Mode")["Difference"].mean()
aveage_days_shipping


# In[88]:


aveage_days_shipping.plot.bar()


# In[92]:


#total discount grouped by Order_Priority
df.groupby(["Order_Priority"])["Discount"].sum()


# In[116]:


#count of order priority for particular city

f=df.groupby(df["Order_Priority"])["City"].value_counts()
f

