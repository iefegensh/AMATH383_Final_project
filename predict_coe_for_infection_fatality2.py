import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = pd.read_csv('D:/桌面/AMath383/final/ddd3.csv')
data2 = pd.read_csv('D:/桌面/AMath383/final/ddd2.csv')

# Extracting only the first 60 data points
H_values = data['infection_fatality'].values[:60]
H_original = data2['infection_fatality'].values[25:85]  # Adjusted to match the range in data

# Define the model function with the optimized parameters
def model_function(H_k, a, b, c, d, e):
    return a * H_k + b * H_k**2 + c * H_k**3 + d * H_k**4 + e

# Fit the model to get the parameters (using the first 60 points)
params, _ = curve_fit(model_function, H_values[:-1], H_values[1:])
a_opt, b_opt, c_opt, d_opt, e_opt = params

# Generate predictions for the first 60 points
H_predictions = [model_function(H_k, a_opt, b_opt, c_opt, d_opt, e_opt) for H_k in H_values]

# Plot the original and predicted infection fatality rates for the first 60 points
plt.figure(figsize=(12, 6))
plt.scatter(range(1, len(H_original)+1), H_original, label='Original Data', color='blue')
plt.plot(range(1, 61), H_predictions, label='Model Predictions', color='red', linewidth=2)
plt.title('Infection Fatality Rate Predictions for First 60 Data Points')
plt.xlabel('Data Point Number')
plt.ylabel('Infection Fatality Rate')
plt.legend()
plt.grid(True)
plt.show()

print(params)
