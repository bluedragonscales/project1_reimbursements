import os
from psycopg import connect, OperationalError

def create_connection():
    try:
        conn = connect(
            host=os.environ.get("HOST2"),
            dbname=os.environ.get("DATABASE"),
            user=os.environ.get("USER"),
            password=os.environ.get("PASSWORD2"),
            port=os.environ.get("PORT")
        )
        return conn
    except OperationalError as o:
        print(str(o))

connection = create_connection()
print(connection)
