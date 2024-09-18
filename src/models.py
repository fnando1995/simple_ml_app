from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,  Integer, Float

Base = declarative_base()

class Predictions(Base):
    """
    Definition of the Predictions table, later created using create_all()
    
    """
    __tablename__ = 'Predictions'
    id = Column(Integer, primary_key = True, autoincrement = True,index=True)
    recency = Column(Float,index=True)
    frequency = Column(Float,index=True)
    monetary = Column(Float,index=True)
    cluster = Column(Integer,index=True)



