import psycopg2
import ssl

db_config = {
    "host": "172.17.0.2",  
    "port": 5432,          
    "database": "mydb",    
    "user": "myuser",      
    "password": "mypassword",
    "sslmode": "verify-full",
    "sslrootcert": "ssl/ca.crt"
}

try:
    print("Connecting to the PostgreSQL database...")
    connection = psycopg2.connect(**db_config)

    cursor = connection.cursor()

    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"PostgreSQL database version: {db_version}")

except Exception as e:
    print(f"Error: {e}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
    print("Database connection closed.")
    
