#!/usr/bin/env python3

from .orm import Database

##This should generate the content for the homepage. User independent

def gen_homepage():
    with Database('twitter.db') as db:
        db.cursor.execute("""SELECT * FROM content;""")
        content = db.cursor.fetchall()
        return content