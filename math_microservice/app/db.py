from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    with app.app_context():
        from app.models import MathRequest  # Import aici pentru a evita circular import
        db.create_all()
