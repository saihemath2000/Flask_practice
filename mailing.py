from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'saihemath2000@gmail.com'
app.config['MAIL_PASSWORD'] = 'qccmzhinmawmkjcv'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = 'saihemath2000@gmail.com'

@app.route("/")
def index():
    email = 'itssridhar2001@gmail.com'
    subject = "Hello from Flask-Mail"
    message = "This is a test email sent from a Flask application using Flask-Mail."
    msg = Message(subject, recipients=[email], body=message)
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
   app.run(debug = True)