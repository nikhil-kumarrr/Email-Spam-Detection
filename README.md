# Email Spam Detection using Machine Learning  

## Project Overview  
This project focuses on building a machine learning model to classify emails as **Spam** or **Not Spam**.  
Using Natural Language Processing (NLP) techniques and machine learning algorithms, the model learns patterns from email text and predicts whether a given email is legitimate or spam.  

---

## Tech Stack  
- **Programming Language**: Python  
- **Libraries**:  
  - `scikit-learn` (Machine Learning models)  
  - `pandas`, `numpy` (Data handling)  
  - `matplotlib`, `seaborn` (Visualization)  
- **Algorithms Used**:  
  - Logistic Regression  
  - Naive Bayes (MultinomialNB)  

---

## Project Workflow  
1. **Data Preprocessing**  
   - Clean and prepare email text  
   - Remove stopwords, punctuations, and apply stemming  

2. **Feature Extraction**  
   - Convert text into numerical vectors using CountVectorizer / TF-IDF  

3. **Model Training**  
   - Train multiple ML models (Naive Bayes, Logistic Regression)  

4. **Evaluation**  
   - Accuracy, Precision, Recall, F1-Score  
   - Confusion Matrix  
   - ROC Curve & AUC Score  

---

## Results  
- **Logistic Regression Accuracy**: ~97%  
- **Naive Bayes Accuracy**: ~97%  

Both models performed well, with Logistic Regression showing slightly better performance.  

---

## Dataset  
The dataset contains labeled email messages as **Spam (1)** or **Not Spam (0)**.  
- Text data is preprocessed (stopword removal, stemming, punctuation removal).  
- Features extracted using **Bag of Words / TF-IDF** techniques.  

*Dataset Source : https://www.kaggle.com/datasets/suraj452/mail-data*

---
