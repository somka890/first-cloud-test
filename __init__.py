from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, template_folder='../templates')

    app.config['SECRET_KEY'] = 'labai-slapta-raktis'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/demo.db'


    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    from .models import Vartotojas

    @login_manager.user_loader
    def load_user(user_id):
        return Vartotojas.query.get(int(user_id))

    from .routes import main
    app.register_blueprint(main)

    return app
