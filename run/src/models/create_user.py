#!/usr/bin/env python3
from .orm import Database
from flask import redirect, url_for

#TODO add a check to make sure it can't add duplicates


def create_login_admin(username,password):
    with Database('twitter.db') as db:
        db.cursor.execute("""INSERT INTO users(username,password) VALUES('{}','{}');""".format(username,password))
        return redirect(url_for('login.log_in'))

def create_login_nonadmin(username,password):
    with Database('twitter.db') as db:
        db.cursor.execute("""INSERT INTO users(username,password) VALUES('{}','{}');""".format(username,password))
        return redirect(url_for('login.log_in'))