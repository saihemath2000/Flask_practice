from flask import Flask,session,request,redirect,url_for

app= Flask(__name__)
app.secret_key="SeyferAfram@143"

@app.route('/')
def index():
    if "username" in session:
        username= session['username']
        return 'Logged in as '+username+'<br>'+"<b><a href='/logout'>Click here to logout</a></b>"
    return 'You are not logged in '+"<b><a href='/login'>Click here to login</a></b>"

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        session['username']=request.form['username']
        return redirect(url_for('index'))
    return '''
            <form action = "" method = "post">
              <p><input type = text name = username /></p>
              <p><input type = submit value = Login /></p>
            </form>
           '''

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))           

if __name__=='__main__':
    app.run(debug=True)