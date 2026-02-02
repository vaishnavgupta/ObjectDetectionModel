# 🧠 ResNet50 Object Detection Web App

This project is a Deep Learning based Object Detection web application built using **ResNet50** and **Flask**.  
Users can upload an image through a web interface, and the model predicts the object present in the image.

The application is deployed on **Hugging Face Spaces** and can be accessed online.

---

## 🚀 Live Demo

🔗 Hugging Face Space:  
https://huggingface.co/spaces/vaishnavgupta/object-detection-app

---

## 📌 Features

- Upload an image through a web interface  
- Deep Learning model based on ResNet50  
- Predicts one of the following classes:
  - airplane  
  - automobile  
  - bird  
  - cat  
  - deer  
  - dog  
  - frog  
  - horse  
  - ship  
  - truck  
- Loader animation while prediction is running  
- Interactive UI with image preview  
- Footer with developer details  
- Hosted for free on Hugging Face Spaces  

---

## 🛠️ Tech Stack

- **Python**
- **TensorFlow / Keras**
- **Flask**
- **HTML, CSS, JavaScript**
- **Hugging Face Spaces (Docker)**
- **GitHub**

---

## ⚙️ How It Works

1. User uploads an image from the browser.
2. Flask server receives the image.
3. Image is resized to the model’s required input size.
4. The ResNet50 model predicts the class label.
5. Prediction result is displayed on the webpage along with the uploaded image.

