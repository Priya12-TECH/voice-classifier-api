import pickle
import numpy as np

with open("models/voice_classifier.pkl", "rb") as f:
    model = pickle.load(f)

def predict_voice(features):
    prob = model.predict_proba(features)[0]
    prediction = model.predict(features)[0]

    if prediction == 1:
        return "AI_GENERATED", float(prob[1])
    else:
        return "HUMAN", float(prob[0])
