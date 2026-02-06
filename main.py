from data import df
from model import train_model
from evaluation import evaluate_model

model, X_test, y_test, y_pred = train_model(df)
evaluate_model(y_test, y_pred)