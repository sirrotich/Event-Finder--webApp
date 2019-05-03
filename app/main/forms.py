from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):
    review = TextAreaField('Service Review',validators=[Required()])
    submit = SubmitField('submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class ProviderForm(FlaskForm):
    location = StringField("Where are you located?", validators = [Required()])
    company = StringField("Company name?")
    service = TextAreaField('What do you provide?')
    submit = SubmitField('Submit')