import os
from flask import Flask

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def hello(): 
    return 'Hello ya bas!'


@app.route('/<name>')
def name(name): 
    return f'Hello {name} ya fanny'


if __name__ == '__main__':
    app.run()
    print(os.environ['APP_SETTINGS'])
