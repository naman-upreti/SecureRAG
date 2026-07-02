from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.core.security.password import hash_password,verify_password

from typing import Optional
class AuthService:
    """
    Handles authentication business logic.
    """

    def __init__(
        self,
        repository: UserRepository,
    ):
        self.repository = repository

    def register_user(
        self,
        name: str,
        email: str,
        password: str,
    ) -> User:

        existing_user = self.repository.get_user_by_email(email)

        if existing_user:
            raise ValueError("Email already registered")

        user = User(
            name=name,
            email=email,
            password_hash=hash_password(password),
        )

        return self.repository.create_user(user)

    def authenticate_user(self,email: str,password: str ) -> Optional[User]:
        """
        Authenticate user by email and password
        """
        user = self.repository.get_user_by_email(email)

        if user is None:
            return None

        if not verify_password(password,user.password_hash):
            return None

        return user




"""
email -> repository -> user found - if no  --> return none 
- if yes --> password check 
if not match --> return none 
if match --> return user
"""