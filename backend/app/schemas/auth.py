
from pydantic import BaseModel


class RegisterRequest(BaseModel):
    name:str 
    email:str
    password :str 

class LoginRequest(BaseModel):
    email:str 
    password:str 

class TokenResponse(BaseModel):
    access_token:str 
    token_type:str="bearer"


class UserResponse(BaseModel):
    """
        this create a user response 
        when user is created we send this to the user
    """
    id:int
    name:str 
    email:str
    role:str 
   
    


"""
registerRequest 
loginRequest 
tokenRequest 
Frontend

{
    "email":"naman@gmail.com",
    "password":"123456"
}

        │
        ▼

LoginRequest (Schema)

        │
        ▼

Auth Router

        │
        ▼

AuthService.authenticate_user()

        │
        ▼

verify_password()

        │
        ▼

create_access_token()

        │
        ▼

TokenResponse
"""