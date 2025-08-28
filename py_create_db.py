import psycopg2
import ssl

db_config = {
    "host": "172.17.0.2",  
    "port": 5432,
    "database": "postgres",       
    "user": "myuser",      
    "password": "mypassword",
    "sslmode": "verify-full",
    "sslrootcert": "ssl/ca.crt"
}

new_db_name = "new_db"

try:
    print("Connecting to the PostgreSQL database...")
    connection = psycopg2.connect(**db_config)

    cursor = connection.cursor()

    cursor.execute("CREATE DATABASE {}").format(sql.Identifier(new_db_name))

    connection.commit()
    print(f"PostgreSQL new database : {new_db_name}")

except Exception as e:
    print(f"Error: {e}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
    print("Database connection closed.")
    


###################################### w/ creation of SSL ##################################################

import psycopg2
from psycopg2 import sql


db_host = "your-db-hostname.com"
db_port = 5432
db_user = "your_username"
db_password = "your_password"
new_db_name = "my_secure_db"


ssl_mode = "verify-full"
ssl_root_cert = "/path/to/root.crt"
ssl_cert = "/path/to/client.crt"
ssl_key = "/path/to/client.key"

try:
    # Connect to default 'postgres' database to CREATE DATABASE
    conn = psycopg2.connect(
        dbname="postgres",
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port,
        sslmode=ssl_mode,
        sslrootcert=ssl_root_cert,
        sslcert=ssl_cert,
        sslkey=ssl_key
    )
    conn.autocommit = True  # Needed for CREATE DATABASE command

    cur = conn.cursor()
    cur.execute(sql.SQL("CREATE DATABASE {}").format(
        sql.Identifier(new_db_name)
    ))
    print(f"Database '{new_db_name}' created successfully over SSL!")

    cur.close()
    conn.close()

except psycopg2.Error as e:
    print("An error occurred:", e)