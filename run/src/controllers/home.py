#!/usr/bin/env python3

from flask import Blueprint, render_template, url_for, request, abort, session
from ..models import home
from ..models import add_friend
controller = Blueprint('home', __name__)

@controller.route('/homepage', methods=['GET','POST'])
def homepage():
    if 'username' in session:
        if request.method == 'POST':
            friend = request.form['add_friend']
            add_friend.add_friend(friend)
            content = home.gen_homepage()
            return render_template('homepage.html', username=session['username'], content=content, section_title='You have friends!')
        else:
            content = home.gen_homepage()
            return render_template('homepage.html', username=session['username'], content=content, section_title='World Activity')
    else:
        abort(403)