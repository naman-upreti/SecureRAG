from datetime import datetime 
from sqlalchemy import Boolean
from sqlalchemy import DateTime 
from sqlalchemy import Integer 
from sqlalchemy import String 
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id:Mapped[int]=mapped_column(
        Integer,
        primary_key=True,
        index = True 
    )    


    name:Mapped[str]=mapped_column(
        String(255),
        nullable= False
    )

    email:Mapped[str]=mapped_column(
        String(255),
        nullable= False,
        unique= True,
        index = True 
    )

    password_hash:Mapped[str]=mapped_column(
        String(255),
        nullable= False
    )

    role:Mapped[str]=mapped_column(
        String(50),
        nullable= False,
        default = "employee"
    )

    is_active:Mapped[bool]=mapped_column(
        Boolean,
        default=True,
        nullable= False
    )

    created_at:Mapped[datetime]=mapped_column(
        DateTime,
        default=datetime.utcnow
    )   



"""
    what infromation does user needs 
    - id : int -- primary key and index 
    - name : str -- this is the name that is displayed in ui 
    - email : str -- unique and index # [EMAIL_ADDRESS] 
    - password_hash : str  -- [PASSWORD] -> which will e hashed 
                            hash them usinf bcrypt later on 
                            even the database leak nobody sees the original password 
    - role : str -- admin , manager , enployee  authorization  uses it to check the access 
    - is_active : bool 
    - created_at : datetime timestamp

Let's Visualize the Table

Your model creates:


Column		    Type	    Purpose
id		        Integer	    Primary key
name		    String	    User's display name
email		    String	    Login identifier
password_hash	String	    Securely stored password
role		    String	    Authorization
is_active	    Boolean	    Enable/disable account
created_at	    DateTime	Account creation timestamp
"""

