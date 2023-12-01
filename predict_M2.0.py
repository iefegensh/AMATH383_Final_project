import pandas as pd
import matplotlib.pyplot as plt

# Initial values and parameters
H0 = 393
a = 1.252565209999886
b = -7.251376882874723*10**(-7)
c=8.594598759521143*10**(-13)
d = -3.614391933965026*10**(-19)
# Generating the predicted values
H = [H0]
for i in range(200):
    H0 = a * H0 + b * H0**2 + c*H0**3 + d*H0**4
    H.append(H0)

# Load the actual data
data = pd.read_csv('C:/Users/86130/Desktop/AMATH383/project/ddd2.csv')
data['sequential_number'] = range(1, len(data) + 1)

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(data['sequential_number'], data['cumulative_cases'], label='Original Data')
plt.plot(range(201), H, color='green', label='Model Prediction')
plt.title('Hospital Beds Mean Over Time')
plt.xlabel('Sequential Number')
plt.ylabel('Hospital Beds Mean')
plt.legend()
plt.grid(True)
plt.show()
