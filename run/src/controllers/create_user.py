from flask import Blueprint, render_template, request
from ..models import create_user

controller = Blueprint('create_user',__name__)

@controller.route('/create_user', methods=['GET','POST'])
def newUser():
    if request.method == 'POST':
        #TODO stuff
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']
        checkbox = request.form.get('admin')
        if password==password2:
            if checkbox:
                return create_user.create_login_admin(username,password)
            else:
                return create_user.create_login_nonadmin(username,password)
        else:
            return render_template('create_user.html',test='Passwords do not match')
            
    else:
        return render_template('create_user.html')