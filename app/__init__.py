# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'music-rec-2025'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Import & register blueprint DI DALAM fungsi (hindari circular import)
    from app.routes.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app