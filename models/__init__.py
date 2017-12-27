from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from models.light import Light
    db.drop_all()
    db.create_all()
