from flask import Flask, abort

app= Flask(__name__)

@app.route('/')
def two_hundred():
    return "200! Success"

@app.route('/error')
def error():
    abort(500, 'here is some error')

if __name__ == "__main__":
    app.run(debug = True, port = 8000, host = "0.0.0.0")

