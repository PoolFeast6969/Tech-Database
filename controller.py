from bottle import route, install, template, error, run, static_file, get, HTTP_CODES, request
import json, sqlite3

@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

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

@error(300)
def error_return(error):
        error = 300
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(301)
def error_return(error):
        error = 301
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(302)
def error_return(error):
        error = 302
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(303)
def error_return(error):
        error = 303
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(304)
def error_return(error):
        error = 304
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(305)
def error_return(error):
        error = 305
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(306)
def error_return(error):
        error = 306
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(307)
def error_return(error):
        error = 307
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(100)
def error_return(error):
        error = 100
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(101)
def error_return(error):
        error = 101
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(400)
def error_return(error):
        error = 400
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(401)
def error_return(error):
        error = 401
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(402)
def error_return(error):
        error = 402
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(403)
def error_return(error):
        error = 403
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(404)
def error_return(error):
        error = 404
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(405)
def error_return(error):
        error = 405
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(406)
def error_return(error):
        error = 406
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(407)
def error_return(error):
        error = 407
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(408)
def error_return(error):
        error = 408
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(409)
def error_return(error):
        error = 409
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(410)
def error_return(error):
        error = 410
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(411)
def error_return(error):
        error = 411
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(412)
def error_return(error):
        error = 412
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(413)
def error_return(error):
        error = 413
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(414)
def error_return(error):
        error = 414
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(415)
def error_return(error):
        error = 415
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(416)
def error_return(error):
        error = 416
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(417)
def error_return(error):
        error = 417
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(418)
def error_return(error):
        error = 418
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(428)
def error_return(error):
        error = 428
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(429)
def error_return(error):
        error = 429
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(431)
def error_return(error):
        error = 431
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(200)
def error_return(error):
        error = 200
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(201)
def error_return(error):
        error = 201
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(202)
def error_return(error):
        error = 202
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(203)
def error_return(error):
        error = 203
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(204)
def error_return(error):
        error = 204
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(205)
def error_return(error):
        error = 205
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(206)
def error_return(error):
        error = 206
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(500)
def error_return(error):
        error = 500
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(501)
def error_return(error):
        error = 501
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(502)
def error_return(error):
        error = 502
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(503)
def error_return(error):
        error = 503
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(504)
def error_return(error):
        error = 504
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(505)
def error_return(error):
        error = 505
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])
@error(511)
def error_return(error):
        error = 511
        return template('error.tpl', code=error, explanation=HTTP_CODES[error])

run(host='0.0.0.0', port=8080, debug=True, reloader=True)
