import psycopg2
import ssl

try:
    conn = psycopg2.connect(
        host="<your-db-host.com>",
        port=5432,
        dbname="postgres",
        user="<your_admin_user>",
        password="<your_password>",
        sslmode="require",
        sslrootcert="ssl/ca.crt"
    )
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("CREATE DATABASE analytics_db;")
    print("Database created successfully")

    cur.close()
    conn.close()
    print("Connection closed securely")

except Exception as e:
    print("Error during database creation: ", e)