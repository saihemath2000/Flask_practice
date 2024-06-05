from flask import Flask, session, request, redirect, url_for, flash, render_template

app = Flask(__name__)
app.secret_key = "SeyferAfram@143"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        flash("You are successfully logged in")
        return redirect(url_for('index'))
    return '''
            <form action = "" method = "post">
              <p><input type = text name = username /></p>
              <p><input type = submit value = Login /></p>
            </form>
           '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
