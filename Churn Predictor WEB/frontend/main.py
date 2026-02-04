import streamlit as st
import requests
import pandas as pd

# Page Config
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="centered"
)

# API URL
API_URL = API_URL = "http://127.0.0.1:8000/predict"

# Title
st.title("📊 Customer Churn Predictor")
st.markdown("Enter customer details below to predict churn probability:")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("👤 Customer Info")
    gender = st.selectbox("Gender", ["Female", "Male"])
    senior_citizen = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    
    st.subheader("📞 Phone Services")
    phone_service = st.selectbox("Phone Service", ["Yes", "No"])
    
    if phone_service == "Yes":
        multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No"])
    else:
        multiple_lines = "No phone service"

with col2:
    st.subheader("🌐 Internet Services")
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    
    options = ["Yes", "No", "No internet service"]
    
    online_security = st.selectbox("Online Security", options)
    online_backup = st.selectbox("Online Backup", options)
    device_protection = st.selectbox("Device Protection", options)
    tech_support = st.selectbox("Tech Support", options)
    streaming_tv = st.selectbox("Streaming TV", options)
    streaming_movies = st.selectbox("Streaming Movies", options)
    
    st.subheader("💰 Billing Info")
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment_method = st.selectbox(
        "Payment Method",
        ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
    )
    
    monthly_charges = st.number_input("Monthly Charges ($)", 0.0, 500.0, 50.0, step=1.0)
    total_charges = st.number_input("Total Charges ($)", 0.0, 10000.0, 500.0, step=1.0)

# Predict button
if st.button("🚀 Predict Churn", type="primary"):
    input_data = {
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }
    
    try:
        with st.spinner("Predicting..."):
            response = requests.post(API_URL, json=input_data)
        
        if response.status_code == 200:
            result = response.json()
            
            # Extract prediction from the response structure
            if "response" in result:
                prediction = result["response"]
                
                # Display the main prediction
                st.markdown("---")
                
                # Create a nice card for the prediction
                pred_card = st.container()
                with pred_card:
                    col1, col2 = st.columns([2, 1])
                    
                    with col1:
                        # Map the prediction to more readable format
                        pred_text = prediction["predicted_category"]
                        if pred_text == "CHURN":
                            st.error(f"**Prediction: Customer will CHURN** ⚠️")
                        else:
                            st.success(f"**Prediction: Customer will NOT CHURN** ✅")
                    
                    with col2:
                        confidence_percent = prediction["confidence"] * 100
                        st.metric("Confidence", f"{confidence_percent:.1f}%")
                
                # Display class probabilities
                st.subheader("📊 Probability Breakdown")
                
                # Convert probabilities to readable format
                probs = prediction["class_probabilities"]
                readable_probs = {}
                
                for key, value in probs.items():
                    if key == "0":
                        readable_probs["NOT CHURN"] = value
                    elif key == "1":
                        readable_probs["CHURN"] = value
                    else:
                        readable_probs[key] = value
                
                # Display as metrics
                cols = st.columns(len(readable_probs))
                for i, (label, prob) in enumerate(readable_probs.items()):
                    with cols[i]:
                        st.metric(label, f"{prob:.1%}")
                
                # Display as dataframe
                st.subheader("Detailed Probabilities")
                prob_df = pd.DataFrame({
                    "Category": list(readable_probs.keys()),
                    "Probability": list(readable_probs.values())
                })
                st.dataframe(prob_df.style.format({"Probability": "{:.2%}"}))
                
                # Show raw response for debugging
                with st.expander("View raw API response"):
                    st.json(result)
                
            else:
                st.error("Unexpected response format from API")
                st.json(result)
        
        else:
            st.error(f"API Error: {response.status_code}")
            st.write("Response:", response.json())
    
    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the FastAPI server. Make sure it's running at the correct URL.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")