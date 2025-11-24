from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .db import get_db
from . import models_db, schemas
from .auth import get_password_hash, verify_password, create_access_token, get_current_user
from .auth import oauth2_scheme
router = APIRouter()
@router.post('/users', response_model=schemas.UserOut)
def create_user(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models_db.User).filter(models_db.User.email == user_in.email).first()
    if existing:
        raise HTTPException(status_code=400, detail='Email already registered')
    hashed = get_password_hash(user_in.password)
    u = models_db.User(email=user_in.email, hashed_password=hashed, role='user')
    db.add(u); db.commit(); db.refresh(u); return u
@router.get('/races', response_model=list[schemas.RaceOut])
def public_list_races(db: Session = Depends(get_db)):
    return db.query(models_db.Race).filter(models_db.Race.status == 'scheduled').all()
@router.post('/bets', response_model=schemas.BetOut)
def place_bet(bet_in: schemas.BetCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    # simple balance check
    user = db.query(models_db.User).filter(models_db.User.user_id == current_user.user_id).first()
    if user.balance < bet_in.amount:
        raise HTTPException(status_code=400, detail='Insufficient balance')
    # compute odds placeholder
    odds = 2.0
    b = models_db.Bet(user_id=bet_in.user_id, race_id=bet_in.race_id, horse_id=bet_in.horse_id, amount=bet_in.amount, odds=odds, status='placed')
    user.balance -= bet_in.amount
    db.add(b); db.commit(); db.refresh(b); db.commit(); return b
