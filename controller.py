from bottle import route, install, template, error, run, static_file, get, HTTP_CODES, request
import json, sqlite3

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
def send_database():
    connection = sqlite3.connect("glossary.db")
    connection.row_factory = dict_factory
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM table_definitions")
    return json.dumps(cursor.fetchall())

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

run(host='localhost', port=8080, debug=True, reloader=True)
