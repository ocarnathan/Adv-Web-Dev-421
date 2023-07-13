from flask import Flask, render_template, request
app = Flask (__name__)

@app.route('/')
def index ():
    return render_template ('index.html')

@app.route('/report')
def report():
    UserName = request.args.get('UserName')
    Password = request.args.get('Password')
    return render_template('report.html' ,UserName=UserName,Password=Password)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run()

#home page or domain is locally represented as http://127.0.0.1:5000/
# to create multiple pages we will use decorators;
#  @app.route("/another-page")