import joblib

model = joblib.load("models/laptop_price_pipe.pkl")
print(model)
