import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

df = pd.read_csv("logs/attacks.csv", names=["ip","user","pass","time"])

X = [[len(str(u)), len(str(p))] for u,p in zip(df["user"],df["pass"])]

model = IsolationForest()
model.fit(X)

joblib.dump(model,"ml_engine/model.pkl")
print("Model trained")
