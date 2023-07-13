#home page or domain is locally represented as http://127.0.0.1:5000/
# to create multiple pages we will use decorators;
#  @app.route("/another-page")

# to access this page we will use;
#  http://127.0.0.1:5000/another-page
from flask import Flask
app = Flask (__name__)

@app.route ('/')
def index():
    return '<h1> Hello World! </h1>'

@app.route('/contact-us')
def info():
    return "<h2> Contact Us </h2>" # http://127.0.0.1:5000/contact-us

# below is an example of how profile pages are set up
@app.route ('/users/<username>')
def userprofile(username):
    return "<h3> This is a profile page for {}</h3>" .format(username.upper()) # http://127.0.0.1:5000/users/<username>

# @app.route ('/users/<username>')
# def userprofile(username):
#     return "6th character of your name is ={}" .format(username[5]) # http://127.0.0.1:5000/users/<username>


# username update excercise below
# @app.route ('/users/<username>')
# def userprofile(username):

#     if username[-1] == 'y':
#         usernamemod = username[:-1] + 'iful' 
#         return "Your real name is :{} and your latin name is:{} " .format(username, usernamemod) # http://127.0.0.1:5000/users/<username>
#     else:
#         usernamemod = username + 'y'
#         return "Your real name is :{} and your latin name is:{}" .format(username, usernamemod)

if __name__ == '__main__':
    app.run()

# code below used to enable debugging
# make sure debugging is turned back off before publishing
# debugging instructions in wk 6 debugging video at 3 min mark
# if __name__ == '__main__':
#     app.run(debug=True)