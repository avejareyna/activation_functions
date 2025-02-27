import numpy as np
import matplotlib.pyplot as plt

'''
Defining the gaussian function
'''
def gaussian(x, A=1): # A represents the amplitude of the function.
    return A * np.exp(-x**2) #Calculate the exponential of "-x^2".

'''
Defining the derivative of the gaussian function
'''
def gaussian_derivative(x, A=1): 
    return -2 * x * gaussian(x, A) 

'''
Generate 400 points to plot from -3 to 3
'''
x = np.linspace(-3, 3, 400) 
y = gaussian(x) 
dy = gaussian_derivative(x) 

plt.figure(figsize=(8, 5)) 
plt.plot(x, y, label='Gaussian') 
plt.plot(x, dy, label='Derivative of the Gaussian function', linestyle='dashed') 
plt.axhline(0, color='black', linewidth=0.5) 
plt.axvline(0, color='black', linewidth=0.5) 
plt.title("Gaussian function and its derivative") 
plt.legend() 
plt.grid()  
plt.show()

