from flask import Blueprint, flash, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
  
    if request.method == 'POST':
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(username) < 4 or len(username) > 20:
            flash('Username must be 4-20 characters.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
            
    return render_template("sign_up.html")