from flask import Flask

tasks = [
    'ir pro medico', 
    'fazer feira'
]
usuario = 'luanda'

app_flask = Flask(__name__)

@app_flask.route('/')
def index():
    return "Oi, Mundo!"

@app_flask.route('/usuario')
def get_usuario():
    return usuario

if __name__ == '__main__':
    app_flask.run()