from datetime import datetime
from distutils import command

from alwaysHungry import db, login_manager
from sqlalchemy import orm
import enum
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    firstName = db.Column(db.String(30), nullable=False)
    lastName = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), unique=True)
    phoneNumber = db.Column(db.Integer, unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    transport = db.Column(db.Boolean, nullable=False)
    accountNumber = db.relationship("BankAccount", cascade="all, delete-orphan")
    services = db.relationship("Service", secondary="user_service")


class BankAccount(db.Model):
    accountNumber = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    balance = db.Column(db.Double)


class Category(enum.Enum):
    PAINTER = "painter"
    PLUMBER = "plumber"
    CATERER = "caterer"


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    user = db.relationship(User, secondary="user_service")
    category = db.Column(db.Enum(Category))


class UserService(db.Model):
    __tablename__ = 'user_service'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), primary_key=True)


class UserJob(db.Model):
    __tablename__ = 'user_job'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), primary_key=True)


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    user = db.relationship(User, secondary="user_service")
    category = db.Column(db.Enum(Category))
