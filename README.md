# heart-disease-predictor
 Heart disease risk prediction web app built with Streamlit and scikit-learn


Heart Disease Risk Predictor
A machine learning web application that predicts the likelihood of heart disease in a patient based on 13 clinical features including age, sex, chest pain type, blood pressure, cholesterol, and exercise-related measurements.
How it works:

The app is powered by a Logistic Regression model trained on the UCI Heart Disease dataset (303 patients, Cleveland clinic). The model achieves 88.5% accuracy and 90.6% sensitivity on unseen patients — meaning it correctly identifies 9 out of 10 patients who actually have heart disease.
A user enters a patient's clinical measurements into the form, clicks Predict, and the app returns an instant risk assessment with a probability score — for example, "High risk of heart disease — 98.9% probability."
Built with: Python, scikit-learn, Pandas, Streamlit
Deployed at: https://heart-disease-predictor-bl4wdyed4yngvi5kyccpoc.streamlit.app/
Dataset: UCI Machine Learning Repository — Heart Disease Dataset (Cleveland)
