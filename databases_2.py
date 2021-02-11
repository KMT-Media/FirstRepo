# PYTHON MYSQL REALTED

import mysql.connector as mc
config = {
    'host':'localhost',
    'user':'kidus',
    'password':'02455'
}
mydb = mc.connect(**config)
cursor = mydb.cursor()

# create a database
# create_db_query = "CREATE DATABASE cars"
# cursor.execute(create_db_query)

# check if database exists
# show_db_query = "SHOW DATABASES"
# cursor.execute(show_db_query)
# for db in cursor:
#     print(db)

# cursor is used to execute queries