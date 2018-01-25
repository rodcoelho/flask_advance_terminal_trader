from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import acl as USER

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database/database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Customer(db.Model):
    __tablename__ = 'customers'
    pk = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    role = db.Column(db.SmallInteger, default=USER.USER)
    status = db.Column(db.SmallInteger, default=USER.NEW)

    def __init__(self, username = None, password = None, email=None):
        self.username=username
        self.password=password
        self.email=email

    def status(self):
        return USER.STATUS[self.status]

    def role(self):
        return USER.ROLE[self.role]

    def __repr__(self):
        return "<Customer %r>" % (self.username)

if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    first_customer = Customer("rodrigo", 'swordfish', 'rawduh@gmail.com')
    db.session.add(first_customer)
    db.session.commit()
