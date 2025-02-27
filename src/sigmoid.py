import numpy as np
import matplotlib.pyplot as plt
'''
Defining sigmoid function
'''
def sigmoid(x):
    '''
    Map any value between the values from 0 to 1
    '''
    return 1 / (1 + np.exp(-x))
'''
Define the derivative of the sigmoid
'''
def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x)) # Derivate the sigmoid

'''
400 points from -10 to 10
'''
x = np.linspace(-10, 10, 400)
y = sigmoid(x) # Evaluate the function for each value of x
dy = sigmoid_derivative(x) # Evaluate the derivative

'''
Plot
'''
plt.figure(figsize=(8, 5)) 
plt.plot(x, y, label='Sigmoid') 
plt.plot(x, dy, label='Derivative of the sigmoid function', linestyle='dashed') 
plt.axhline(0, color='black', linewidth=0.5) 
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Sigmoid function and its derivative") 
plt.legend() 
plt.grid() 
plt.show() 
