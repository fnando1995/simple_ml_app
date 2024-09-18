from fastapi import FastAPI, Depends, HTTPException
import joblib
import pandas as pd

from .database import engine,db
from .config import MODEL_PATH
from .schema import CustomerData, BatchCustomerData
from .crud import save_predictions, get_predictions
from .models import Base

# Create Models in Database Conn
Base.metadata.create_all(bind=engine)

# Load model
model = joblib.load(MODEL_PATH)

# Init Fast API App
app = FastAPI()

# EndPoints

@app.post("/test")
def test():
    """
    Test endpoint to check connectivity
    """
    return {"message": "Hello World, this is a test!"}

@app.post("/getall")
def get_all_preds(db=Depends(db)):
    """
    Endpoint to get all the predictions in the 
    database as a list.
    """
    preds = get_predictions(db)
    if preds:
        return preds
    else:
        raise HTTPException(status_code=200, detail='No preds found in the database.')

@app.post("/predict")
def predict_segment(data: CustomerData,db = Depends(db)):
    """
    Endpoint to predict a single request.
    Return the result:
        {   
        cluster: #NumberOfCluster
        }
    """
    try:
        # Transform CustomerData to a dataframe
        df = pd.DataFrame([data.model_dump()])
        
        # Predict
        results = model.predict(df)

        # modify results as needed
        cluster = int(results[0])

        # save results in database
        save_predictions(db, data,cluster)
        
        return  {
                "cluster":cluster
                    }
    except Exception as e:
        # Raise Error if anything happens, the Error will be detailed in the endpoint response.
        raise HTTPException(status_code=500, detail=f"Inference Error: {e}")

@app.post("/predict_batch")
def predict_batch(data: BatchCustomerData, db=Depends(db)):
    """
    Endpoint to predict a batch request.
    Return the result:
        {   
        clusters: [#NumberOfCluster,#NumberOfCluster,...]
        }
    """
    try:
        # Transform BatchCustomerData to a dataframe
        df = pd.DataFrame([customer.model_dump() for customer in data.customers])
        
        # Predict
        results = model.predict(df)

        # modify results as needed
        clusters = results.tolist()

        # save each result in database
        for customer_data, cluster in zip(data.customers, clusters):
            save_predictions(db, customer_data, cluster)
        
        # Return the clusters as a list
        return {
                "clusters": clusters
                }
    except Exception as e:
        # Raise Error if anything happens, the Error will be detailed in the endpoint response.
        raise HTTPException(status_code=500, detail=f"Batch Inference Error: {e}")