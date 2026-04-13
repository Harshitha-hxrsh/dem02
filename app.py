from flask import Flask, jsonify, gunicorn

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello World!",
        "status": "success",
        "status_code": 200
    })

@app.route('/welcome')
def welcome():
    return jsonify({
        "message": "Welcome to the Flask App 🚀",
        "status": "success",
        "status_code": 200
    })

@app.route('/about')
def about():
    return jsonify({
        "message": "This is a sample Flask API",
        "status": "success",
        "status_code": 200
    })

if __name__ == '__main__':
    app.run(debug=True)
