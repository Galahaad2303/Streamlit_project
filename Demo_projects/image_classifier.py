import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image


# Load the trained model
@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model('path/to/your/model')
    return model


# Preprocess the input image
def preprocess_image(image):
    image = image.resize((224, 224))
    image = np.array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image


# Class labels for the ImageNet dataset (you can modify this based on your model's classes)
class_labels = ['class1', 'class2', 'class3', '...']

# Load the model
model = load_model()

# Streamlit app layout
st.title("Image Classifier")
st.write("Upload an image for classification")

# File upload feature
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read and preprocess the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    processed_image = preprocess_image(image)

    # Make predictions
    predictions = model.predict(processed_image)
    predicted_class = np.argmax(predictions)
    predicted_label = class_labels[predicted_class]
    confidence = predictions[0][predicted_class] * 100

    # Display the predicted class and confidence
    st.write(f"Predicted Class: {predicted_label}")
    st.write(f"Confidence: {confidence:.2f}%")
