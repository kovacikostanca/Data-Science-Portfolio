from pathlib import Path
import json

import joblib
import pandas as pd
import streamlit as st

ROOT_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = ROOT_DIR / "models"

st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📡",
    layout="wide",
)

@st.cache_resource
def load_artifacts():
    import os
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model = joblib.load(os.path.join(BASE_DIR, 'models', 'churn_model.pkl'))
    scaler = joblib.load(os.path.join(BASE_DIR, 'models', 'scaler.pkl'))
    with open(os.path.join(BASE_DIR, 'models', 'model_metadata.json')) as f:
        metadata = json.load(f)
    return model, scaler, metadata

model, scaler, metadata = load_artifacts()
THRESHOLD = metadata["optimal_threshold"]
FEATURE_COLUMNS = metadata["feature_columns"]

st.title("📡 Customer Churn Predictor")
st.markdown("Enter a customer profile below to predict churn risk.")
st.markdown("---")

with st.sidebar:
    st.header("Model Info")
    st.metric("Algorithm", metadata.get("model_name", "Unknown"))
    st.metric("ROC-AUC", f"{metadata.get('roc_auc', 0.0):.4f}")
    st.metric("Threshold", f"{THRESHOLD:.2f}")

st.subheader("Customer Profile")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Account**")
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"],
    )
    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)",
        ],
    )
    paperless = st.selectbox("Paperless Billing", ["Yes", "No"])

with col2:
    st.markdown("**Charges**")
    monthly_charges = st.slider(
        "Monthly Charges ($)", 20.0, 120.0, 65.0, step=0.5
    )
    total_charges = st.number_input(
        "Total Charges ($)", min_value=0.0, value=float(tenure * monthly_charges)
    )
    st.markdown("**Demographics**")
    senior = st.selectbox("Senior Citizen", ["No", "Yes"])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["No", "Yes"])

with col3:
    st.markdown("**Services**")
    internet = st.selectbox("Internet Service", ["Fiber optic", "DSL", "No"])
    phone = st.selectbox("Phone Service", ["Yes", "No"])
    multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes"])
    online_security = st.selectbox("Online Security", ["No", "Yes"])
    online_backup = st.selectbox("Online Backup", ["No", "Yes"])
    device_protect = st.selectbox("Device Protection", ["No", "Yes"])
    tech_support = st.selectbox("Tech Support", ["No", "Yes"])
    streaming_tv = st.selectbox("Streaming TV", ["No", "Yes"])
    streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes"])

binary = {"Yes": 1, "No": 0}

def build_features() -> pd.DataFrame:
    data = {
        "gender": 0,
        "SeniorCitizen": 1 if senior == "Yes" else 0,
        "Partner": binary[partner],
        "Dependents": binary[dependents],
        "tenure": tenure,
        "PhoneService": binary[phone],
        "MultipleLines": binary[multiple_lines],
        "OnlineSecurity": binary[online_security],
        "OnlineBackup": binary[online_backup],
        "DeviceProtection": binary[device_protect],
        "TechSupport": binary[tech_support],
        "StreamingTV": binary[streaming_tv],
        "StreamingMovies": binary[streaming_movies],
        "PaperlessBilling": binary[paperless],
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "InternetService_Fiber optic": 1 if internet == "Fiber optic" else 0,
        "InternetService_No": 1 if internet == "No" else 0,
        "Contract_One year": 1 if contract == "One year" else 0,
        "Contract_Two year": 1 if contract == "Two year" else 0,
        "PaymentMethod_Credit card (automatic)": 1 if payment_method == "Credit card (automatic)" else 0,
        "PaymentMethod_Electronic check": 1 if payment_method == "Electronic check" else 0,
        "PaymentMethod_Mailed check": 1 if payment_method == "Mailed check" else 0,
    }
    df_input = pd.DataFrame([data])
    df_input = df_input.reindex(columns=FEATURE_COLUMNS, fill_value=0)
    df_input[["tenure", "MonthlyCharges", "TotalCharges"]]
    df_input[["tenure", "MonthlyCharges", "TotalCharges"]] = scaler.transform(
        df_input[["tenure", "MonthlyCharges", "TotalCharges"]]
    )
    return df_input

st.markdown("---")

if st.button("🔍 Predict Churn Risk", type="primary", use_container_width=True):
    features = build_features()
    probability = model.predict_proba(features)[0][1]
    prediction = int(probability >= THRESHOLD)

    st.markdown("---")
    st.subheader("Prediction Result")

    r1, r2, r3 = st.columns(3)
    with r1:
        st.metric("Churn Probability", f"{probability * 100:.1f}%")
    with r2:
        st.metric("Threshold Used", f"{THRESHOLD:.2f}")
    with r3:
        if prediction == 1:
            st.error("⚠️ HIGH CHURN RISK")
        else:
            st.success("✅ LOW CHURN RISK")

    st.progress(float(probability))
    st.markdown(f"Risk level: **{probability * 100:.1f}%**")
    st.markdown("---")

    f1, f2 = st.columns(2)

    with f1:
        st.markdown("**Key Risk Signals**")
        signals = []
        if contract == "Month-to-month":
            signals.append("⚠️ Month-to-month contract — no lock-in")
        if internet == "Fiber optic":
            signals.append("⚠️ Fiber optic — high-cost, competitive service")
        if payment_method == "Electronic check":
            signals.append("⚠️ Electronic check — low engagement signal")
        if tenure < 12:
            signals.append("⚠️ Short tenure — still in high-churn window")
        if monthly_charges > 70:
            signals.append("⚠️ High monthly charges — price sensitivity risk")
        if tech_support == "No":
            signals.append("⚠️ No tech support — lower perceived value")
        if online_security == "No":
            signals.append("⚠️ No online security — less stickiness")
        if not signals:
            signals.append("✅ No major risk signals detected")
        for s in signals:
            st.markdown(s)

    with f2:
        st.markdown("**Recommended Retention Actions**")
        if prediction == 1:
            if contract == "Month-to-month":
                st.markdown("💡 Offer discounted 1-year contract upgrade")
            if monthly_charges > 70:
                st.markdown("💡 Provide loyalty discount on current plan")
            if tech_support == "No":
                st.markdown("💡 Offer free 3-month tech support trial")
            if online_security == "No":
                st.markdown("💡 Bundle online security at reduced rate")
            if tenure < 12:
                st.markdown("💡 Assign dedicated onboarding support rep")
            st.markdown("💡 Schedule proactive check-in call within 7 days")
        else:
            st.markdown("✅ Customer appears stable — standard engagement")
            st.markdown("💡 Consider upsell opportunity on premium services")
