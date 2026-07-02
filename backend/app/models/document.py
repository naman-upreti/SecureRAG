from datetime import datetime 

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String 

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
# mapped is used for Python 3.8+ type hints and modern SQLAlchemy


from app.db.base import Base

class Document(Base): # this class inherit the mapper feature from base class in db/
    # becaluse sqlalchemy only recognize the clases that inherit from base as data base 

    #____ Field 1 id _____
    __tablename__ = "documents" # defining table name 
    id:Mapped[int]=mapped_column(
        Integer,
        primary_key=True,
        index =True # when the user count increse the index help sqlite to directl acced the fealt 
    )
    
    #____ Field 2 file name ___
    filename:Mapped[str]=mapped_column(
        String(255),
        nullable=False # making it mendotory as file name cant be empty 
    )

    #___ Field 3____ 
    file_path :Mapped[str]=mapped_column(
        String(500),
        nullable=False,
        unique=True,
        index = True
    )

    # ___ Field 4 Upload time ____

    uploaded_at:Mapped[datetime]= mapped_column(
        DateTime, 
        default = datetime.utcnow 
    )

    # ___ Field 5 Indexed ____
    is_indexed:Mapped[bool]=mapped_column(
        Boolean,
        default=False 
    )

    #___ Field 6 Chunk Count ____

    chunk_count:Mapped[int]= mapped_column(
        Integer,
        default = 0
    )

""" the table will look like the below table 

| id | filename     | file_path   | uploaded_at | is_indexed | chunk_count |
| -- | ------------ | ----------- | ----------- | ---------- | ----------- |
| 1  | employee.pdf | uploads/... | 2026        | False      | 0           |
"""