import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    profile_name = Column(String(80), nullable=False)
    post = relationship('Post',back_populates='User', uselist=False)
    follower = relationship('Follower',back_populates='user', uselist=True)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    created_by_user = Column(String(250), ForeignKey('user.id'), nullable=False)
    created_at = Column(DateTime(80), nullable=False)
    comment = Column(String(250), nullable=False)
    user = relationship('User', back_populates='post')
    post_media = relationship('Post_Media', back_populates='post')


class Post_Media(Base):
    __tablename__ = 'post_media'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    media_file = Column(String(80), nullable=False)
    post = relationship('Post', back_populates='post_media')


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    following_user_id = Column(String(250), ForeignKey('user.id'), nullable=False)
    followed_user_id = Column(String(250), ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='follower')



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
