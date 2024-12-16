from flask import Flask,request,make_response
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/about')
def about():
    return 'This is the About Page.'

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    return f'Hello, {username}!'

@app.route('/custom_response')
def custom_response():
    response = make_response('This is a custom response!')
    response.headers['X-Custom-Header'] = 'Value'
    return response

if __name__ == "__main__":
    app.run(debug=True)