# 🩺 Diabetes Prediction using Machine Learning (diabates-ML-project)
This project aims to predict the likelihood of diabetes in patients using machine learning models, based on medical history and health-related metrics. It was developed as part of my undergraduate research at Redeemer's University and has since been improved upon as I’ve continued to grow in the field of data science.

## 🔍 Problem Statement
Diabetes is a major public health concern worldwide. Early prediction can help in taking preventive steps and managing the disease more effectively. This project explores various supervised learning models to build a reliable classifier that predicts whether a patient is diabetic based on features like age, gender, BMI, blood glucose level, HbA1c, hypertension, and smoking history.

## 📊 Dataset
The dataset was sourced from Kaggle and contains anonymized patient records with the following attributes:
- gender
- age
- hypertension
- heart_disease
- smoking_history
- bmi
- HbA1c_level
- blood_glucose_level
- diabetes (target)

## 🧠 Models Used
**Four classification algorithms were used and compared:**
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- XGBoost

Each model was trained and evaluated to determine performance on accuracy, precision, recall, F1-score, and AUC-ROC.

## 📈 Results & Insights
XGBoost outperformed other models in most metrics, demonstrating its suitability for structured healthcare data.
Visualizations helped identify correlations and feature importance.
Preprocessing techniques (encoding, normalization) were crucial in improving model performance.

## 🛠️ Tools & Technologies
- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Matplotlib, Seaborn
- Jupyter Notebook

## 📚 What I Learned
- How to evaluate and compare machine learning models rigorously
- Dealing with imbalanced datasets and categorical variables
- Communicating insights with visualizations
- Applying ML to real-world healthcare problems

## 🧑‍💻 Author
**Oluwasegun Isaac Adejuwon**
Aspiring Data Scientist | Passionate about healthcare analytics & impactful machine learning

Feel free to connect with me on LinkedIn or explore other projects on my GitHub.
