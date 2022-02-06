#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


vendas = {'produtos':['melancia', 'mamao'],'quantidade':[2, 4],'valor':[12, 14], 'marca':['bradesco','consul']}
vendas_tabela = pd.DataFrame(vendas)
print(vendas_tabela)
display(vendas_tabela)


# In[32]:


df = pd.read_excel("C:\\Users\\Asus\\Documents\\porto_galinhas.xlsx")
df


# In[23]:


df


# In[6]:


import pandas as pd
df = pd.read_excel("C:\\Users\\Asus\\Downloads\\Vendas.xlsx")
df


# In[8]:


import pandas as pd
df = pd.read_excel("C:\\Users\\Asus\\Downloads\\Vendas.xlsx")
display(df)


# In[ ]:




