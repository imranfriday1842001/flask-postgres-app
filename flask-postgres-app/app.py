from flask import Flask
import os
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:postgres@db:5432/flask_db")

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT 'Hello from Dockerized PostgreSQL!'")
    result = cur.fetchone()[0]
    cur.close()
    conn.close()
    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

