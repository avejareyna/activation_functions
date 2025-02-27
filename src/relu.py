import numpy as np
import matplotlib.pyplot as plt

'''
Defining relu function
'''
def relu(x):
    '''
    return the maximum between 0 and x.
    If x>=0, the function returns x.
    If x< 0, the function returns 0.
    '''
    return np.maximum(0, x) 

'''
Defining the derivative
'''
def relu_derivative(x): 
    '''
    Returns:
    1, if x>0
    0, if x<=0
    '''
    return np.where(x > 0, 1, 0) 

'''
Generate 400 values from -3 to 3 stored in x
'''
x = np.linspace(-3, 3, 400)
y = relu(x) #Evaluate relu function with values of x
dy = relu_derivative(x) #Evaluating the derivative for each value of x

'''
Plot
'''
plt.figure(figsize=(8, 5)) 
plt.plot(x, y, label='ReLU') 
plt.plot(x, dy, label='Derivative of ReLU function', linestyle='dashed') 
plt.axhline(0, color='black', linewidth=0.5) 
plt.axvline(0, color='black', linewidth=0.5) 
plt.title("ReLU function and its derivative") 
plt.legend() 
plt.grid() 
plt.show() 
