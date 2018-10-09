#!/usr/bin/env python3

from .orm import Database
from flask import Flask, render_template, redirect, url_for

def login(username,password):
    with Database('twitter.db') as db:
        db.cursor.execute("""SELECT password FROM users WHERE username=?;""",(username,))
        #remember password2 is a tuple with one object
        password2 = db.cursor.fetchone()
        if password2:
            if password == password2[0]:
                #TODO change redirect to url_for eventually
                return redirect(url_for('home.homepage'))
            #TODO login failure html has to be the login page with 'loginfailure' on it
            return render_template('login.html', test='Passwords do not match')
        return render_template('login.html', test='User does not exist')
