import numpy as np
import matplotlib.pyplot as plt

'''
Defining the identity function
f(x) = x
'''
def identity(x):
    return x

'''
calculating the derivative
f'(x) = 1, since it's the same function as the input
'''
def identity_derivative(x):
    '''Crea a list of ones with the same size as x'''
    return np.ones_like(x) 

x = np.linspace(-10, 10, 400) #400 values from -10 to 10 stored in x
y = identity(x) #evaluate each value of x 
dy = identity_derivative(x) #the derivative of each value of x

'''
Plot
'''
plt.figure(figsize=(8, 5)) # Size of the graphic
plt.plot(x, y, label='Identity') 
plt.plot(x, dy, label='Derivative of the Identity function', linestyle='dashed') 
plt.axhline(0, color='black', linewidth=0.5) 
plt.axvline(0, color='black', linewidth=0.5) 
plt.title("Identity function and its derivative") 
plt.legend() 
plt.grid() 
plt.show() 
