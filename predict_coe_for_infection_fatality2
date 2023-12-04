import numpy as np
from scipy.optimize import curve_fit
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('D:/桌面/AMath383/final/ddd3.csv')  # Replace with your CSV file path
H_values = data['infection_fatality'].values


X = H_values[:-1]
y = H_values[1:]

def model_function(H_k, a, b,c,d,e):
    return a * H_k + b * H_k**2 + c*H_k**3 + d*H_k**4 + e

params, params_covariance = curve_fit(model_function, X, y)

a_opt, b_opt, c_opt,d_opt,e_opt= params

# Using the optimized coefficients to predict the infection fatality values
predicted_values = model_function(H_values[:-1], a_opt, b_opt, c_opt, d_opt, e_opt)

# Preparing dates for plotting (excluding the last date as the prediction is one step ahead)
data['sequential_number'] = range(1, len(data) + 1)
sequential_number = data['sequential_number']
plot_dates = sequential_number[:-1]

# Plotting both original and predicted data
plt.figure(figsize=(12, 6))
plt.scatter(plot_dates, H_values[:-1], label='Original Data', color='blue')
plt.plot(plot_dates, predicted_values, label='Predicted Data', color='green', linestyle='dashed', linewidth=2)
plt.title('Original vs Predicted Infection Fatality Rate')
plt.xlabel('Date')
plt.ylabel('Infection Fatality Rate')
plt.legend()
plt.grid(True)
plt.show()
print(params)
