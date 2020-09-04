#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


dfprod= pd.read_csv(r"C:\Users\Federico\Documents\Progetti Jupyter\FIle grezzi\doe-biofuel-consumption-production\Produzione.csv")
pd.set_option('display.max_rows', dfprod.shape[0]+1)


# In[3]:


dfprod.head(20)


# In[4]:


dfprod=dfprod.rename(columns={"Unnamed: 0" : "Country"})


# In[5]:


dfprod.set_index("Country", inplace=True)


# In[6]:


dfprod= dfprod.apply(pd.to_numeric, errors='coerce')


# In[7]:


dfprod.replace(0, np.nan, inplace=True)


# In[8]:


dfprod.dropna(inplace=True)


# In[9]:


dfprodcontinenti=dfprod.loc[["North America","Europe","World", "Central & South America","Asia & Oceania", "Africa"]]


# In[10]:


dfprod.drop(["North America","Europe","World", "Central & South America","Asia & Oceania", "Africa"],inplace=True)


# In[11]:


dfprod.index.name = None


# In[12]:


dfprod=dfprod.T


# In[13]:


dfprod


# In[14]:


dfprod.reset_index(inplace=True)


# In[15]:


dfprod=dfprod.rename(columns={"index":"Year"})


# In[16]:


dfprod= dfprod.melt(id_vars="Year", var_name="Country", value_name="Tonnes")


# In[17]:


dfprodcontinenti.index.name = None


# In[18]:


dfprodcontinenti=dfprodcontinenti.T


# In[19]:


dfprodcontinenti.reset_index(inplace=True)


# In[20]:


dfprodcontinenti["Year"]= dfprodcontinenti["index"]


# In[21]:


dfprodcontinenti.drop("index", axis=1, inplace=True)


# In[22]:


dfprodcontinenti=dfprodcontinenti.melt(id_vars="Year", var_name="Continent", value_name="Tonnes")


# In[23]:


nazioni= list(dfprod["Country"].unique())


# In[24]:


continenti= list(dfprodcontinenti["Continent"].unique())


# In[25]:


continenti


# In[26]:


dfprodtotale= pd.DataFrame()


# In[27]:


#Somma la produzione di una nazione nel decennio
produzione=[]
for nazione in nazioni:
    produzione.append(dfprod.loc[dfprod["Country"]==nazione]["Tonnes"].sum())


# In[28]:


dfprodtotale["Country"]= dfprod["Country"].unique()
dfprodtotale["Tonnes"]=produzione
dfprodtotale=dfprodtotale.sort_values("Tonnes")


# In[29]:


dfprodtotalecontinenti= pd.DataFrame()


# In[30]:


#Somma la produzione di un continente nel decennio
produzione_continenti=[]
for continente in continenti:
    produzione_continenti.append(dfprodcontinenti.loc[dfprodcontinenti["Continent"]==continente]["Tonnes"].sum())


# In[ ]:





# In[31]:


dfprodtotalecontinenti["Continent"]= dfprodcontinenti["Continent"].unique()
dfprodtotalecontinenti["Tonnes"]=produzione_continenti
dfprodtotalecontinenti=dfprodtotalecontinenti.sort_values("Tonnes")


# In[32]:


"""fig, ax=plt.subplots(1 , 2, figsize =(15,8))
plt.tight_layout(True)"""
plt.figure(figsize=(12,8))
plt.tight_layout(True)
ax1=sns.lineplot(data=dfprod, x= "Year", y= "Tonnes", hue= "Country",marker="o")


# In[33]:


plt.figure(figsize=(12,8))
plt.tight_layout(True)
ax2= sns.boxplot(data=dfprod, x= "Country", y= "Tonnes")
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=90, ha="right")


# In[34]:


plt.figure(figsize=(12,8))
plt.tight_layout(True)
ax3=sns.lineplot(data=dfprodcontinenti, x= "Year", y= "Tonnes", hue= "Continent",markers=True, style= "Continent")


# In[35]:


plt.figure(figsize=(12,8))
plt.tight_layout(True)
ax4= sns.boxplot(data=dfprodcontinenti, x= "Continent", y= "Tonnes")


# In[36]:


plt.figure(figsize=(12,8))
plt.tight_layout(True)
ax6= sns.barplot(x="Country", y ="Tonnes", data=dfprodtotale)
ax6.set_xticklabels(ax6.get_xticklabels(), rotation=90, ha="right")


# In[37]:


plt.figure(figsize=(12,8))
plt.tight_layout(True)
ax7= sns.barplot(x="Continent", y ="Tonnes", data=dfprodtotalecontinenti)


# In[ ]:




