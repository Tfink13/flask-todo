import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = psycopg2.connect(host="localhost",database="flask-todo", user="csetuser", password="Blue132")
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

 # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

     # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')




# import psycopg2
#
# connection = None
#
# try:
#     conn = psycopg2.connect("dbname=test user=postgres")
# except:
#     print("I can't SELECT from task_list")
#
#     cur = connection.cursor()
# try:
#     cur.execute("""SELECT * from task_list""")
#
#
# rows = cur.fetchall()
# print("\nRows: \n")
# for row in rows:
#     print("   ", row)
