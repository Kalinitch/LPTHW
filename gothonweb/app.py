from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting = "Hello!"
    render = render_template('index.html', greet=greeting)
    return render

if __name__ == "__main__":
    app.run()
