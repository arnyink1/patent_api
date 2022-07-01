"""Modulo de autentificación."""

from fastapi import HTTPException,status
# from datetime import timedelta
from app.token import create_access_token


def auth_user(login):

    if login.username == "username" and login.password == "password":
        access_token = create_access_token(
            data={"sub": login.username}
        )
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No existe usuario {login.username}"
        )