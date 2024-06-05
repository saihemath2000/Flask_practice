from flask import Flask,redirect,url_for,render_template,request

app= Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method=="POST":
        data= request.form
        return render_template('result.html',data=data)

if __name__=='__main__':
    app.run(debug=True)    