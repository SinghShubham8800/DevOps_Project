import os
import psycopg2
import time
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    # This loop gives the database 10 seconds to start up
    for i in range(5):
        try:
            conn = psycopg2.connect(
                host='db',
                database='myapp',
                user='user',
                password='password'
            )
            return conn
        except psycopg2.OperationalError:
            print(f"Database not ready, retrying... ({i+1}/5)")
            time.sleep(2)
    raise Exception("Could not connect to the database")

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return render_template('index.html', db_version=db_version)
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
