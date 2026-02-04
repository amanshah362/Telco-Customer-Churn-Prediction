from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from model.predict import predict_output, model, MODEL_VERSION

app = FastAPI()

# human readable       
@app.get('/')
def home():
    return {'message':'Churn Prediction API'}

# machine readable
@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is not None
    }

@app.post('/predict', response_model=PredictionResponse)
def predict_churn(data: UserInput):

    user_input = {
        'gender': data.gender,
        'SeniorCitizen': data.SeniorCitizen,
        'Partner': data.Partner,
        'Dependents': data.Dependents,
        'tenure': data.tenure,
        'PhoneService': data.PhoneService,
        'MultipleLines': data.MultipleLines,
        'InternetService': data.InternetService,
        'OnlineSecurity': data.OnlineSecurity,
        'OnlineBackup': data.OnlineBackup,
        'DeviceProtection': data.DeviceProtection,
        'TechSupport': data.TechSupport,
        'StreamingTV': data.StreamingTV,
        'StreamingMovies': data.StreamingMovies,
        'Contract': data.Contract,
        'PaperlessBilling': data.PaperlessBilling,
        'PaymentMethod': data.PaymentMethod,
        'MonthlyCharges': float(data.MonthlyCharges),
        'TotalCharges': float(data.TotalCharges)
    }

    try:

        prediction = predict_output(user_input)

        return JSONResponse(status_code=200, content={'response': prediction})
    
    except Exception as e:

        return JSONResponse(status_code=500, content=str(e))
