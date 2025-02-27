import numpy as np
import matplotlib.pyplot as plt

'''
Defining the step function
'''
def step(x):
    return np.where(x >= 0, 1, 0) #Return 1 if x>=0 and 0 if x<0

'''
Defining the derivative
'''
def step_derivative(x):
    return np.zeros_like(x) #Create a list with the same size as "x", full of zeros

'''
400 points from -10 to 10.
'''
x = np.linspace(-10, 10, 400)
y = step(x) #evaluate each value of x in the step function
dy = step_derivative(x) #evaluate each value of x in the step_derivative function

'''
plot
'''
plt.figure(figsize=(8, 5)) 
plt.plot(x, y, label='Step') 
plt.plot(x, dy, label='Step derivative', linestyle='dashed') 
plt.axhline(0, color='black', linewidth=0.5) 
plt.axvline(0, color='black', linewidth=0.5) 
plt.title("Step function and its derivative") 
plt.legend() 
plt.grid() 
plt.show() 
