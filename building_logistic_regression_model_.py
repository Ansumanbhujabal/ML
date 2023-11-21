# -*- coding: utf-8 -*-
"""Building Logistic Regression Model .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oQCgYGkTTmUgJlEn3BjQnMYD1uLYeVpn

#**Logistic Regression**
![image.png](data:image/png;base64,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)

Y_hat --> predicted value

X --> Input Variable

w --> weight

b --> bias

#**Gradient Descent:**
Gradient Descent is an optimization algorithm used for minimizing the loss function in various machine learning algorithms. It is used for updating the parameters of the learning model.

w = w - α*dw

b = b - α*db

# **Learning Rate:**

Learning rate is a tuning parameter in an optimization algorithm that determines the step size at each iteration while moving toward a minimum of a loss function.

![image.png](data:image/png;base64,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6I8X7DHwZ6y05+T2fbeyd8BM6z7d4evW/ei2df5EYbww3Vpn3MZeAf9994ZvI/ABBHIydjRhgl9ahLmibZfQ1smc5e2W3bo6bkXVe5kfgOnQRejvyc56eL6FTaW+dVHU5Uef9qJvvGUwK88dcJUW/jqNwW7r/EmPTs+f+K7Pk3ym52QvPNddtuvv9DcBAgQI3CDQwSd7jZa9IQunWiWDrfLrSvGe9ZN4pwJUWAIECHxNgQ5A2aNr9muW62jfnQCZFn26Ymf9us/Ryig/BAgQ+PAC6ZJNqyetn/wKkDRPIIEyAbK+s7u/5+XUlggQILCTQO4XdbBT73Vl2ntMHXCR+069r7R133an7N212YyYTdBcD0a5a2M+9Ekg9yzTeo+tblgHBQECpxPIiN4EywxiyjSDlTLoqYGzgTQDLho4O7LY6N/THS4KTIAAAQIRSHBMq3IcjdjRvuOzpAmcHpdxzBAgQIDAaQUSBBMgx9QgOj44nnUSWCUCBAgQIHA6gT43N7YuEyQTRMfWZWAy7+j3ME+3AxWYAAECBN5HYKubdSuIdl7vZ75P7nwLAQIECBA4iEDvVY7ZaRAd/9NK5yVwSgQIECBA4HQCuSe5vn+5da+yATNBNCNptTRPd6goMAECBM4r0N9L3bpXuQ6i/cHsBFjB8rzHjJITIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQ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)

![image.png](data:image/png;base64,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6I8X7DHwZ6y05+T2fbeyd8BM6z7d4evW/ei2df5EYbww3Vpn3MZeAf9994ZvI/ABBHIydjRhgl9ahLmibZfQ1smc5e2W3bo6bkXVe5kfgOnQRejvyc56eL6FTaW+dVHU5Uef9qJvvGUwK88dcJUW/jqNwW7r/EmPTs+f+K7Pk3ym52QvPNddtuvv9DcBAgQI3CDQwSd7jZa9IQunWiWDrfLrSvGe9ZN4pwJUWAIECHxNgQ5A2aNr9muW62jfnQCZFn26Ymf9us/Ryig/BAgQ+PAC6ZJNqyetn/wKkDRPIIEyAbK+s7u/5+XUlggQILCTQO4XdbBT73Vl2ntMHXCR+069r7R133an7N212YyYTdBcD0a5a2M+9Ekg9yzTeo+tblgHBQECpxPIiN4EywxiyjSDlTLoqYGzgTQDLho4O7LY6N/THS4KTIAAAQIRSHBMq3IcjdjRvuOzpAmcHpdxzBAgQIDAaQUSBBMgx9QgOj44nnUSWCUCBAgQIHA6gT43N7YuEyQTRMfWZWAy7+j3ME+3AxWYAAECBN5HYKubdSuIdl7vZ75P7nwLAQIECBA4iEDvVY7ZaRAd/9NK5yVwSgQIECBA4HQCuSe5vn+5da+yATNBNCNptTRPd6goMAECBM4r0N9L3bpXuQ6i/cHsBFjB8rzHjJITIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQ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)

# **import dependencies**
"""

import numpy as np
import pandas as pd

"""# **Logistic Regression**"""

class Logistic_Regression():


  # declaring learning rate & number of iterations (Hyperparametes)
  def __init__(self, learning_rate, no_of_iterations):

    self.learning_rate = learning_rate
    self.no_of_iterations = no_of_iterations



  # fit function to train the model with dataset
  def fit(self, X, Y):

    # number of data points in the dataset (number of rows)  -->  m
    # number of input features in the dataset (number of columns)  --> n
    self.m, self.n = X.shape


    #initiating weight & bias value

    self.w = np.zeros(self.n)

    self.b = 0

    self.X = X

    self.Y = Y


    # implementing Gradient Descent for Optimization

    for i in range(self.no_of_iterations):
      self.update_weights()



  def update_weights(self):

    # Y_hat formula (sigmoid function)

    Y_hat = 1 / (1 + np.exp( - (self.X.dot(self.w) + self.b ) ))


    # derivaties

    dw = (1/self.m)*np.dot(self.X.T, (Y_hat - self.Y))

    db = (1/self.m)*np.sum(Y_hat - self.Y)


    # updating the weights & bias using gradient descent

    self.w = self.w - self.learning_rate * dw

    self.b = self.b - self.learning_rate * db


  # Sigmoid Equation & Decision Boundary

  def predict(self, X):

    Y_pred = 1 / (1 + np.exp( - (X.dot(self.w) + self.b ) ))
    Y_pred = np.where( Y_pred > 0.5, 1, 0)
    return Y_pred