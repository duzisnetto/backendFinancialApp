from brain import app
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager


login = LoginManager(app)


@login.user_loader
def load_user(id):
    return User.objects.get(id=id)

class User(UserMixin, db.Document):
    meta = {'collection': 'users'}
    name = db.StringField(default=True)
    sobrenome = db.StringField(default=True)
    email = db.EmailField(unique=True)
    password_hash = db.StringField(default=True)
    active = db.BooleanField(default=True)
    isAdmin = db.BooleanField(default=False)
    isCliente = db.BooleanField(default=False)
    isMaster = db.BooleanField(default=False)
    isConsultor = db.BooleanField(default=False)
    dataCriacao = db.DateTimeField(default=datetime.now())
    ultima_atividade = db.DateTimeField(default=datetime.now())
    familia_id = db.IntegerField(default=0)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)