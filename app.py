from flask import Flask, abort, redirect, render_template, request, session
from src.models import db
from src.repositories.username_repository import users_repository_singleton


app = Flask(__name__)
app.secret_key = 'cool-guy'


# TODO: DB connection
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql://root:password!@localhost:3306/furfinder'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# gets the homepage


@app.get('/')
def index():
    return render_template('index.html')

# sends the user to the create user form


@app.get('/users/new')
def create_new_user_form():
    return render_template('signup.html')


# directs the user to the homepage given there user id
@app.get('/users/<int:user_id>/home')
def user_home(user_id):
    user = users_repository_singleton.get_user_by_id(user_id)
    return render_template('userProfile.html', user=user)


# creates user and stores it in database
@app.post('/users')
def create_user():
    username = request.form.get('username', '')
    user_password = request.form.get('user_password', '')
    firstName = request.form.get('firstName', '')
    lastName = request.form.get('lastName', '')
    user_email = request.form.get('user_email', '')
    user_phone_number = request.form.get('user_phone_number', ' ')
    if username == '' or firstName == '' or lastName == '' or user_email == '' or user_password == '' or user_phone_number == '':
        abort(400)

    user = users_repository_singleton.create_user(
        username, user_password, firstName, lastName, user_email, user_phone_number)

    session['user_id'] = user.user_id

    return redirect(f'/users/{user.user_id}/newSurvey')



if __name__ == '__main__':
    app.run(debug=True)