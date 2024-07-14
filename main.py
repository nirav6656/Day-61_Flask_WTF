from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.config['SECRET_KEY'] = "my secret key"

def is_8(form, field):
    if len(field.data) < 8:
        raise ValidationError('Must be 8')
class Form(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[is_8])
    submit = SubmitField("Log In")





@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login",methods = ['GET','POST'])
def login():
    email = None
    submit = None
    password = None
    form = Form()
    if form.validate_on_submit():
        email = form.email.data
        form.email.data = ''
    return render_template('login.html', email=email,submit = submit, password = password,form=form)



@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404

if __name__ == '__main__':
    app.run(debug=True)
