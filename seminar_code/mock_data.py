import pandas as pd
import numpy as np

# Create data for one person
np.random.seed(0)
ages = np.arange(20, 41)  # Age from 20 to 40
data = pd.DataFrame({
    'age': ages,
    'bmi': np.random.uniform(18.5, 30, size=len(ages)),  # Random BMI values
    'blood_pressure': np.random.uniform(80, 130, size=len(ages)),  # Random blood pressure values
    'cholesterol': np.random.uniform(150, 250, size=len(ages)),  # Random cholesterol levels
    'exercise': np.random.randint(0, 2, size=len(ages)),  # Random exercise data
    'target': np.random.randint(0, 2, size=len(ages))  # Random target values
})

# Save to CSV
data.to_csv('individual_data.csv', index=False)

print("Dataset created and saved as 'individual_data.csv'.")
