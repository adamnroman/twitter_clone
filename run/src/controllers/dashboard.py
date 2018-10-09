from flask import Blueprint, render_template, request, session, abort

from ..models import dashboard
from ..models import tweet

controller = Blueprint('dashboard', __name__)

@controller.route('/dashboard', methods=['GET','POST'])
def dash_board():
    if 'username' in session:
        username = session['username']
        content = dashboard.gen_dashboard()
        if request.method == 'POST':
            twit = request.form['tweet']
            retwit_index = request.form['retweet']
            if retwit_index:
                twit, user = dashboard.grab_data(int(retwit_index))
                tweet.retweet(user, twit)
            else:
                tweet.tweet(twit)
            content = dashboard.gen_dashboard()
            return render_template('dashboard.html', content=content, section_title='Friend Activity!')
        else:
            return render_template('dashboard.html', content=content,section_title='Friend Activity!')
    else:
        abort(403)

