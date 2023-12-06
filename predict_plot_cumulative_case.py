import pandas as pd
import matplotlib.pyplot as plt

H0 = 393
a = -1178.9001075514389
b = 0.9715115940005915
c = -1.1170050746589687e-07
d = 3987.5205192166845
e = 64.60294990167476
H = [H0]
for i in range(120):
    H0 = a * (i+1) + b * H0 + c * H0**2 + d + e*(i+1)**2
    H.append(H0)

data = pd.read_csv('C:/Users/86130/Desktop/AMATH383/project/ddd4.csv')
data['sequential_number'] = range(1, len(data) + 1)

plt.figure(figsize=(10, 6))
plt.scatter(data['sequential_number'], data['cumulative_cases'], label='Original Data')
plt.plot(range(121), H, color='red', label='Model Prediction')
plt.title('cumulative_cases Over Time')
plt.xlabel('Sequential Number')
plt.ylabel('cumulative_cases')
plt.legend()
plt.grid(True)
plt.show()
