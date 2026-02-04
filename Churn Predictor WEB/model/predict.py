import pickle
import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder

# import the ml model
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "churn_model.pkl")

with open(model_path, "rb") as model_file:
    model = pickle.load(model_file)

# MLFlow
MODEL_VERSION = '1.0.0'

# Get class labels from model (important for matching probabilities to class names)
class_labels = model.classes_.tolist()

def predict_output(user_input: dict):

    df = pd.DataFrame([user_input])

    # Predict the class
    predicted_class = model.predict(df)[0]

    # Get probabilities for all classes
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)
    
    # Create mapping: {class_name: probability}
    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))

    label_encoder = LabelEncoder()
    
    predicted_category = 'CHURN' if predicted_class == 1 else 'NOT CHURN'
    return {
        "predicted_category": predicted_category,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }