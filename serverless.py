from bottle import route, run, template

@route('/')
def index():
    return '<h1>Welcome!</h1>'

@route('/hello/<name>')
def hello(name):
    return template('<h1>Welcome!</h1><br><b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)