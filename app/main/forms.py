from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [Required()])
    submit = SubmitField('Submit')

class ServiceForm(FlaskForm):
    title = StringField('Blog Title')
    topic = StringField('Topic')
    content = TextAreaField('Blog Content')
    submit = SubmitField('Submit')

class ReviewForm(FlaskForm):

    comment = TextAreaField('Comment')
    submit = SubmitField('Post Comments')