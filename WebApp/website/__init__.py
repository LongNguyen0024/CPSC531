from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
dbName = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{dbName}'
    
    db.init_app(app)
    db.create_all(app=app)
    print('Database Created!')
    
    
    from .views import views
    from .models import User

    app.register_blueprint(views, url_prefix='/')

    
    login_manager = LoginManager()
    login_manager.login_view = 'views.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return views
