from pydantic import HttpUrl
from sqlalchemy.sql.coercions import expect
from fastapi import APIRouter
from fastapi import Depends
from app.schemas.auth import RegisterRequest,LoginRequest,TokenResponse 
from app.core.security.jwt import create_access_token
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService
from app.db.database import get_db
from sqlalchemy.orm import Session

from app.schemas.auth import UserResponse
from fastapi import HTTPException
router = APIRouter()

@router.post(
    "/register",
    response_model=UserResponse
)
def register(
        register:RegisterRequest,
        db:Session=Depends(get_db)
    ): 
    
    repository =UserRepository(db)

    service= AuthService(repository)

    try:
        return service.register_user(
            register.name,
            register.email,
            register.password
        )
    except ValueError as e:
        raise HTTPException(
            status_code=409,
            detail=str(e)
        )


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    login_request: LoginRequest,
    db: Session = Depends(get_db),
):
    repository = UserRepository(db)
    service = AuthService(repository)

    user = service.authenticate_user(
        login_request.email,
        login_request.password,
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    token = create_access_token(
        {
            "sub": str(user.id),
            "email": user.email,
            "role": user.role,
        }
    )

    return TokenResponse(
        access_token=token,
        token_type="bearer",
    )    
"""
post/register 
post/login 
"""