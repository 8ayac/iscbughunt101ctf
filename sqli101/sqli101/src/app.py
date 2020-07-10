import os

import MySQLdb
from flask import abort, redirect, render_template, request, session
from flask import Flask, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.secret_key = os.environ.get('SECRET_KEY')  # to use session


@app.route('/', methods=['GET'])
def get_index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def post_login():
    password = request.form['password']
    if is_admin(password):
        session['flag'] = os.environ.get('FLAG')
        return redirect(url_for('get_admin'))
    else:
        return redirect(url_for('get_index'))


@app.route('/admin', methods=['GET'])
def get_admin():
    try:
        return render_template('flag.html', flag=session['flag'])
    except:
        return redirect(url_for('get_index'))


@app.route('/logout', methods=['GET'])
def get_logout():
    session.pop('flag', None)
    return redirect(url_for('get_index'))


def is_admin(pw: str) -> bool:
    conn = MySQLdb.connect(
        host='db',
        user=os.environ.get('MYSQL_USER'),
        passwd=os.environ.get('MYSQL_PASSWORD'),
        db=os.environ.get('MYSQL_DATABASE')
    )
    cursor = conn.cursor()

    try:
        stmt = f'SELECT * FROM users WHERE username="admin" AND password="{pw}";'
        cursor.execute(stmt)
    except MySQLdb.Error as e:
        abort(500, description=repr(e))
    finally:
        conn.close()

    return cursor.rowcount > 0


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', code=500, msg=e.description)


if __name__ == '__main__':
    app.run()
