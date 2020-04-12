#!/usr/bin/env python
# coding: utf-8

# $$\Large \textbf{Creating A Database With SQL}$$
# 
# $$\textbf{Phuong Van Nguyen}$$
# 
# This notebook will show how to create a Database with **SQL**

# # Loading Librariries

# In[2]:


get_ipython().run_line_magic('load_ext', 'sql')

import pandas as pd
import sqlite3
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.offline as py
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pandas_profiling import ProfileReport


# # Creating a Database
# First, I will create my own database, namely: ***PhuongDatabase.db***, located in the following folder with its paths as
# 
# >C:\Users\Phuong_1\Documents\SQL\MyDataBaseSQL
# 
# 

# In[3]:


conn= sqlite3.connect("C:/Users/Phuong_1/Documents/SQL/MyDataBaseSQL/PhuongDabase.db")


# After running the code line above, one can see a file, namely: ***PhuongDabase.db***, in the target folder

# # Importing multiple excel files into Database

# In[ ]:


def to_myDataBase(type_file,title_file, conn):
    """
    type_file: string, delaring the type of file, such as 'csv' or 'excel'
    title_file: string, the name of file including its extension
    conn: link to database
    """
    if type_file=='csv':
        df = pd.read_csv(title_file)
        df.to_sql(title_file,conn)
    elif type_file=='excel':
        df=pd.read_excel(title_file)
        df.to_sql(title_file,conn)    
    #%sql sqlite:///C:/Users/Phuong_1/Documents/SQL/MyDataBaseSQL/PhuongDabase.db
    #%sql SELECT name FROM sqlite_master WHERE type='table'


# In[15]:


df=pd.read_excel('Nháp số liệu phòng tư vấn 2020.xlsx')
df.to_sql('Nháp_số_liệu_phòng_tư_vấn_2020',conn)


# In[33]:


df = pd.read_csv('default of credit card clients.csv')
df.to_sql('default_of_credit_card_clients',conn)


# In[36]:


df1 = pd.read_csv('UCI_Credit_Card.csv')
df1.to_sql('UCI_Credit_Card',conn)


# In[42]:


df2 = pd.read_csv('cousin-marriage-data.csv')
df2.to_sql('cousin_marriage_data',conn)


# # Checking database

# In[18]:


get_ipython().run_line_magic('sql', 'sqlite:///C:/Users/Phuong_1/Documents/SQL/MyDataBaseSQL/PhuongDabase.db')
get_ipython().run_line_magic('sql', "SELECT name FROM sqlite_master WHERE type='table'")


# # Exporting data to Pandas DataFrame
# ## By SQL

# In[19]:


df_cousin = get_ipython().run_line_magic('sql', 'SELECT * FROM cousin_marriage_data')
df_cousin=df_cousin.DataFrame()
display(df_cousin.head(5))


# In[20]:


fig = px.bar(df_cousin, x='Percent', y='Country',orientation='h')
fig.show()


# ## By Pandas Read

# In[ ]:


sql_string='SELECT * FROM cousin_marriage_data'
mydata = pd.read_sql(sql_string, conn)
mydata

