import numpy as np
from scipy.optimize import curve_fit
import pandas as pd

# Load data from CSV file
data = pd.read_csv('C:/Users/86130/Desktop/AMATH383/project/ddd3.csv')
X = data['sequential_number'].values[:-1]
y = data['hospital_beds_mean'].values[1:]

def model_function(X, a, b, c, d, e):
    k = X
    H_k = data['hospital_beds_mean'].values[:-1]
    return a * k + b * H_k + c * H_k**2 + d *H_k**3 + e

initial_guess = [100, -111, 12.2, -33, 1]

params_opt, params_cov = curve_fit(model_function, X, y, p0=initial_guess)

a_opt, b_opt, c_opt, d_opt, e= params_opt
print(f"Optimized parameters: a = {a_opt}, b = {b_opt}, c = {c_opt}, d = {d_opt}, {e}")
