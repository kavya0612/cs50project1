from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
   
"""
    def add_user(user_name,password):
        u = User(name=user_name,password=password)
        db.session.add(user)
        db.session.commit()
        return user 
"""