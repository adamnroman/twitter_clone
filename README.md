# twitter_clone:
# Using Flask this repository deploys a web application that allows users to send messages to all users and user friends.
# To repost messages you have to input the index number because I thought it looked cleaner than having a repost button next 
# to each message even though it was a bit less intuitive.

# I built this application as a platform that my friends could use to send messages to each other without having to have that
# information accessible by the public through commonly used social media.

# SECURITY:
# I used firewalld on my virtual server to prevent most security risks with only a single open port. 

# SRC:
# HTML, CSS, and Javascript is sourced from Bootstrap with some Jinja2 templating. I used flask blueprints for each page for
# organizational purposes and for possible reusability in the future if I wish to make a more complex web application.
# For function calls I used relative imports because the names of the directories are subject to change, but I had no plan to 
# change the structure of the application. Some developers discourage relative imports, but in this situation I think it was
# preferable.
