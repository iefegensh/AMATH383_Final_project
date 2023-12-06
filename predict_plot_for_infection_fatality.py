import pandas as pd
import matplotlib.pyplot as plt

H0 = 0.0192
a = 0.9802926923188372
b = 1.0773020272434675
c=-6.75877098709384
d=-170.58994120629634

H = [H0]
for i in range(60):
    H0 = a * H0 + b * H0**2 * c*H0**3 + d*H0**4
    H.append(H0)

data = pd.read_csv('C:/Users/86130/Desktop/AMATH383/project/ddd3.csv')
data['sequential_number'] = range(1, len(data) + 1)

plt.figure(figsize=(10, 6))
plt.scatter(data['sequential_number'], data['infection_fatality'], label='Original Data')
plt.plot(range(61), H, color='green', label='Model Prediction')
plt.title('infection_fatality Over Time')
plt.xlabel('Sequential Number')
plt.ylabel('infection_fatality')
plt.legend()
plt.grid(True)
plt.show()
