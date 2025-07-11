import numpy as np

def preprocess_input(data, feature_order, scaler, gender_map, smoke_map):
    row = {}
    for feature in feature_order:
        if feature == "gender":
            row[feature] = gender_map[data["gender"]]
        elif feature == "smoking_history":
            row[feature] = smoke_map[data["smoking_history"]]
        else:
            row[feature] = float(data[feature])
    arr = np.array([[row[feat] for feat in feature_order]])
    return scaler.transform(arr)
