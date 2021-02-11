# PYTHON MYSQL RELATED 
from getpass import getpass
from mysql.connector import connect, Error

# step-1 connect to mysql server
try:
  with connect(
    host="localhost",
    user="kidus",
    password="02455",
  ) as connection:
    print(connection)

    # step-2 create a new database(once database created and python runs.. u can't run again)
    # create_db_query = "CREATE DATABASE books_db"
    # with connection.cursor() as cursor:
    #   cursor.execute(create_db_query)

    # display the name of the databases in your server
    show_db_query = "SHOW DATABASES"
    with connection.cursor() as cursor:
      cursor.execute(show_db_query)
      for db in cursor:
        print(db)
except Error as e:
  print(e)

# this code returns mysql connection object and stored in connection variable

# user this variable to access mysql server
