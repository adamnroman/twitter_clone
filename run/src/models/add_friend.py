#!/usr/bin/env python3
from .orm import Database
from flask import session

def add_friend(friend):
    with Database('twitter.db') as db:
        username = session['username']
        db.cursor.execute("""INSERT INTO friends(username,friend) 
                    VALUES(?,?);""",(username, friend)
        )
        db.cursor.execute("""INSERT INTO friends(username,friend) 
                    VALUES(?,?);""",(friend, username)
        )