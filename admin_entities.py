from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .db import get_db
from . import models_db, schemas
from .auth import require_admin_user
router = APIRouter(prefix='/admin', tags=['admin'])
@router.get('/horses', response_model=list[schemas.HorseOut])
def list_horses(db: Session = Depends(get_db), _: models_db.User = Depends(require_admin_user)):
    return db.query(models_db.Horse).all()
@router.post('/horses', response_model=schemas.HorseOut)
def create_horse(h: schemas.HorseCreate, db: Session = Depends(get_db), _: models_db.User = Depends(require_admin_user)):
    horse = models_db.Horse(name=h.name, age=h.age, trainer=h.trainer)
    db.add(horse); db.commit(); db.refresh(horse); return horse
@router.put('/horses/{horse_id}', response_model=schemas.HorseOut)
def update_horse(horse_id: int, h: schemas.HorseCreate, db: Session = Depends(get_db), _: models_db.User = Depends(require_admin_user)):
    horse = db.query(models_db.Horse).filter(models_db.Horse.horse_id == horse_id).first()
    if not horse: raise HTTPException(status_code=404, detail='Horse not found')
    horse.name = h.name; horse.age = h.age; horse.trainer = h.trainer
    db.commit(); db.refresh(horse); return horse
@router.delete('/horses/{horse_id}')
def delete_horse(horse_id: int, db: Session = Depends(get_db), _: models_db.User = Depends(require_admin_user)):
    horse = db.query(models_db.Horse).filter(models_db.Horse.horse_id == horse_id).first()
    if not horse: raise HTTPException(status_code=404, detail='Horse not found')
    db.delete(horse); db.commit(); return {'success': True}
# Jockeys
@router.get('/jockeys', response_model=list[schemas.JockeyOut])
def list_jockeys(db: Session = Depends(get_db), _: models_db.User = Depends(require_admin_user)):
    return db.query(models_db.Jockey).all()
@router.post('/jockeys', response_model=schemas.JockeyOut)
def create_jockey(j: schemas.JockeyCreate, db: Session = Depends(get_db), _: models_db.User = Depends(require_admin_user)):
    jj = models_db.Jockey(name=j.name, rating=j.rating); db.add(jj); db.commit(); db.refresh(jj); return jj
@router.put('/jockeys/{jockey_id}', response_model=schemas.JockeyOut)
def update_jockey(jockey_id: int, j: schemas.JockeyCreate, db: Session = Depends(get_db), _: models_db.User = Depends(require_admin_user)):
    jockey = db.query(models_db.Jockey).filter(models_db.Jockey.jockey_id == jockey_id).first()
    if not jockey: raise HTTPException(status_code=404, detail='Jockey not found')
    jockey.name = j.name; jockey.rating = j.rating; db.commit(); db.refresh(jockey); return jockey
@router.delete('/jockeys/{jockey_id}')
def delete_jockey(jockey_id: int, db: Session = Depends(get_db), _: models_db.User = Depends(require_admin_user)):
    jockey = db.query(models_db.Jockey).filter(models_db.Jockey.jockey_id == jockey_id).first()
    if not jockey: raise HTTPException(status_code=404, detail='Jockey not found')
    db.delete(jockey); db.commit(); return {'success': True}
# Races CRUD
@router.post('/races', response_model=schemas.RaceOut)
def create_race(r: schemas.RaceCreate, db: Session = Depends(get_db), _: models_db.User = Depends(require_admin_user)):
    race = models_db.Race(name=r.name, location=r.location, date=r.date, status='scheduled'); db.add(race); db.commit(); db.refresh(race); return race
@router.get('/races', response_model=list[schemas.RaceOut])
def list_races(db: Session = Depends(get_db), _: models_db.User = Depends(require_admin_user)):
    return db.query(models_db.Race).all()
@router.put('/races/{race_id}', response_model=schemas.RaceOut)
def update_race(race_id: int, r: schemas.RaceCreate, db: Session = Depends(get_db), _: models_db.User = Depends(require_admin_user)):
    race = db.query(models_db.Race).filter(models_db.Race.race_id == race_id).first()
    if not race: raise HTTPException(status_code=404, detail='Race not found')
    race.name = r.name; race.location = r.location; race.date = r.date; db.commit(); db.refresh(race); return race
@router.delete('/races/{race_id}')
def delete_race(race_id: int, db: Session = Depends(get_db), _: models_db.User = Depends(require_admin_user)):
    race = db.query(models_db.Race).filter(models_db.Race.race_id == race_id).first()
    if not race: raise HTTPException(status_code=404, detail='Race not found')
    db.delete(race); db.commit(); return {'success': True}
# Bets list/settle
@router.get('/bets')
def list_bets(db: Session = Depends(get_db), _: models_db.User = Depends(require_admin_user)):
    return db.query(models_db.Bet).all()
@router.post('/bets/{bet_id}/settle')
def settle_bet(bet_id: int, result: dict, db: Session = Depends(get_db), _: models_db.User = Depends(require_admin_user)):
    b = db.query(models_db.Bet).filter(models_db.Bet.bet_id == bet_id).first()
    if not b: raise HTTPException(status_code=404, detail='Bet not found')
    if b.horse_id == result.get('winner_horse_id'):
        b.status = 'won'
        user = db.query(models_db.User).filter(models_db.User.user_id == b.user_id).first()
        if user:
            user.balance += b.amount * b.odds
    else:
        b.status = 'lost'
    db.commit()
    return b
@router.get('/stats')
def stats(db: Session = Depends(get_db), _: models_db.User = Depends(require_admin_user)):
    users_count = db.query(models_db.User).count()
    bets_count = db.query(models_db.Bet).count()
    total_amount = sum([b.amount for b in db.query(models_db.Bet).all()]) if bets_count else 0
    return {'users_count': users_count, 'bets_count': bets_count, 'total_amount': total_amount, 'model_auc': 0.75}
