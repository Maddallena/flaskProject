from app.extensions import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(1000), nullable=False)
    name = db.Column(db.String(1000), nullable=False)
    task_list = db.relationship('TaskList', backref='user', lazy=True)

    def __init__(self, email: str(100), password: str(1000), name: str(1000)):
        self.email = email
        self.password = password
        self.name = name

    def create(email, password, name):
        new_user = User(email, password, name)
        db.session.add(new_user)
        db.session.commit()



class TaskList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tasks = db.relationship('Task', backref='task_list', lazy=True)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    task_list_id = db.Column(db.Integer, db.ForeignKey('task_list.id'), nullable=False)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    video = db.Column(db.String(450))