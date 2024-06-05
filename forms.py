from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,RadioField,SubmitField,TextAreaField,SelectField,ValidationError,validators

class ContactForm(FlaskForm):
    name = StringField('Name of student',[validators.DataRequired("please enter ur name")])
    gender = RadioField('Gender',choices=[('M','Male'),('F','Female')])
    Address= TextAreaField('Address')
    email = StringField('Email',[validators.DataRequired("please enter ur email address"),validators.Email("please enter ur email addr")])
    Age = IntegerField('age')
    language = SelectField('Languages',choices=[('cpp','c++'),('py','python')])
    submit = SubmitField('send')