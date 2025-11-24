from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
class UserCreate(BaseModel):
    email: EmailStr
    password: str
class UserOut(BaseModel):
    user_id: int
    email: EmailStr
    role: str
    balance: float
    created_at: datetime
    class Config:
        orm_mode = True
class HorseCreate(BaseModel):
    name: str
    age: Optional[int] = None
    trainer: Optional[str] = None
class HorseOut(HorseCreate):
    horse_id: int
    class Config:
        orm_mode = True
class JockeyCreate(BaseModel):
    name: str
    rating: Optional[float] = None
class JockeyOut(JockeyCreate):
    jockey_id: int
    class Config:
        orm_mode = True
class RaceCreate(BaseModel):
    name: str
    location: Optional[str] = None
    date: Optional[datetime] = None
class RaceOut(RaceCreate):
    race_id: int
    status: str
    class Config:
        orm_mode = True
class BetCreate(BaseModel):
    user_id: int
    race_id: int
    horse_id: int
    amount: float
class BetOut(BaseModel):
    bet_id: int
    user_id: int
    race_id: int
    horse_id: int
    amount: float
    odds: float
    status: str
    class Config:
        orm_mode = True
