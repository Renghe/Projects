import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.initializers import Orthogonal

# Load the model
model = load_model('model.h5', custom_objects={'Orthogonal': Orthogonal})

# Title of the app
st.title('LSTM Model Prediction')

# Instructions
st.write("Upload a CSV file containing the input data for the LSTM model (10x10 matrix).")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    input_data = pd.read_csv(uploaded_file, header=None).values

    # Check if the input_data has the correct shape
    if input_data.shape == (10, 10):
        # Convert input data to numpy array and reshape to match model input shape
        input_data = input_data.reshape(1, 10, 10)

        # Button for prediction
        if st.button('Predict'):
            prediction = model.predict(input_data)
            st.write(f'Prediction: {prediction[0][0]}')
    else:
        st.error("The uploaded file does not have the correct shape. Please upload a 10x10 matrix.")
