import pandas as pd
import matplotlib.pyplot as plt

# Optimized coefficients from the curve fitting
a = 1.111541924383468
b = -5.0790246437777995
c = 114.4859838535092
d = -1023.196605079298
e = -0.000983384177513787

data = pd.read_csv('D:/桌面/AMath383/final/ddd3.csv')
data2 = pd.read_csv('D:/桌面/AMath383/final/ddd2.csv')

import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

H_values = data['infection_fatality'].values
H_original = data2['infection_fatality'].values

# Define the model function with the optimized parameters
def model_function(H_k, a, b, c, d, e):
    return a * H_k + b * H_k**2 + c * H_k**3 + d * H_k**4 + e

# Fit the model to get the parameters (using the last known coefficients here as an example)
params, _ = curve_fit(model_function, H_values[:-1], H_values[1:])
a_opt, b_opt, c_opt, d_opt, e_opt = params

# Predict future values using the last known infection fatality rate
H_last = H_values[-1]  # The last known value
num_future_predictions = 60  # Number of future points to predict

# Generate future predictions
H_future = [H_last]
for _ in range(num_future_predictions):
    H_next = model_function(H_last, a_opt, b_opt, c_opt, d_opt, e_opt)
    H_future.append(H_next)
    H_last = H_next

# Create an extended x-axis for the original and future values
sequential_numbers = list(range(1, len(H_values) + num_future_predictions + 1))

# Plot the original and predicted infection fatality rates
plt.figure(figsize=(12, 6))
plt.scatter(sequential_numbers[:len(H_values)], H_values, label='Original Data', color='blue')
plt.plot(sequential_numbers[len(H_values)-1:], H_future, label='Predicted Future Values', color='green', linestyle='dashed', linewidth=4)
plt.title('Infection Fatality Rate with Future Predictions')
plt.xlabel('Sequential Number')
plt.ylabel('Infection Fatality Rate')
plt.legend()
plt.grid(True)
plt.show()
