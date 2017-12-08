from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, HiddenField, BooleanField
from wtforms.validators import Length, Email
from ..models import Role


class EditProfileForm(FlaskForm):
    username = StringField('Username', render_kw={'readonly': True})
    name = StringField('Real name', validators=[Length(1, 64)])
    email = StringField('Email', validators=[Email()])
    location = StringField('Location', validators=[Length(1, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')


class EditProfileAdminForm(FlaskForm):
    username = StringField('Username', render_kw={'readonly': True})
    role = SelectField('Role', coerce=int)
    name = StringField('Real name', validators=[Length(1, 64)])
    email = StringField('Email', validators=[Email()])
    location = StringField('Location', validators=[Length(1, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]


class EditProblemForm(FlaskForm):
    description = HiddenField('Description')
    input = HiddenField('Input')
    output = HiddenField('Output')
    sample_input = HiddenField('Sample input')
    sample_output = HiddenField('Sample output')


class SubmitProblemForm(FlaskForm):
    oj_name = HiddenField('OJ')
    problem_id = HiddenField('Problem')
    language = SelectField('Language')
    source_code = HiddenField('Source code')
    share = BooleanField('Share your code with others')
    submit = SubmitField('Submit')

    def __init__(self, language=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language.choices = language or []
