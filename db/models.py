from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Materials(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Integer, nullable=False)


class Works(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    work_name = db.Column(db.String(150), nullable=False)
    costs = db.Column(db.Integer, nullable=False)

