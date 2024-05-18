# controller.py
from flask import Flask, render_template, request, session, redirect, url_for
from service import signup, login

app = Flask(__name__)
app.secret_key = '$T@2023'

@app.route("/")
def display_page():
    return render_template('authentification.html')

@app.route("/data")
def display_first_page():
    return render_template('index.html')

@app.route("/signup", methods=['POST'])
def handle_signup():
    email = request.form['email']
    password = request.form['password']
    user_id = signup(email, password)
    if user_id:
        session['user_id'] = str(user_id)
        return redirect(url_for('display_first_page'))
    else:
        return render_template('authentification.html', error='Email already exists')

@app.route("/login", methods=['POST'])
def handle_login():
    email = request.form['email']
    password = request.form['password']
    user = login(email, password)
    if user:
        session['user_id'] = str(user['_id'])
        return redirect(url_for('display_first_page'))
    else:
        return render_template('authentification.html', error='Invalid email or password')

if __name__ == '__main__':
    app.run(debug=True)