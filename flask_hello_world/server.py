from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)
@app.route("/")
@app.route("/alex")
def hello():
    return "Hello World, Alex!"

if __name__ == '__main__':

    manager.run()