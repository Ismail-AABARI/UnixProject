# service.py
from dal import get_user_by_email, create_user
from flask_bcrypt import Bcrypt
from modele import Account

bcrypt = Bcrypt()

def signup(email, password):
    existing_user = get_user_by_email(email)
    if existing_user:
        return None

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = Account(email=email, password=hashed_password)
    user_id = create_user(user.__dict__)
    return user_id

def login(email, password):
    user = get_user_by_email(email)
    if not user:
        return None

    if bcrypt.check_password_hash(user['password'], password):
        return user
    else:
        return None