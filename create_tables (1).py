import psycopg2
from sql_queries import create_table_queries, drop_table_queries
def create_database():
    try: 
        conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
        
    except psycopg2.Error as e: 
            print("Error: Could not make connection to the Postgres database")
            print(e)
    
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")
    
    conn.close()
    
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn
def drop_tables(cur, conn):

    for query in drop_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except psycopg2.Error as e:
            print("Error: Issue dropping table.")
            print(e)

    print("Tables dropped successfully.")
def create_tables(cur, conn):

    for query in create_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except psycopg2.Error as e:
            print("Error: Issue creating table.")
            print(e)
    print("Tables created successfully.")

def main():

    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)
    conn.close()


if __name__ == "__main__":
    main()