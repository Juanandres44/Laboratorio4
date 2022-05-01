import pandas as pd

import json

import RegModel

from typing import Optional

from fastapi import FastAPI,Request

from sklearn.metrics import r2_score




app = FastAPI()

RegressionModel = RegModel.Model()



@app.get("/")
def read_root():
   return {"Hello": "World"}



@app.post("/predict")
def make_predictions(dataModel: RegModel.DataModel):
    df = pd.DataFrame(dataModel.dict(), columns=dataModel.dict().keys(), index=[0])
    df.columns = RegModel.pred_columns()
    prediction = RegressionModel.make_predictions(df)
    return prediction.tolist()

@app.post("/rSquared")
async def calculate_r2(request_body: Request):
    request_info = await request_body.json()
    json_str = json.dumps([js for js in request_info])
    df = pd.read_json(json_str)
    df.columns = RegModel.r2_columns()
    x = df.drop('Life expectancy', axis=1)
    y = df['Life expectancy']
    y_pred = RegressionModel.make_predictions(x)
    r2 = r2_score(y, y_pred)
    return "'R^2: %.2f" % r2


