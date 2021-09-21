from bottle import post, get, put, delete
from bottle import route, run, template, static_file, request, response
from database.crud_db import inserting, updating, listing, deleting

@route('/')
def index():
    return template('static_files/home')

@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)

# @post('/insert')
@route('/insert')
def creation_handler():
    '''Handles name creation'''
    return template('static_files/insert')

@get('/list')
def listing_handler():
    '''Handles name listing'''
    result = listing()
    return template('static_files/list', rows=result)

# @put('/update')
@route('/update')
def update_handler():
    '''Handles name updates'''
    return template('static_files/update')

# @delete('/delete')
@route('/delete')
def delete_handler():
    '''Handles name deletions'''
    return template('static_files/delete')

run(host='localhost', port=8080, debug=True, reloader=True)