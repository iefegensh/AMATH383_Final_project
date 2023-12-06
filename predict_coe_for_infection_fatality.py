import numpy as np
from scipy.optimize import curve_fit
import pandas as pd

data = pd.read_csv('C:/Users/86130/Desktop/AMATH383/project/ddd3.csv')  # Replace with your CSV file path
H_values = data['infection_fatality'].values


X = H_values[:-1]
y = H_values[1:]

def model_function(H_k, a, b,c,d):
    return a * H_k + b * H_k**2 + c*H_k**3+d*H_k**4

params, params_covariance = curve_fit(model_function, X, y)

a_opt, b_opt, c_opt,d_opt= params

print(f"Optimized parameters: a = {a_opt}, b = {b_opt}, {c_opt},{d_opt}")
