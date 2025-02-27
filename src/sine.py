import numpy as np
import matplotlib.pyplot as plt
'''
Definition of the sine function
'''
def sinusoidal(x, A=1, omega=1, phi=0):
    '''
    A = amplitude, omega = angular frequency, phi = fase
    '''
    return A * np.sin(omega * x + phi) # Structure of the sine
'''
Defining the derivative of the sine
'''

def sinusoidal_derivative(x, A=1, omega=1, phi=0):
    return A * omega * np.cos(omega * x + phi) # Calculate the cosine

'''
Generate 400 points from -2pi to 2pi
'''
x = np.linspace(-2*np.pi, 2*np.pi, 400)
y = sinusoidal(x) #Evaluate the function for each value of x
dy = sinusoidal_derivative(x) # Evaluate the derivative

'''
Plot
'''
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Sine') 
plt.plot(x, dy, label='derivative of the sine', linestyle='dashed') 
plt.axhline(0, color='black', linewidth=0.5) 
plt.axvline(0, color='black', linewidth=0.5) 
plt.title("sine function and its derivative") 
plt.legend() 
plt.grid() 
plt.show() 
