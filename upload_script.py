import pandas as pd
import pyodbc

data = pd.read_csv ('advertising.csv')   
df = pd.DataFrame(data)

conn = pyodbc.connect('Driver=django.db.backends.sqlite3;'
                      'Server=localhost;'
                      'Database=/Users/erkebulanzhumalin/ict/db.sqlite3;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

# Create Table
cursor.execute('''
		CREATE TABLE products (
			product_id int primary key,
			product_name nvarchar(50),
			price int
			)
               ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO products (product_id, product_name, price)
                VALUES (?,?,?)
                ''',
                row.product_id, 
                row.product_name,
                row.price
                )
conn.commit()
