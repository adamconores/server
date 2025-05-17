from flask import Flask, render_template, request, redirect, session
import models
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET' and 'username' in request.args:
        username = request.args.get('username')
        password = request.args.get('password')
        if models.loginUser(username, password):
            session['username'] = username
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html', error=None)

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
