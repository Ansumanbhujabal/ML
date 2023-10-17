# -*- coding: utf-8 -*-
"""Neurolab .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yecqeVyjsN6aF4sB-yPjVTl7cl7zyeXt

## **IMPORT**
"""

!pip install neurolab

import numpy as np
import neurolab as nl

"""# Create train samples

"""

input_data = np.random.uniform(-0.5, 0.5, (10, 2))
target_data = (input_data[:, 0] + input_data[:, 1]).reshape(10, 1)
net = nl.net.newff([[-0.5, 0.5], [-0.5, 0.5]], [5, 1])

"""## Train the network"""

err = net.train(input_data, target_data, show=15)

"""## **Test the network**"""

output = net.sim([[0.2, 0.1]])  # 0.2 + 0.1

# Print the output
print("Network output for [0.2, 0.1]:", output)

