# -*- coding: utf-8 -*-
"""Loan Status Prediction .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wz6mqKE8sNQttuHNlzPGh22GdzedBzOb

# **IMPORT**
"""

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

data = pd.read_csv('/content/loan_dataset.csv')

data.head()

data.shape

data.describe()

"""# **Checking Missing Values**"""

data.isnull().sum()

"""# Handling Missing Values by Dropping"""

data = data.dropna()

data.isnull().sum()

"""# Label Encoding"""

data.replace({"Loan_Status": {'N': 0, 'Y': 1}}, inplace=True)

data.head()

"""# **Dependent Column Values**"""

data['Dependents'].value_counts()

# Replacing the value of 3+ as 4
data = data.replace(to_replace='3+', value=4)

data['Dependents'].value_counts()

"""# **Visualizing Education and Loan**"""

sns.countplot(x='Education', hue='Loan_Status', data=data)

"""# **Marital Status And Loan**"""

sns.countplot(x='Married', hue='Loan_Status', data=data)

"""## **Label Encoding Of Categorical Values**"""

data = data.replace({'Married': {'No': 0, 'Yes': 1}, 'Gender': {'Male': 1, 'Female': 0}, 'Education': {
                    'Not Graduate': 0, 'Graduate': 1}, 'Property_Area': {'Rural': 0, 'Urban': 1, 'Semiurban': 2}, 'Self_Employed': {'Yes': 1, 'No': 0}})

data.head()

"""# **Data And Label**"""

X = data.drop(columns=['Loan_ID', 'Loan_Status'], axis=1)
Y = data['Loan_Status']

print(X)

print(Y)

"""# **Train Test Split**"""

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""# **Model Training**"""

classifier = svm.SVC(kernel='linear')

classifier.fit(X_train, Y_train)

"""# **Model Evaluation**"""

X_train_prediction = classifier.predict(X_train)
train_accuracy = accuracy_score(X_train_prediction, Y_train)

print(train_accuracy)

"""**On Test Data**"""

X_test_prediction = classifier.predict(X_test)
teat_accuracy = accuracy_score(X_test_prediction, Y_test)

print(teat_accuracy)

"""# **Predictive System**"""

input_data = ('LP001002', 'Male', 'No', 0, 'Graduate',
              'No', 5849, 0, 0, 360, 1, 'Urban')
data = np.asarray(input_data)

data = data.replace({"Loan_Status": {'N': 0, 'Y': 1}, 'Married': {'No': 0, 'Yes': 1}, 'Gender': {'Male': 1, 'Female': 0}, 'Education': {
                    'Not Graduate': 0, 'Graduate': 1}, 'Property_Area': {'Rural': 0, 'Urban': 1, 'Semiurban': 2}, 'Self_Employed': {'Yes': 1, 'No': 0}})


# Assuming 'input_data' is a NumPy array
input_data = np.array(['LP001002', 'Male', 'No', 0,
                      'Graduate', 'No', 5849, 0, 0, 360, 1, 'Urban'])

# Convert the NumPy array to a pandas DataFrame
input_df = pd.DataFrame([input_data], columns=['ID', 'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
                                               'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term',
                                               'Credit_History', 'Property_Area'])

# Label encoding for input_df
input_df.replace({'Married': {'No': 0, 'Yes': 1},
                  'Gender': {'Male': 1, 'Female': 0},
                  'Education': {'Not Graduate': 0, 'Graduate': 1},
                  'Property_Area': {'Rural': 0, 'Urban': 1, 'Semiurban': 2},
                  'Self_Employed': {'Yes': 1, 'No': 0}}, inplace=True)

# Handle 'Dependents' column (if necessary)
input_df['Dependents'] = input_df['Dependents'].replace(
    to_replace='3+', value=4)

# Extract features for prediction
features = input_df.drop(columns=['ID'])

# Make prediction
loan_status_prediction = classifier.predict(features)

# Convert prediction to human-readable format
if loan_status_prediction[0] == 1:
    prediction_result = 'Approved'
else:
    prediction_result = 'Not Approved'

print("Loan Status Prediction for the input data: {}".format(prediction_result))