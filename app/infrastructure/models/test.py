from app import db


class Test(db.Model):
    __tablename__ = "test"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=True)
