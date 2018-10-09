#!/usr/bin/env python3
from .orm import Database
from .friendlist import friends_list
from flask import session

def gen_dashboard():
    with Database('twitter.db') as db:
        username = session['username']
        friendslist = friends_list()
        db.cursor.execute("""SELECT * FROM content WHERE username=?;""",(username,))
        usercontent = db.cursor.fetchall()
        friend_content = []
        for all in friendslist:
            db.cursor.execute("""SELECT * FROM content WHERE username=?;""",(str(all[0]),))
            friend_content += db.cursor.fetchall()
        content = usercontent + friend_content
        return content

def grab_data(indy):
    with Database('twitter.db') as db:
        db.cursor.execute("""SELECT tweets FROM content WHERE pk=?;""",(indy,))
        twit = db.cursor.fetchone()[0]
        db.cursor.execute("""SELECT username FROM content WHERE pk=?;""",(indy,))
        user = db.cursor.fetchone()[0]
        return twit, user

