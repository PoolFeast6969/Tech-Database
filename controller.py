from bottle import route, install, template, error, run, static_file, get, HTTP_CODES, request
import sqlite3
import json
from bottle_sqlite import SQLitePlugin

install(SQLitePlugin(dbfile='glossary.db'))

@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@error(404)
def return_error(error):
    error=404
    return template('error.tpl', code=error, explanation=HTTP_CODES[error])

@route('/')
def load_page():
    return template('home.tpl')

@route('/', method='POST')
def send_database(db):
    cursor=db.execute('SELECT * FROM table_definitions')
    return json.dumps(cursor.fetchall())

run(host='localhost', port=8080, debug=True, reloader=True)
