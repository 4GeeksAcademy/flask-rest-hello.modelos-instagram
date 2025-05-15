from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    __tablename__="user"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(120), nullable=False)
    lastname: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "firtsname": self.firstname,
            "lastname": self.lastname,
            # do not serialize the password, its a security breach
        }
class Post(db.Model):
     __tablename__="post"
     id: Mapped[int] = mapped_column(primary_key=True)
     user_id: Mapped[int] =mapped_column(ForeignKey("user.id"),nullable=False)

     def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            
            
        }
     
class Media(db.Model):
     __tablename__="media"
     id: Mapped[int] = mapped_column(primary_key=True)
     type: Mapped[str] = mapped_column(String(120), nullable=False)
     url:  Mapped[str] = mapped_column(String(120), nullable=False)
     post_id: Mapped[int] =mapped_column(ForeignKey("post.id"),nullable=False)


     def serialize(self):
        return {
            "id": self.id,
            "post_id": self.post_id,
            "type": self.type,
            "url": self.url,
            
        }
     
class Follower(db.Model):
    __tablename__="follower"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_from_id: Mapped[int] =mapped_column(ForeignKey("user.id"),nullable=False)
    user_to_id: Mapped[int] =mapped_column(ForeignKey("user.id"),nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id
            
        }
class Comment(db.Model):
    __tablename__="comment"
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(500), nullable=False)
    autor_id: Mapped[int] =mapped_column(ForeignKey("user.id"),nullable=False)
    post_id: Mapped[int] =mapped_column(ForeignKey("post.id"),nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "post_id": self.post_id,
            "comment_text": self.comment_text,
            "autor_id": self.autor_id,
            
        }
     

    

     

