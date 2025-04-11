import psycopg2

db_config = {
    "host": "<private-endpoint-hostname>",  
    "port": 5432,                          
    "database": "<database-name>",         
    "user": "<username>",                  
    "password": "<password>",              
    "sslmode": "verify-full",              
    "sslrootcert": "ca-certificate.crt"    
}

create_tables_queries = [
    """
    CREATE TABLE IF NOT EXISTS users (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS products (
        product_id SERIAL PRIMARY KEY,
        product_name VARCHAR(100) NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        stock INT DEFAULT 0
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS orders (
        order_id SERIAL PRIMARY KEY,
        user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
        product_id INT REFERENCES products(product_id) ON DELETE CASCADE,
        quantity INT NOT NULL,
        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
]

try:
    print("Connecting to the PostgreSQL database...")
    connection = psycopg2.connect(**db_config)

    cursor = connection.cursor()

    for query in create_tables_queries:
        cursor.execute(query)
        print(f"Executed query: {query.splitlines()[0]}")  # Print the first line of the query for clarity

    connection.commit()
    print("Tables created successfully.")

except Exception as e:
    print(f"Error: {e}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
    print("Database connection closed.")