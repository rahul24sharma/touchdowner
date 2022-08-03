from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea 
from flask_ckeditor import CKEditorField
from flask_wtf.file import FileField


#Create A Search Form
class SearchForm(FlaskForm):
    searched = StringField("Username", validators=[DataRequired()])
    submit = SubmitField("Submit")

#Create Login Form
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")
    
# Create a Posts Form
class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    #content = StringField("Content", validators=[DataRequired()], widget=TextArea())
    content = CKEditorField('Content',validators=[DataRequired()] )
    #author = StringField("Author")
    slug = StringField("Slug", validators=[DataRequired()])
    submit = SubmitField("Submit")
    
#Create a form class
class Userform(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    favorite_color = StringField("Favorite color")
    about_author = TextAreaField("About Author")
    password_hash = PasswordField('Password', validators=[DataRequired(), EqualTo('password_hash2', message='Passwords Must Match!')])
    password_hash2 =PasswordField('Confirm Password', validators=[DataRequired()])
    profile_pic = FileField("Profile Pic")
    submit = SubmitField("Submit")        
    
  #Create a form class
class Namerform(FlaskForm):
    name = StringField("What's your Name", validators=[DataRequired()])
    submit = SubmitField("Submit")
    
#Create a password_form class
class PasswordForm(FlaskForm):
    email = StringField("What's your Email", validators=[DataRequired()])
    password_hash = PasswordField("What's your Password", validators=[DataRequired()])
    submit = SubmitField("Submit")   