#import statement
from sqlalchemy import create_engine

#This is the SQLAlchemy connection engine. Printing the table names #helps to confirm the connection is live. 
#other databases on AWS include
marketing_data
tourism_data

engine = create_engine('mysql://tourism:XxAheL0MPiLc1oA5h1Fx@utah-tourism.cl2whwpngjxy.us-west-1.rds.amazonaws.com:3306/marketing_data')
connection = engine.connect()
print (engine.table_names())

#alternate connection for marketing data
#mysql://tourism:XxAheL0MPiLc1oA5h1Fx@utah-tourism.cl2whwpngjxy.us-west-1.rds.amazonaws.com:3306/tourism_data

#write your initial SQL query here. This will be used to build the initial DataFrame through SQLAlchemy
query = '''SELECT *
            FROM Adara_Ecosystem'''

df = pd.read_sql(query, connection)

#To read the column names from one of the databases
connection.execute(query).keys()

#To write to the database
#Push tourism taxes to database 'tourism_data'; table named 'tourism_taxes'
df.to_sql(name='table_name', con=connection, if_exists = 'append', index_label = 'index_col')