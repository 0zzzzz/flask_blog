from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from oz_blog.config import Config
from flask_bcrypt import Bcrypt
from flask_mail import Mail

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from oz_blog.main.routes import main
    from oz_blog.users.routes import users
    from oz_blog.posts.routes import posts
    from oz_blog.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(errors)
    mail.init_app(app)

    return app
