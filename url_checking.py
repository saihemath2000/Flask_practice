from flask import Flask,redirect,url_for 

app = Flask(__name__)

@app.route('/hello')
def myhello():
    return "Hello world!"

@app.route('/parameter/<arg>')
def myvarcharparameter(arg):
    return "My param is %s 🤞" % arg

@app.route('/parameter/<int:pa>')
def myintparameter(pa):
    return "My int param is %d" % pa

@app.route('/check/<type>')
def checking(type):
    if type=='varchar':
        return redirect(url_for('myvarcharparameter',arg=type))
    else:
        return redirect(url_for('myintparameter',pa=2)) 
    

if __name__=='__main__':
    app.run(debug=True) 