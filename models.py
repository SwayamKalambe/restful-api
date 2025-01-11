from sqlalchemy import Column, Integer, String, Float
from database import Base

class FashionItems(Base):
    __tablename__ = "fashion_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index= True, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String, nullable=False)


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)