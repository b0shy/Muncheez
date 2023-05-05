from flask import Flask, abort, redirect, render_template, request, session
from src.models import db
from src.repositories.username_repository import users_repository_singleton


app = Flask(__name__)
app.secret_key = 'cool-guy'


# TODO: DB connection
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql://root:password@localhost:3306/muncheez'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# gets the homepage
@app.get('/')
def index():
    return render_template('index.html')

#Renders Forum page
@app.route('/forum')
def forum():
    return render_template('forum.html')

#Renders Add Post page
@app.route('/add_post')
def add_post():
    return render_template('add_post.html')

# sends the user to the create user form

#gets the sign up page 
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

    return redirect(f'/nearYou')

#shows all the restaurants
@app.get('/allRestaurant')
def get_all_Restaurant():
    return render_template('restaurant_list.html')

#shows the food near you page
@app.get('/nearYou')
def get_near_You():
    return render_template('near_you.html')


#shows the features page
@app.get('/features')
def get_features():
    return render_template('features.html')

#shows the features page
@app.get('/about')
def get_about():
    return render_template('about.html')

#shows the features page
@app.get('/contact')
def get_contact():
    return render_template('contact.html')

#logs the user in and redirects them to the restaurant page 
@app.post('/login')
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    user = users_repository_singleton.login(username, password)

    if user:
        return redirect(f'/nearYou')
    else:
        return render_template('index.html', error='Invalid Username or Password')
    





if __name__ == '__main__':
    app.run(debug=True)