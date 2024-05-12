from flask import Flask, render_template
import psycopg2
from config import host, user, password, db_name
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

def get_db_connection():
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    # conn = get_db_connection()
    # with conn.cursor() as cursor:
    #     cursor.execute('')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=3001)
