import psycopg2
from project2 import ss

hostname='localhost'
database='postgres'
pwd='navgurukul'
username='postgres'
port_id=5432

conn=None
cur=None
try:
    conn=psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id )

    cur=conn.cursor()
    create_script='''CREATE TABLE if not exists movieinfo(
        movie_name varchar(50),
        release_date varchar(40) )'''

    cur.execute(create_script)
    conn.commit()
    for i in ss:
        cur.execute("insert into movieinfo(movie_name,release_date) values(%s,%s)",i)
    print("successfully inserted....")
    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
    
