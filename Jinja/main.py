from flask import Flask,render_template
''' 
    It create an instance of the flask class,
    which will be your WSGI(Web Server Gateway Interface) application
'''
##WSGI Application
app=Flask(__name__)     #entry point

@app.route("/")
def welcome():
    return "<html><H1>Let us focus on intergating HTML tags</H1></html>"

@app.route("/index")
def index():
    return render_template('index.html')  #It looks for index.html under templates folder
    ''' If index.html is not found it will through TemplateNotFound error in webpage'''

@app.route("/about")
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True)           #runs the entire app
