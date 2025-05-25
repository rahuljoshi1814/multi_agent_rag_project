import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="Rj database",
        user="postgres",
        password="Rahul@2309",
        host="localhost",
        port="5432"
    )
