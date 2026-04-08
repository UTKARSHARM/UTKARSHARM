import mysql.connector
import pandas as pd

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Streampulse"
    )

def run_query(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df