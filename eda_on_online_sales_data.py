# -*- coding: utf-8 -*-
"""EDA on Online Sales Data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1td5OkzhZ1TlIAjyZiKzfF2PZG8XFax5H
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
# %matplotlib inline

df = pd.read_excel('/content/drive/MyDrive/Online Retail.xlsx')

df.head()

df.head()

df.shape

df.describe()

df['InvoiceYearMonth']=df['InvoiceDate'].map(lambda date:100*date.year+date.month)
df['Revenue']=df['Quantity']*df['UnitPrice']
df.head()

df_revenue=df.groupby(['InvoiceYearMonth']).agg({'Revenue':sum}).reset_index()
df_revenue.head()

import seaborn as sns

sns.lineplot(data=df_revenue)

sns.barplot(data=df_revenue,x='InvoiceYearMonth',y='Revenue')
plt.xticks(rotation=45)
plt.show()

df.isna().sum()

df.dropna(inplace=True)

df.isna().sum()

df.shape

df['Month']=df['InvoiceDate'].dt.month

df['Day']=df['InvoiceDate'].dt.day_name()

duplicate_rows=df.duplicated()
duplicate_rows.sum()
if True in duplicate_rows:
  df=df[~duplicate_rows]

df_revenue['MonthlyGrowth']=df_revenue['Revenue'].pct_change()

df['Country'].nunique()

df['Country'].unique()

df_USA=df[df['Country']=='USA']
df_USA

df_MOQ=df.groupby('InvoiceYearMonth')['Quantity'].sum()
df_MOQ

