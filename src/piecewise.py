import numpy as np
import matplotlib.pyplot as plt

'''
Definition of the function
'''
def piecewise(x): #Se define la función lineal a tramos.
    '''
    If x < -1: the function returns -1
    If (-1 <= x) & (x <=1): the funcion returns "x" (a line with slope 1)
    If x > 1: the function returns 1
    '''
    return np.piecewise(x, [x < -1, (-1 <= x) & (x <= 1), x > 1], [-1, lambda x: x, 1])  #función de numpy que permite definir funciones por partes.

'''
Defining the derivative
'''
def piecewise_derivative(x): 
    '''
    If x < -1: the function returns 0
    If (-1 <= x) & (x <=1): the derivative is 1.
    If x > 1: the function returns 0
    '''
    return np.piecewise(x, [x < -1, (-1 <= x) & (x <= 1), x > 1], [0, 1, 0])

'''
Generate 400 evenly spaced points from -3 to 3
'''
x = np.linspace(-3, 3, 400) 
y = piecewise(x) #Evaluate the values of x
dy = piecewise_derivative(x) #Evaluate the values with the derivative

'''
Plot config
'''
plt.figure(figsize=(8, 5)) #Size
plt.plot(x, y, label='Piecewise') 
plt.plot(x, dy, label='Derivative', linestyle='dashed') # Plot of the derivative with a discontinous line
plt.axhline(0, color='black', linewidth=0.5) 
plt.axvline(0, color='black', linewidth=0.5) 
plt.title("Piecewise function with its derivative") 
plt.legend() # Labels
plt.grid() 
plt.show() 
