from sqlmodel import SQLModel , Field , Column
import uuid
from datetime import datetime, date, timezone
import sqlalchemy.dialects.postgresql as pg
""""
class User :
    uid : uuid.UUID
    username : str 
    email : str 
    first_name : str 
    last_name : str 
    is_verified : bool = False 
    created_at : datetime 
    updated_at : datetime
"""

class User(SQLModel , table=True):
    __tablename__ ='users'
    uid : uuid.UUID = Field(
        sa_column=Column(
            pg.UUID , 
            nullable=False ,
            primary_key= True , 
            default= uuid.uuid4
        )
    )
    username : str 
    email : str 
    first_name : str 
    last_name : str 
    is_verified : bool = Field(default=False)
    created_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP(timezone=True),
            default_factory=lambda: datetime.now(timezone.utc)
        )
    )
    update_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP(timezone=True),
            default_factory=lambda: datetime.now(timezone.utc)
        )
    )
    
    def __repr__(self):
        return f"User{self.username}"