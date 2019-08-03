from flask import Blueprint
from flask import Flask, render_template

userManagment = Blueprint('users', __name__)


@userManagment.route('/home')
def register():
    return render_template('Register.html')
