import os
import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    # 'db' is the hostname defined in docker-compose
    conn = psycopg2.connect(host='db',
                            database='myapp',
                            user='user',
                            password='password')
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT version();')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return render_template('index.html', db_version=db_version)
