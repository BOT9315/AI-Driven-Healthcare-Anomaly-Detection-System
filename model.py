import numpy as np
from sklearn.ensemble import IsolationForest

# Create model
model = IsolationForest(contamination=0.1)

# Train with normal health data
normal_data = np.array([
    [72, 98, 36.8, 120],
    [75, 97, 37.0, 118],
    [70, 99, 36.7, 122],
    [73, 98, 36.9, 119],
])

model.fit(normal_data)

def predict_anomaly(data):
    prediction = model.predict([data])
    score = model.decision_function([data])[0]

    if prediction[0] == -1:
        if score < -0.2:
            return "HIGH"
        else:
            return "MEDIUM"
    else:
        return "LOW"