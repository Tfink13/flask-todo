import psycopg2

import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(f"dbname={current_app.config['DB_NAME']} user={current_app.config['DB_USER']}")
        #  ask zach
        # "f"dbname={current_app.config['DB_NAME']} user={current_app.config['DB_USER']}""
        # "dbname=flask_todo user=csetuser"

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        cur = db.cursor()
        cur.execute("SELECT * from all_tasks")
        rows = cur.fetchall()
        print(rows)
        cur.execute(f.read())
        cur.close()
        db.commit()

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)




# import psycopg2
# from config import config
#
# def connect():
#     # """ Connect to the PostgreSQL database server """
#     conn = psycopg2.connect("""host="localhost",database="flask-todo", user="csetuser", password="Blue132""")
#     try:
#         # read connection parameters
#         params = config()
#
#         # connect to the PostgreSQL server
#         print('Connecting to the PostgreSQL database...')
#         conn = psycopg2.connect(**params)
#
#         # create a cursor
#         cur = conn.cursor()
#
#         # execute a statement
#         print('PostgreSQL database version:')
#         cur.execute('SELECT version()')
#
#         # display the PostgreSQL database server version
#         db_version = cur.fetchone()
#         print(db_version)
#
#      # close the communication with the PostgreSQL
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#             print('Database connection closed.')




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
