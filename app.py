from flask import Flask, request
from utils import *


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/generate-password/')
def generate_password():
    password_len = request.args.get("password-len", "10")
    if not password_len.isdigit():
        return "Error, password-len should be integer"

    password_len = int(password_len)

    if password_len > 100:
        return "Password should be less then 100"

    return generater_random_password(password_len)

@app.route('/requirements/')
def reading_file():
    return reading_requirements()

@app.route('/generate-users/')

def generate_users_list():
    users = request.args.get("users", "100")
    if not users.isdigit():
        return "Error, users should be integer"
    users = int(users)

    return generate_users(users)


if __name__ == "__main__":
    app.run(debug=True)
