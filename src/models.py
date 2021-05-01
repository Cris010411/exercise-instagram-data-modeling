import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    user =  relationship(User)
    text = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)

class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    tipo = Column(String(250))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)

class Followers(Base):
    __tablename__ = 'followers'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    user_from_id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'))
    
    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')