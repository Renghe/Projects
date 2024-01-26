import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the saved model
with open('your_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

st.title('Rock and Mine Detection App')

# Input for new data
st.header('Enter new data:')
input_data = st.text_area('Enter data (comma-separated values):', '0.0307,0.0523,0.0653,...')

if st.button('Predict'):
    # Convert input string to a list of floats
    input_list = [float(val) for val in input_data.split(',')]

    # Reshape the input for prediction
    input_reshaped = np.asarray(input_list).reshape(1, -1)

    # Make prediction
    prediction = model.predict(input_reshaped)

    # Display the prediction
    st.subheader('Prediction:')
    if prediction[0] == 'R':
        st.write('The object is a Rock')
    else:
        st.write('The object is a mine')

