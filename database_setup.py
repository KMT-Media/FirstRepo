import mysql.connector
from mysql.connector import errorcode
from databases_2 import cursor

# database name
db_name = 'acme'

# create table
TABLES = {}

TABLES['logs'] = (
    "CREATE TABLE `logs` ("
    " `id` int(11) NOT NULL AUTO_INCREMENT",
    " `text` varchar(100) NOTNULL",
    " `user` varchar(100) NOTNULL",
    " `created` datetime NOTNULL DEFAULT CURRENT_TIMESTAMP,"
    " PRIMARY KEY(`id`)"
    ")ENGINE=InnoDB"
)
def create_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
    print('Database {} created'.format(db_name))

# def create_table():
#     cursor.execute("USE {}".format(db_name))

#     for table_name in TABLES:
#         table_description = TABLES[table_name]
#         try:
#             print("Creating table ({})".format(db_name))
#             # cursor.execute()
#         except mysql.connector.Error as err:
#             if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#                 print('TABLE ALREADY EXISTS')
#             else:
#                 print(err.msg)

def show_databases():
    show_database_query = "SHOW DATABASES"
    cursor.execute(show_database_query)
    # returns list of dabtbase names in tuple
    for db in cursor:
        print(db)

def show_tables():
    cursor.execute("USE {}".format(db_name)) 
    cursor.execute("SHOW TABLES")
    for table_data in cursor:
        print(table_data)

create_database()
# create_table()
# show_databases()
show_tables()