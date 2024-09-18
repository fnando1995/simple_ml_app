from pydantic import BaseModel, ConfigDict
from typing import List

class CustomerData(BaseModel):
    """
    Schema for the Customer Data to be used.
    """
    recency: float
    frequency: float
    monetary: float

    model_config = ConfigDict(
        from_attributes=True        
    )

class BatchCustomerData(BaseModel):
    """
    Schema for the Batch Customer Data to be used. This is
    a list of Customer Data.
    """
    customers: List[CustomerData]    