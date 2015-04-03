from bottle import route, install, template, error, run
import sqlite3
from bottle_sqlite import SQLitePlugin

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='/static/')

@route('/')
def retrieve_data():
    return template('home.tpl')

@route('/', method='POST')
def get_ajax():
    username = request.forms.get('username')

@error(404)
def errors(error):
    return template('error.tpl', error=code)

run(host='0.0.0.0', port=8080, debug=True, reloader=True)
