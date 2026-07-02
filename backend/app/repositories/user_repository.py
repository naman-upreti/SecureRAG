from sqlalchemy.orm import Session 
from app.models.user import User 
from typing import Optional 
class UserRepository:
    def __init__(self,db:Session):
        self.db = db 

    def create_user(self, user:User)->User:
        """ 
        Add user to Database 
        """

        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user

        except Exception:
            self.db.rollback()
            raise 
    
    
    def get_user_by_email(self,email:str,)->Optional[User]:    
        return (
            self.db.query(User)
            .filter(User.email == email).first() 
        )
    
    
            
    def get_user_by_id(self,user_id:int)->Optional[User]:
        return(
            self.db.query(User).filter(User.id==user_id).first()
        )

    def update_user(self,user:User)->User:
        """
        update an existing user in database
        """

        try:
            self.db.commit()
            self.db.refresh(user)
            return user 

        except Exception:
            self.db.rollback()
            raise 

    # def delete_user(self ,user=User):
    #     """
    #     delete an exixting user form database 
    #     """

    #     try:
    #         self.db.delete(user)
    #         self.db.commit()
    #         # no return because there is nothing to return
    #     except Exception:
    #         self.db.rollback()
    #         raise


    
"""
how the service uses them 

suppose the service wants to deactivate the user

user = repository._user_by_id(user_id)
user is_active = False 
repository.update(user)

""" 
## the only purpose od the repository is to convert the python login into the sql commant
## so the the database that we are using can understand 
## it doesnt care about the user activaities at all