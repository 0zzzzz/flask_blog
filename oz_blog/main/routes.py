from flask import render_template, Blueprint
from oz_blog.models import User

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    """Главная страница"""
    return render_template('home.html')
