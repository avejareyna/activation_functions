import numpy as np
import matplotlib.pyplot as plt
'''
Defining the tanh function
'''
def tanh(x):
    return np.tanh(x) #This function maps any value to the range from -1 to 1
'''
Defining the derivative of tanh
'''
def tanh_derivative(x):
    return 1 - np.tanh(x)**2 

'''
Generate 400 points from -3 to 3
'''
x = np.linspace(-3, 3, 400)
y = tanh(x) # Evaluate the tanh function
dy = tanh_derivative(x) # Evaluate the derivative of tanh

'''
Plot
'''
plt.figure(figsize=(8, 5)) 
plt.plot(x, y, label='Hyperbolic tangent') 
plt.plot(x, dy, label='Derivative of the tanh', linestyle='dashed') 
plt.axhline(0, color='black', linewidth=0.5) 
plt.axvline(0, color='black', linewidth=0.5) 
plt.title("Tanh and its derivative") 
plt.legend() 
plt.grid() 
plt.show() 
