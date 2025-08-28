import psycopg2
from psycopg2 import sql

def create_schema_and_tables(db_name, user, password, host, port, schema_name):
    """
    Connects to a PostgreSQL database, creates a new schema, and then creates
    a table within that schema.

    Args:
        db_name (str): The name of the database.
        user (str): The username for the database.
        password (str): The password for the database user.
        host (str): The host address of the database.
        port (int): The port number for the database.
        schema_name (str): The name of the schema to create.
    """
    conn = None
    try:
        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        cur = conn.cursor()

        # Use the psycopg2.sql module for safe and dynamic SQL queries.
        # This prevents SQL injection attacks.

        # 1. Create the new schema
        print(f"Attempting to create schema: {schema_name}")
        cur.execute(sql.SQL("CREATE SCHEMA IF NOT EXISTS {}").format(
            sql.Identifier(schema_name)
        ))
        print(f"Schema '{schema_name}' created or already exists.")

        # 2. Create a table within the new schema
        table_name = "users"
        create_table_query = sql.SQL("""
            CREATE TABLE IF NOT EXISTS {schema}.{table} (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
            )
        """).format(
            schema=sql.Identifier(schema_name),
            table=sql.Identifier(table_name)
        )
        
        print(f"Attempting to create table '{table_name}' in schema '{schema_name}'.")
        cur.execute(create_table_query)
        print(f"Table '{table_name}' created or already exists in schema '{schema_name}'.")
        
        # Commit the transaction
        conn.commit()
        print("Changes committed successfully.")

    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to or interacting with PostgreSQL: {error}")

    finally:
        # Close the database connection
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed.")

# --- How to use the function ---
if __name__ == "__main__":
    # Replace these with your actual database credentials and desired schema name
    DB_NAME = "your_database_name"
    USER = "your_username"
    PASSWORD = "your_password"
    HOST = "localhost" # or your host address
    PORT = 5432 # or your port
    NEW_SCHEMA_NAME = "analytics_data"

    create_schema_and_tables(
        db_name=DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        schema_name=NEW_SCHEMA_NAME
    )