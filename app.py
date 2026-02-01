# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 23:18:29 2026

@author: vaishnav gupta
"""

from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)

# Loading Trained Model
model = tf.keras.models.load_model("model.h5")
print("Loaded model input shape:", model.input_shape)

input_shape = model.input_shape[1:3]  

# Prediction Labels
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

UPLOAD_FOLDER = "static"
os.makedirs(UPLOAD_FOLDER, exist_ok=True) 

@app.route("/", methods=['GET', 'POST'])
def home():
    prediction = None
    img_path = None
    
    if request.method == "POST":
        file = request.files["file"]
        filename = secure_filename(file.filename)

        img_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(img_path)

        # --- Preprocess image correctly ---
        img = Image.open(img_path).convert("RGB")   # ensure 3 channels
        img = img.resize(input_shape)               # must match model input
        img = np.array(img) / 255.0
        img = np.expand_dims(img, axis=0)
        
        # Prediction
        pred = model.predict(img)
        prediction = class_names[np.argmax(pred)]
    
    return render_template("index.html", prediction=prediction, img_path=img_path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)