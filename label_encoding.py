# -*- coding: utf-8 -*-
"""Label Encoding.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xM3rd433IJ-1diKtbT2tcls-gOt8K6vZ
"""

#Importing
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

"""# **Breast cancer Data Label encoding**"""

#loading
cancer= pd.read_csv('/content/breast_cancer_data.csv')
cancer.head()

#How many for M and B
cancer['diagnosis'].value_counts()

#Load the label encoder function
label_encode= LabelEncoder()

labels= label_encode.fit_transform(cancer.diagnosis)

"""# **0---Benign**
## **1---Malignant **
"""

#Appending the labelled to the original dataframe
cancer['target']=labels

cancer.head()

cancer['target'].value_counts()

"""# **Iris Encoding**"""

#Importing
iris=pd.read_csv('/content/iris_data.csv')
iris.head()

#Label count
iris['Species'].value_counts()

#encoding
label2= label_encode.fit_transform(iris.Species)

#joining
iris['target']=label2

#checking
iris['target'].value_counts()

iris.head()

