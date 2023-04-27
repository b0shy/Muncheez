from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(255), primary_key=False)
    user_password = db.Column(db.String(255), primary_key=False)
    firstName = db.Column(db.String(255), primary_key=False)
    lastName = db.Column(db.String(255), primary_key=False)
    user_email = db.Column(db.String(255), primary_key=False)
    user_phone_number = db.Column(db.String(10), primary_key=False)