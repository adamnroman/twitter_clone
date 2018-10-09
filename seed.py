from run.src.models.orm import Database

with Database('twitter.db') as db:
    db.cursor.execute("""INSERT INTO content(username,tweets,retweet,time)
                    VALUES('adam','yo sup', 0, 'Oct 5 1999');"""
    )
    db.cursor.execute("""INSERT INTO content(username,tweets,retweet,time)
                    VALUES('jonathan','yo sup -adam', 1, 'Oct 6 1999');"""
    )
    db.cursor.execute("""INSERT INTO users(username,password)
                    VALUES('adam','password');"""
    )
    db.cursor.execute("""INSERT INTO users(username,password)
                    VALUES('jonathan','password');"""
    )
    db.cursor.execute("""INSERT INTO friends(username,friend)
                    VALUES('adam','jonathan');"""
    )
    db.cursor.execute("""INSERT INTO friends(username,friend)
                    VALUES('jonathan','adam');"""
    )
