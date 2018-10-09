#!/usr/bin/env python3

from .orm import Database
from flask import session

def friends_list():
    with Database('twitter.db') as db:
        username = session['username']
        db.cursor.execute("""SELECT friend FROM friends WHERE username=?;""",(username,))
        friends_list = db.cursor.fetchall()
        return friends_list