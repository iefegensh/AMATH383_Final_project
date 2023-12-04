import pandas as pd
import matplotlib.pyplot as plt

H0 = 134.23
a = -73.94261294332631
b = 1.2389006279320247
c = -2.49885417520337e-06
d = -5.828273397340896e-12
e = 946.9485783245336
f = -1227.393250676133
H = [H0]
for i in range(120):
    H0 = a * (i+1) + b * H0 + c * H0**2 + d *H0**3 + e + f/(i+1)
    H.append(H0)

data = pd.read_csv('C:/Users/86130/Desktop/AMATH383/project/ddd4.csv')
data['sequential_number'] = range(1, len(data) + 1)


plt.figure(figsize=(10, 6))
plt.scatter(data['sequential_number'], data['hospital_beds_mean'], label='Original Data')
plt.plot(range(121), H, color='green', label='Model Prediction')
plt.title('Hospital Beds Mean Over Time')
plt.xlabel('Sequential Number')
plt.ylabel('Hospital Beds Mean')
plt.legend()
plt.grid(True)
plt.show()
