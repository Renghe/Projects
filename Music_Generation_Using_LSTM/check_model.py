from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.initializers import Orthogonal
import numpy as np
import os

# Step 1: Define and save the model
model = Sequential()
model.add(LSTM(64, kernel_initializer=Orthogonal(), input_shape=(10, 10)))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.save('model.h5')
print("Model saved successfully.")

# Step 2: Check if the model file exists
if os.path.exists('model.h5'):
    print("Model file exists.")
else:
    print("Model file does not exist.")

# Step 3: Load the model and make a prediction
model = load_model('model.h5', custom_objects={'Orthogonal': Orthogonal})
print("Model loaded successfully.")

dummy_input = np.random.random((1, 10, 10))
prediction = model.predict(dummy_input)
print("Prediction:", prediction)
