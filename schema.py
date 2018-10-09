from run.src.models.orm import Database

with Database('twitter.db') as db:
    db.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                      pk INTEGER PRIMARY KEY AUTOINCREMENT,
                      username VARCHAR,
                      password VARCHAR
                      );"""
    )
    db.cursor.execute("""CREATE TABLE IF NOT EXISTS content(
                      pk INTEGER PRIMARY KEY AUTOINCREMENT,
                      username VARCHAR,
                      tweets VARCHAR,
                      retweet BOOL,
                      time VARCHAR
                      );"""
    )
    db.cursor.execute("""CREATE TABLE IF NOT EXISTS friends(
                      pk INTEGER PRIMARY KEY AUTOINCREMENT,
                      username VARCHAR,
                      friend VARCHAR
                      );"""
    )
