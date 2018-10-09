#!/usr/bin/env python3

from .orm import Database
import time
from flask import session

def tweet(twit):
    with Database('twitter.db') as db:
        username = session['username']
        localtime = time.asctime(time.localtime(time.time()))
        db.cursor.execute("""INSERT INTO content(username,tweets,retweet,time)
                        VALUES(?,?,0,?);""",(username,twit,str(localtime))
        )

def retweet(user,twit):
    with Database('twitter.db') as db:
        username = session['username']
        localtime = time.asctime(time.localtime(time.time()))
        user = "-" + user
        twit += user
        db.cursor.execute("""INSERT INTO content(username,tweets,retweet,time)
                        VALUES(?,?,1,?);""",(username,twit,str(localtime))
        )