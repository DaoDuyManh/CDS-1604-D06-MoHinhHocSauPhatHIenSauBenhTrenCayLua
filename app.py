# streamlit311\Scripts\activate
# python -m streamlit run app.py

import streamlit as st
from PIL import Image
import pandas as pd
import altair as alt
from test import get_probs, class_names
import onnx  

model = onnx.load("Model/best_model.onnx")

st.set_page_config(page_title="Rice Leaf Disease Classifier", layout="wide")

st.markdown(
    "<h1 style='text-align: center; color: #2E8B57;'>🌾 Rice Leaf Disease Classifier</h1>", 
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center; font-size:16px;'>Upload rice leaf images and get predictions</p>",
    unsafe_allow_html=True
)

uploaded_files = st.file_uploader(
    "Select rice leaf images (jpg/png/jpeg)", 
    type=["jpg", "png", "jpeg"], 
    accept_multiple_files=True
)

results = []

if uploaded_files:
    for uploaded_file in uploaded_files:
        img = Image.open(uploaded_file).convert("RGB")
        probs = get_probs(uploaded_file.name)
        pred_index = probs.argmax()
        pred_label = class_names[pred_index]
        pred_confidence = probs[pred_index]

        results.append({
            "filename": uploaded_file.name,
            "prediction": pred_label,
            "confidence": float(pred_confidence),
            **{class_names[i]: float(probs[i]) for i in range(len(class_names))}
        })

        st.markdown(f"<hr style='border:1px solid #eee'>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([1,1])

        with col1:
            st.image(img, caption=uploaded_file.name, use_container_width=True)
        
        with col2:
            st.markdown(f"<h3 style='color:#2E8B57;'>Prediction: {pred_label}</h3>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size:16px;'>Confidence: <b>{pred_confidence:.2f}</b></p>", unsafe_allow_html=True)
            
            prob_df = pd.DataFrame({
                'Disease': class_names,
                'Probability': probs
            })
            chart = alt.Chart(prob_df).mark_bar(color="#2E8B57").encode(
                x=alt.X('Disease', sort=None, axis=alt.Axis(labelAngle=0)),  
                y='Probability',
                tooltip=['Disease', 'Probability']
            ).properties(width=400, height=200)
            st.altair_chart(chart, use_container_width=True)

            st.dataframe(prob_df.set_index('Disease'), width=400, height=200)

if results:
    df = pd.DataFrame(results)
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download predictions CSV",
        data=csv,
        file_name="rice_leaf_predictions_hidden_final.csv",
        mime="text/csv",
        use_container_width=True
    )



# venv\Scripts\activate
