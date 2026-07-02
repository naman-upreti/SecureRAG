from datetime import datetime, timedelta, timezone
from typing import Any,Optional

from jose import jwt,JWTError

from app.core.config import settings

def create_access_token(data:dict[str,Any])->str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc)+timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update(
        {
            "exp":expire,
        }
    )
    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    return encoded_jwt

# datetime.utcnow() it will give the current time in UTC
# timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES) it will give the time in minutes

def verify_access_token(token:str) -> Optional[dict[str,Any]]:
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        return payload
    except JWTError:
        return None 


"""
what this file do   user logs in -->  userId,Email,Role --> jwt.encode()- klbdfuxbgjhbfvkh.....
verify token incoming request --> twt token -> jwt.decode()--> velid? --> response 


1. what is JWT? 
    login -> authenticaton -> generate json web  token  - > user upload the Pdf 
    -> authorization -> is the user allowed to access the information -> admin panel 
    -> authorization -> if not allowed reject the request if yes then proceed 
    token -> is the only key to access the information -> user should not share the token 
    


    server -> secret key -> sign token -> client -> client send token to server 
    server -> verify -> secret key -> is token valid 
    
"""

