from db.datebase import Base
from sqlalchemy import String,Integer,Column,Float

class User(Base):
    __tablename__ = "users"
    _id = Column(Integer,primary_key=True, unique=True, index=True)
    name = Column(String)
    password = Column(Integer)
    email = Column(String)


class Product(Base):
    __tablename__ = "produtcs"
    _id = Column(Integer,primary_key=True, unique=True, index=True)
    price = Column(Float)
    name = Column(String)
    category = Column(String)
    gender = Column(String)
    detail = Column(String)
    image = Column(String)


class Category(Base):
    __tablename__ = "category"
    _id = Column(Integer,primary_key=True,index=True)
    name=Column(String)


class Contact(Base):
    __tablename__ = "contact"
    id_ = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    massage = Column(String)
    date = Column(String)
    subject = Column(String)

