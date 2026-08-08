###Building URL dynamically
##Variable rule
###Jinja2 Template engine
'''
{{ }} expressions to print output in html
{%.....%} conditions, for loops
{#.....#} this is for comments
'''

from flask import Flask,render_template,request,redirect,url_for
''' 
    It create an instance of the flask class,
    which will be your WSGI(Web Server Gateway Interface) application
'''
##WSGI Application
app=Flask(__name__)     #entry point

@app.route("/")
def welcome():
    return "<html><H1>Let us focus on intergating HTML tags</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')  #It looks for index.html under templates folder
    ''' If index.html is not found it will through TemplateNotFound error in webpage'''

@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}'
    return render_template('form.html')

@app.route('/success/<int:score>')   #variable rule: restricting parameter to one particular rule
def success(score):
    return "The marks you got is "+ str(score)

@app.route('/success_story/<int:score>')   #variable rule: restricting parameter to one particular rule
def success_story(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    return render_template('result.html',results=res)

@app.route('/success_result/<int:score>')   #variable rule: restricting parameter to one particular rule
def success_result(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    exp={'score':score,"res":res}
    return render_template('result1.html',results=exp)

##if condition
@app.route('/successif/<int:score>')   #variable rule: restricting parameter to one particular rule
def successif(score):
    return render_template('result.html',results=score)   

@app.route('/fail/<int:score>')   #variable rule: restricting parameter to one particular rule
def fail(score):

    return render_template('result.html',results=score)

@app.route('/getresults',methods=['GET','POST'])
def getreults():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['Maths'])
        C=float(request.form['C'])
        datascience=float(request.form['datascience'])

        total_score=(science+maths+C+datascience)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('success_result',score=total_score))

@app.route("/about")
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True)           #runs the entire app