import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle
import os

# ==========================
# DUMMY TRAINING DATA
# ==========================
# 15 features = (13 MFCC + 1 spectral + 1 pitch)
X = np.random.rand(50, 15)

# Labels: 0 = HUMAN, 1 = AI_GENERATED
y = np.random.randint(0, 2, size=50)

# ==========================
# TRAIN SIMPLE MODEL
# ==========================
model = LogisticRegression()
model.fit(X, y)

# ==========================
# SAVE MODEL
# ==========================
os.makedirs("models", exist_ok=True)

with open("models/voice_classifier.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Dummy voice classifier model saved successfully")
