# -*- coding:utf-8 -*-
import os
from flask import render_template, flash, redirect, request, url_for
from flask.ext.login import login_user, login_required, logout_user, current_user
from app import app, login_manager
from app.models import User, Book, Author
from database import db_session
from forms import LoginForm, BookForm, AuthorForm, RegistrationForm, SearchForm


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@login_manager.unauthorized_handler
def unauthorized():
    flash("Login first.", 'danger')
    return redirect(url_for('index'))


@app.route('/')
def index():
    form = LoginForm()
    form_s = SearchForm()
    books = db_session.query(Book).all()
    return render_template("index.html", form=form, user=current_user, is_authenticated=current_user.is_authenticated(), books=books, form_s=form_s)


@app.route('/book/')
@login_required
def book():
    form = LoginForm()
    books = db_session.query(Book).all()
    return render_template("books.html", form=form, user=current_user, is_authenticated=True, books=books)


@app.route('/author/')
@login_required
def author():
    form = LoginForm()
    authors = db_session.query(Author).all()
    return render_template("authors.html", form=form, user=current_user, is_authenticated=True, authors=authors)


@app.route('/book/<id>', methods=['GET', 'POST'])
@login_required
def book_edit(id):
    form = LoginForm()
    book = db_session.query(Book).get(id)
    book_form = BookForm(request.form, obj=book)
    book_form.authors.choices = [(p.id, p.name) for p in db_session.query(Author).order_by('id')]

    if book_form.validate_on_submit():
        book = db_session.query(Book).get(id)
        book.title = book_form.title.data
        book.authors = [db_session.query(Author).get(o) for o in book_form.authors.data]
        db_session.commit()
        flash('Saved.', 'info')
        return redirect(url_for('index'))

    book_form.authors.data = [p.id for p in book.authors]
    return render_template("book.html", bform=book_form, form=form, book=book, user=current_user, is_authenticated=True)


@app.route('/book_add/', methods=['GET', 'POST'])
@login_required
def book_add():
    form = LoginForm()
    book_form = BookForm(request.form)
    book_form.authors.choices = [(p.id, p.name) for p in db_session.query(Author).order_by('id')]

    if book_form.validate_on_submit():
        book = Book()
        book.title = book_form.title.data
        book.authors = [db_session.query(Author).get(o) for o in book_form.authors.data]
        db_session.add(book)
        db_session.commit()
        flash('Successfully added.', 'success')
        return redirect(url_for('index'))

    return render_template("add_book.html", bform=book_form, form=form, user=current_user, is_authenticated=True)


@app.route('/book_rm/<id>', methods=['GET', 'POST'])
@login_required
def book_rm(id):
    book = db_session.query(Book).get(id)
    if book:
        db_session.delete(book)
        db_session.commit()
        flash('Deleted.', 'warning')
    return redirect(url_for('index'))


@app.route('/author/<id>', methods=['GET', 'POST'])
@login_required
def author_edit(id):
    form = LoginForm()
    author = db_session.query(Author).get(id)
    author_form = AuthorForm(request.form, obj=author)
    author_form.books.choices = [(p.id, p.title) for p in db_session.query(Book).order_by('id')]

    if author_form.validate_on_submit():
        author = db_session.query(Author).get(id)
        author.name = author_form.name.data
        author.books = [db_session.query(Book).get(o) for o in author_form.books.data]
        db_session.commit()
        flash('Saved.', 'info')
        return redirect(url_for('index'))

    author_form.books.data = [p.id for p in author.books]
    return render_template("author.html", bform=author_form, form=form, author=author, user=current_user, is_authenticated=True)


@app.route('/author_add/', methods=['GET', 'POST'])
@login_required
def author_add():
    form = LoginForm()
    author_form = AuthorForm(request.form)
    author_form.books.choices = [(p.id, p.title) for p in db_session.query(Book).order_by('id')]

    if author_form.validate_on_submit():
        author = Author()
        author.name = author_form.name.data
        author.books = [db_session.query(Book).get(o) for o in author_form.books.data]
        db_session.add(author)
        db_session.commit()
        flash('Successfully added.', 'success')
        return redirect(url_for('index'))

    return render_template("add_author.html", bform=author_form, form=form, user=current_user, is_authenticated=True)


@app.route('/author_rm/<id>', methods=['GET', 'POST'])
@login_required
def author_rm(id):
    author = db_session.query(Author).get(id)
    if author:
        db_session.delete(author)
        db_session.commit()
        flash('Deleted.', 'warning')
    return redirect(url_for('index'))


@login_required
@app.route('/logout/')
def logout():
    logout_user()
    flash("See you later.", 'info')
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = form.get_user()
        login_user(user)
        flash('Welcome ' + user.email, 'success')
        return redirect(request.args.get("next") or url_for("index"))
    return redirect(url_for("index"))


@app.route("/search/", methods=['GET', 'POST'])
def search():
    form = LoginForm()
    form_s = SearchForm()
    if form_s.validate_on_submit():
        q = form_s.search.data
        books = Book.query.all()
        authors = Author.query.all()
        result = []
        for book in books:
            if q in book.title:
                if not book in result:
                    result.append(book)
        for author in authors:
            if q in author.name:
                for b in author.books:
                    if not b in result:
                        result.append(b)
        return render_template('index.html', books=result, form=form, user=current_user,
                               is_authenticated=current_user.is_authenticated(), form_s=form_s,)

    return redirect(url_for('index'))


@app.route('/register/', methods=('GET', 'POST'))
def register_view():
    form_r = RegistrationForm()
    form = LoginForm()
    if form_r.validate_on_submit() and form_r.validate_login():
        user = User()
        user.name = form_r.name.data
        user.email = form_r.email.data
        user.password = form_r.password.data
        db_session.add(user)
        db_session.commit()
        if current_user.is_authenticated():
            logout_user()
        login_user(user)
        return redirect(url_for('index'))
    return render_template('register.html', form_r=form_r, form=form, user=current_user, is_authenticated=current_user.is_authenticated())



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
