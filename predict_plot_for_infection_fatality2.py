import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Optimized coefficients from the curve fitting
a = 1.14700702
b = -6.62428260
c = 1.43185595*10**2
d = -1.21573841*10**3
e = -1.27524217*10**-3

data = pd.read_csv('D:/桌面/AMath383/final/ddd3.csv')
data2 = pd.read_csv('D:/桌面/AMath383/final/ddd2.csv')

H_values = data['infection_fatality'].values
H_original = data2['infection_fatality'].values[25:146]

# Define the model function with the optimized parameters
def model_function(H_k, a, b, c, d, e):
    return a * H_k + b * H_k**2 + c * H_k**3 + d * H_k**4 + e

# Fit the model to get the parameters (using the last known coefficients here as an example)
params = a, b, c, d, e
a_opt, b_opt, c_opt, d_opt, e_opt = params

# Generate predictions for the entire range of H_values
H_predictions = [max(model_function(H_k, a_opt, b_opt, c_opt, d_opt, e_opt), 0) for H_k in H_values]

# Predict future values using the last known infection fatality rate
H_last = H_values[-1]
num_future_predictions = 60

# Generate future predictions
for _ in range(num_future_predictions):
    H_next = max(model_function(H_last, a_opt, b_opt, c_opt, d_opt, e_opt), 0)
    H_predictions.append(H_next)
    H_last = H_next

# Create an extended x-axis for the original and future values
sequential_numbers = list(range(1, len(H_predictions) + 1))

# Plot the original and predicted infection fatality rates
plt.figure(figsize=(12, 6))
plt.scatter(sequential_numbers[:len(H_original)], H_original, label='Original Data', color='blue')
plt.plot(sequential_numbers, H_predictions, label='Model Predictions', color='red', linewidth=2)
plt.title('Infection Fatality Rate with Model Predictions')
plt.xlabel('Sequential Number')
plt.ylabel('Infection Fatality Rate')
plt.legend()
plt.grid(True)
plt.show()

print(params)
