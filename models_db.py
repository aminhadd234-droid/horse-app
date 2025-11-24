from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base
import datetime
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default='user')
    balance = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
class Horse(Base):
    __tablename__ = 'horses'
    horse_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    trainer = Column(String)
class Jockey(Base):
    __tablename__ = 'jockeys'
    jockey_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    rating = Column(Float)
class Race(Base):
    __tablename__ = 'races'
    race_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String)
    date = Column(DateTime)
    status = Column(String, default='scheduled')
class Bet(Base):
    __tablename__ = 'bets'
    bet_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    race_id = Column(Integer, ForeignKey('races.race_id'))
    horse_id = Column(Integer, ForeignKey('horses.horse_id'))
    amount = Column(Float, nullable=False)
    odds = Column(Float, nullable=False)
    status = Column(String, default='placed')
    user = relationship('User')
    race = relationship('Race')
    horse = relationship('Horse')
