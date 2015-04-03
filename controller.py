import bottle, sqlite3, bottle_sqlite

install(SQLitePlugin(dbfile='glossary.db'))

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='/static/')

@route('/')
def retrieve_data():
    db.execute('SELECT * FROM posts WHERE id = ?')

@route('/', method='POST')
def get_ajax():
    username = request.forms.get('username')

@error('*')
def errors(error):
    return template('error.tpl', error=code)
