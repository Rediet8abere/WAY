from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from bson.objectid import ObjectId
from forms import RegistrationForm, LoginForm
from user import user

app = Flask(__name__)

app.config['SECRET_KEY'] = '820ca0568ea84a53bd886ecac1dbddc9'

@app.route('/')
def index():
    """Return homepage."""
    return render_template('index.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    """Create a new account."""
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if employees.find_one({"username": form.username.data}):
                flash(f'That account already exists')
                return redirect(url_for('index'))
            else:
                current_user = employees.insert_one(user(form.username.data, form.password.data, form.email.data).json())
                return redirect(url_for('index'))
        else:
            flash(f'Incorrect crednetials')
            return render_template('register.html', form=form)

    if request.method == 'GET':
        return render_template('register.html', form=form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    """Enables user to login"""
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if employees.find_one({"email": form.email.data}):
                if (form.email.data == employees.find_one({"email": form.email.data})["email"]) and (form.password.data == employees.find_one({"email": form.email.data})["password"]):
                    return redirect(url_for('show_companies'))
            else:
                flash(f'Log in unsuccessful. Please Check password and email', 'danger')
    return render_template('login.html', form=form)

    if request.method == 'GET':
        return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
