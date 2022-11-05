# importing the library
import math
import matplotlib.pyplot as plt
from scipy.misc import derivative
import numpy as np
  
# defining the function
def function(x):
    return x*x/2
  
# calculating its derivative
def deriv(x):
    return derivative(function, x)
  
# defininf x-axis intervals
y = np.linspace(-6, 6)
  
# plotting the function
plt.plot(y, function(y), color='purple', label='Function')
  
# plotting its derivative
plt.plot(y, deriv(y), color='green', label='Derivative')
  
# formatting
plt.legend(loc='upper left')
plt.grid(True)

plt.show()