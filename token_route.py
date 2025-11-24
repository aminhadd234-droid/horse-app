from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .db import get_db
from . import models_db
from .auth import verify_password, create_access_token
router = APIRouter()
@router.post('/token')
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models_db.User).filter(models_db.User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect username or password')
    access_token = create_access_token(data={'sub': str(user.user_id)})
    return {'access_token': access_token, 'token_type': 'bearer'}
