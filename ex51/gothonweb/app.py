from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def hello_post():
    usergreet = request.form.get('greet')
    username = request.form.get('name')
    if usergreet is None or usergreet == "":
        usergreet = "Hello"
    if username is None or username == "":
        username = "Nobody"
    greeting = "%s, %s!" % (usergreet, username)
    return render_template('index.html', greet=greeting)

@app.route('/hello', methods=['GET'])
def hello_get():
    return render_template('hello_form.html')

if __name__ == "__main__":
    app.run()
