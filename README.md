# Email Spam Detection System
A machine learning–based web application that classifies emails as Spam or Safe (Not Spam) using NLP techniques.
Built with Scikit-Learn and Streamlit, the app provides real-time spam detection with a clean, modern interface.

## 🚀 Features
* Spam vs Not-Spam classification
* Trained ML model loaded from .pkl file
* Text vectorization using saved feature extractor
* Real-time prediction from user input
* Clean glassmorphism UI with clear visual feedback

## How It Works
### 1️⃣ Dataset
#### Uses a labeled email dataset (mail_data.csv) containing:
* Email text
* Spam / Not Spam labels

### 2️⃣ Text Processing
* Text preprocessing
* Feature extraction using TF-IDF / CountVectorizer
* Vectorizer saved as feature_extraction.pkl

### 3️⃣ ML Model
* Binary classification model
* Trained in Jupyter Notebook
* Saved as Email Spam model.pkl

### 4️⃣ Prediction Flow
#### User input → Vectorizer transform → Model prediction →
#### Result displayed as:
* 🚨 Spam Email
* ✅ Safe Email

## Tech Stack
* Python
* Streamlit
* Scikit-Learn
* Pickle
* NumPy
* NLP (Text Vectorization)

## 📦 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create virtual environment
```bash
python -m venv venv
```

### 3️⃣ Activate environment

#### Windows
```bash
venv\Scripts\activate
```

#### Mac/Linux
```bash
source venv/bin/activate
```

### 4️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Run the app
```bash
streamlit run main.py
```

## 📁 Project Structure
```bash
│── main.py                      # Streamlit application
│── Email Spam Detection.ipynb   # Model training notebook
│── mail_data.csv                # Dataset
│── Email Spam model.pkl         # Trained ML model
│── feature_extraction.pkl       # Text vectorizer
│── requirements.txt
└── README.md
```

## Dataset 
Available on
Kaggle : https://www.kaggle.com/datasets/suraj452/mail-data

## 🌐 Live Demo
https://maildetection.streamlit.app/

## 📸 Screenshots
![img alt](https://github.com/nikhil-kumarrr/images/blob/main/Screenshot%202025-12-16%20115920.png?raw=true)
![img alt](https://github.com/nikhil-kumarrr/images/blob/main/Screenshot%202025-12-16%20115854.png?raw=true)
