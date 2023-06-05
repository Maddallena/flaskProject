from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.main import bp
from app.extensions import db
from app.models import User, TaskList, Task


@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/login')
def login():
    return render_template('login.html')


@bp.route('/login',  methods=['GET', 'POST'])
def login_post():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(email=email).first()

        if not user:
            flash('Please check your login details and try again.')
            return render_template('index.html')
    login_user(user, remember=remember)
    return render_template('profile.html')

@bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@bp.route('/signup')
def signup():
    return render_template('signup.html')

@bp.route('/signup', methods=['GET', 'POST'])
def signup_post():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')
        user = User.create(email, password, name)

        if user is not None:
            return render_template('templates/signup.html')
        else:
            flash('Email address already exists')

    return render_template('index.html')

@bp.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)






