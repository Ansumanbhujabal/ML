# -*- coding: utf-8 -*-
"""Implementation of Build Linear Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IFkIDw_SgVQc2hWpBuPi5d3T87HPdSXD

## **IMPORT**
"""

import numpy as np

"""# **Linear Regression:**

Y = wX + b

Y --> Dependent Variable

X --> Independent Variable

w --> weight

b --> bias

## **Gradient Descent:**

Gradient Descent is an optimization algorithm used for minimizing the loss function in various machine learning algorithms. It is used for updating the parameters of the learning model.

w = w - α*dw

b = b - α*db

# **Learning Rate:**

Learning rate is a tuning parameter in an optimization algorithm that determines the step size at each iteration while moving toward a minimum of a loss function.

# **Model Building**
"""

class Linear_Regression():

   def __init__( self, learning_rate, no_of_iterations ) :

        self.learning_rate = learning_rate

        self.no_of_iterations = no_of_iterations

    # fit function to train the model

   def fit( self, X, Y ) :

        # no_of_training_examples, no_of_features

        self.m, self.n = X.shape

        # initiating the weight and bias

        self.w = np.zeros( self.n )

        self.b = 0

        self.X = X

        self.Y = Y


        # implementing Gradient Descent for Optimization

        for i in range( self.no_of_iterations ) :

            self.update_weights()



    # function to update weights in gradient descent

   def update_weights( self ) :

        Y_prediction = self.predict( self.X )

        # calculate gradients

        dw = - ( 2 * ( self.X.T ).dot( self.Y - Y_prediction )  ) / self.m

        db = - 2 * np.sum( self.Y - Y_prediction ) / self.m

        # updating the weights

        self.w = self.w - self.learning_rate * dw

        self.b = self.b - self.learning_rate * db


    # Line function for prediction:

   def predict( self, X ) :

        return X.dot( self.w ) + self.b

"""## **IMPORT**"""

import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

"""## **Data Preprocessing**"""

data= pd.read_csv('/content/salary_data.csv')

data.head()

data.tail()

data.shape

"""# **Check Null Value**"""

data.isnull().sum()

"""# **Label Encoding**

"""

X= data.iloc[:,:-1].values
Y= data.iloc[:,1].values

print(X)

print(Y)

"""## **Train Test Split**"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state = 2)

"""## **Model Training**"""

model = Linear_Regression(learning_rate = 0.02, no_of_iterations=1000)

model.fit(X_train, Y_train)

"""# **Weight & Bias**"""

print('weight = ', model.w[0])
print('bias = ', model.b)

"""# **Testing**"""

test_data_prediction = model.predict(X_test)

print(test_data_prediction)

"""### Visualizing Test"""

plt.scatter(X_test, Y_test, color = 'red')
plt.plot(X_test, test_data_prediction, color='blue')
plt.xlabel(' Work Experience')
plt.ylabel('Salary')
plt.title(' Salary vs Experience')
plt.show()
