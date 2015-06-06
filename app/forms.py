from flask import flash
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, SelectMultipleField, widgets
from wtforms.validators import Required, Length
from app.models import User
from database import db_session
from wtforms import validators


class LoginForm(Form):
    email = TextField('email', validators=[validators.required(), validators.Email()])
    password = PasswordField('password', validators=[validators.required()])

    def get_user(self):
        return db_session.query(User).filter_by(email=self.email.data).first()


class BookForm(Form):
    title = TextField('title', validators=[Required(), Length(1, 200)])
    authors = SelectMultipleField('authors', coerce=int, widget=widgets.ListWidget(prefix_label=False),
                                  option_widget=widgets.CheckboxInput()) 


class AuthorForm(Form):
    name = TextField('name', validators=[Required(), Length(1, 200)])
    books = SelectMultipleField('books', coerce=int, widget=widgets.ListWidget(prefix_label=False),
                                option_widget=widgets.CheckboxInput())


class RegistrationForm(Form):
    name = TextField('name', validators=[validators.required(), Length(4, 50)])
    email = TextField('email', validators=[validators.required(), validators.Email(), Length(max=50)])
    password = PasswordField('password', validators=[validators.required(), Length(max=50)])

    def validate_login(self):
        if db_session.query(User).filter_by(email=self.email.data).count() > 0:
            flash('Duplicate email', 'danger')
            return False
        if db_session.query(User).filter_by(name=self.name.data).count() > 0:
            flash('Duplicate name', 'danger')
            return False
        return True


class SearchForm(Form):
    search = TextField('search', validators = [Required()])


