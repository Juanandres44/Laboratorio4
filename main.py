import pandas as pd

from typing import Optional

from fastapi import FastAPI

from DataModel import DataModel

from joblib import load


app = FastAPI()

model = load("modelo.joblib")



@app.get("/")
def read_root():
   return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}

@app.post("/predict")
def make_predictions(dataModel: DataModel):
    df = pd.DataFrame(dataModel.dict(), columns=dataModel.dict().keys(), index=[0])
    df.columns = dataModel.columns()
    prediction = model.predict(df)
    return {
       'prediction': prediction[0],
    }


#@app.post("/rSquared")
#def make_predictions(dataModel: DataModel):
    df = pd.DataFrame(dataModel.dict(), columns=dataModel.dict().keys(), index=[0])
    df.columns = dataModel.columns()
    score = model.score(df.drop('Life expectancy', axis=1 ),df['Life expectancy'])
    return {
       'r2 score': score[0],
    }


