from src.models import db, users
from werkzeug.security import generate_password_hash, check_password_hash



class usernameRepository:

    def get_all_users(self):
        all_users = users.query.all()
        return all_users

    def get_user_by_email(self, user_email):
        return users.query.get(user_email)

    def get_user_by_id(self, user_id):
        return users.query.get(user_id)

    def create_user(self, userName, user_password, firstName, lastName, user_email, user_phone_number):
        hashed_password = generate_password_hash(user_password)
        created_user = users(
            userName=userName, user_password=hashed_password,
            firstName=firstName, lastName=lastName,
            user_email=user_email, user_phone_number=user_phone_number
        )

        db.session.add(created_user)
        db.session.commit()

        return created_user

    def get_user_password(self, user_password):

        return users.query.get(user_password)

    def login(self, userName, user_password):
        user = users.query.filter_by(userName=userName).first()
        if user and check_password_hash(user.user_password, user_password):
            return user
        return None
    # Survey functions


    # Allows the code to be used in other modules
users_repository_singleton = usernameRepository()