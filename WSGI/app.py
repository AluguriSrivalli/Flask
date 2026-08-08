from flask import Flask
''' 
    It create an instance of the flask class,
    which will be your WSGI(Web Server Gateway Interface) application
'''
##WSGI Application
app=Flask(__name__)     #entry point

@app.route("/")
def welcome():
    return "This is my home page."

@app.route("/second/")
def welcome_second():
    return "This is my second page"

@app.route("/debugger")
def debugger():
    return "When debug=True is set in run(), We can validate changes while developing without restarting the server everytime."

if __name__=="__main__":
    app.run(debug=True)           #runs the entire app
