from flask import Blueprint, render_template, redirect, request, session
from ..models import login

controller = Blueprint('login',__name__)

@controller.route('/login', methods=['GET','POST'])
def log_in():
    if request.method == 'POST':
        session['username'] = request.form['username']
        password = request.form['password']
        #TODO dont forget to go into models login file to change route
        return login.login(session['username'],password) ## calls function from models folder that returns render template
    return render_template('login.html') 