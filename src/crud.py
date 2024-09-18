from sqlalchemy.orm import Session

from .schema import CustomerData
from .models import Predictions

def save_predictions(db: Session, data: CustomerData, cluster: int):
    """
    Save a single prediction using the CustomerData object and the
    cluster results. Creates an object Predictions to save the data
    and seamlessly insert/add to the database (orm).
    """
    
    # Creates Prediction object using CustomerData and Cluster.
    prediction = Predictions(
        recency=data.recency,
        frequency=data.frequency,
        monetary=data.monetary,
        cluster=cluster
    )
    
    # Adds the prediction to the database
    db.add(prediction)
    # Commit changes
    db.commit()
    # Refresh for visualization
    db.refresh(prediction)

def get_predictions(db: Session):
    """
    Returns all the rows in the database (all predictions).
    """
    return db.query(Predictions).all()
