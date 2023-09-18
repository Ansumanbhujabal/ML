# -*- coding: utf-8 -*-
"""Matrix.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GPgtOmethun-BNTA2EfOz3XwdaUp0tDq

# **IMPORT**
"""

import numpy as np
import pandas as pd

m1= np.array([[2,3],[4,5]])
print(m1)

"""# **Creating Matrices with random values**"""

random_matrix= np.random.rand(3,3)
print(random_matrix)
#Default is float

#Random integer matrix
#param-- limit , size
random_int_matrix= np.random.randint(10, size=(3,3))
print(random_int_matrix)

"""**All value as 1**"""

m_3= np.ones((2,3))
print(m_3)

#as int
m_3= np.ones((2,3), dtype=int)
print(m_3)

"""**Null**"""

null_matrix= np.zeros((4,4))
print(null_matrix)

"""# **Identity**"""

identity_matrix = np.eye(3,3)
print(identity_matrix)

"""# **Transpose of a Matrix**"""

a=np.random.randint(10,size=(3,5))
print(a)

transpose_of_a = np.transpose(a)
print(transpose_of_a)

