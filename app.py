from fastapi import FastAPI
from .db import engine, Base, SessionLocal
from . import models_db
from .admin_entities import router as admin_router
from .public_api import router as public_router
from .token_route import router as token_router
import os
app = FastAPI(title='Horse Racing Betting API')
Base.metadata.create_all(bind=engine)
app.include_router(token_router)
app.include_router(public_router)
app.include_router(admin_router)
@app.on_event('startup')
def create_default_admin():
    db = SessionLocal()
    admin_email = os.getenv('ADMIN_EMAIL', 'admin@example.com')
    admin_pass = os.getenv('ADMIN_PASS', 'adminpass')
    exists = db.query(models_db.User).filter(models_db.User.email==admin_email).first()
    from .auth import get_password_hash
    if not exists:
        u = models_db.User(email=admin_email, hashed_password=get_password_hash(admin_pass), role='admin')
        db.add(u); db.commit()
    db.close()
@app.get('/')
def root():
    return {'status':'ok','msg':'Horse Racing Betting API'}
