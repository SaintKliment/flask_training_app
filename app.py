from flask import Flask, render_template, request, redirect, url_for
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
    conn = get_db_connection()
    conn.autocommit = True
    if request.method == 'POST':
        form = request.form
        name = form['name']
        email = form['email']
        with conn.cursor() as cursor:
            cursor.execute('INSERT INTO user_logins(name, email) VALUES(%s, %s)', (name, email))

    return render_template('index.html')

# @app.route('/employees')
# def employees():
#     conn = get_db_connection()
#     conn.autocommit = True
#     with conn.cursor() as cursor:
#             cursor.execute("SELECT * FROM employee")
#             employees = cursor.fetchall()
            
#     print(employees)
#     return render_template('employees.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True, port=3001)
