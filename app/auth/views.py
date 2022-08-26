from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user
from . import auth
from ..models import User
from .forms import LogInForm


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_name=form.user_name.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.home')
            return redirect(next)
        flash('Username or password incorrect')
    return render_template('auth/login.html', form=form)