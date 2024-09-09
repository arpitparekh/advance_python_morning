import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# Load the dataset
data = pd.read_csv('individual_data.csv')

# Prepare the data for training
X = data[['age', 'bmi', 'blood_pressure', 'cholesterol', 'exercise']]  # Features
y = data['target']  # Target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest model
model = make_pipeline(StandardScaler(), RandomForestRegressor(n_estimators=100, random_state=42))
model.fit(X_train, y_train)

# Create new data for age 55
new_data = pd.DataFrame({
    'age': [55],
    'bmi': [np.mean(data['bmi'])],  # Use mean BMI from the dataset
    'blood_pressure': [np.mean(data['blood_pressure'])],  # Use mean BP from the dataset
    'cholesterol': [np.mean(data['cholesterol'])],  # Use mean cholesterol from the dataset
    'exercise': [np.mean(data['exercise'])]  # Use mean exercise value from the dataset
})

# Predict the target value for age 55
prediction = model.predict(new_data)
print(f'Predicted target value for age 55: {prediction[0]:.2f}')

# Additional context about the prediction
print("\nAdditional Context:")
print(f"Mean BMI in Dataset: {np.mean(data['bmi']):.2f}")
print(f"Mean Blood Pressure in Dataset: {np.mean(data['blood_pressure']):.2f}")
print(f"Mean Cholesterol in Dataset: {np.mean(data['cholesterol']):.2f}")
print(f"Mean Exercise Level in Dataset: {np.mean(data['exercise']):.2f}")
