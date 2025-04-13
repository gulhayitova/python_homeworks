import pandas as pd
import sqlite3

with sqlite3.connect('chinook.db') as file:
    customers_table = pd.read_sql('SELECT * FROM customers', file)
    invoices_table = pd.read_sql("SELECT * FROM invoices", file)
    joined = pd.merge(customers_table, invoices_table, on='CustomerId', suffixes=[None, '_other'])
    counts = invoices_table['CustomerId'].value_counts().reset_index()
    counts.columns = ['CustomerId', 'Invoices_Count']

csvfile = pd.read_csv('movie.csv')
df1 = csvfile.get(['director_name', 'color'])
df2 = csvfile.get('director_name', 'num_critic_for_reviews')
left_join = pd.merge(df1, df2, on='director_name', how='left')
outer_join = pd.merge(df1, df2, on='director_name', how='outer')
print('The number of rows of the left-joined dataframe =', left_join.count().iloc[1])
print('The number of rows of the outer-joined dataframe =', outer_join.count().iloc[1])