from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key = True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    password= Column(String)
    gender= Column(String)


class Post(Base):
	__tablename__ = "posts"
	id = Column(Integer, primary_key = True)
	title = Column(String)
	article = Column(String)
	video = Column(String)
	quiz = Column(String)