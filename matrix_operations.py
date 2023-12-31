# -*- coding: utf-8 -*-
"""Matrix_Operations.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15dBG3BHVFlaiQBpmLV5JylJeFe8RLlmC

# **IMPORT**
"""

import numpy as np
import pandas as pd

"""**Add**"""

a= np.array([[2,3],[4,5]])
b= np.array([[6,7],[8,9]])
# c= a+b
# another way
c= np.add(a,b)
print(c)

m= np.random.randint(10, size=(2,3))
n= np.random.randint(10, size=(2,3))
print(m+n)

"""**subtract**"""

# k= c-b
# another way
k= np.subtract(c,b)
print(k)

print(m-n)

"""# **Multiplication**

**by scalar**
"""

# l= a*3
#other way
l=np.multiply(a,3)
print(l)

"""**by vector**"""

# j= a*b
# other way
j = np.multiply(a,b)
print(j)

