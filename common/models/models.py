from app import db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text)
    password = db.Column(db.Text)
    screen_name = db.Column(db.Text)
    access_token = db.Column(db.Text)
    access_secret = db.Column(db.Text)
