import duckdb
import pandas as pd

sql_query = '''
show tables
'''

with duckdb.connect('data/nyc_parking_violation.db') as con:
    print(con.sql(sql_query).df())
