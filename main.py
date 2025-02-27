import numpy as np                           
import matplotlib.pyplot as plt              

#Importing functions from personalized modules

from src.sigmoid import sigmoid             # Sigmoid funcion
from src.step import step                  # Step function
from src.gaussian import gaussian            # Gaussian function
from src.identity import identity             # Identity function
from src.piecewise import piecewise     # Piecewise function
from src.relu import relu                     # ReLU Function (Rectified Linear Unit)
from src.sine import sinusoidal         # Sine function
from src.tangent import tanh     # Hyperbolic tangent function  

def main():
    # Define a range of values to plot in the x axis
    x = np.linspace(-10, 10, 400)
    
    # Calculate the output of each function with a vector given by x
    y_sigmoid     = sigmoid(x)
    y_step        = step(x)
    y_gaussian    = gaussian(x)
    y_identity    = identity(x)
    y_piecewise   = piecewise(x)
    y_relu        = relu(x)
    y_sinusoidal  = sinusoidal(x)
    y_tanh        = tanh(x)
    
    # Configure the plot and the subplots
    fig, axs = plt.subplots(4, 2, figsize=(12, 12))
    axs = axs.flatten()  # Convertimos la matriz de ejes en un arreglo unidimensional para facilitar la asignación
    
    # Plotting each function with its title
    axs[0].plot(x, y_sigmoid)
    axs[0].set_title("Sigmoid")
    
    axs[1].plot(x, y_step)
    axs[1].set_title("Step")
    
    axs[2].plot(x, y_gaussian)
    axs[2].set_title("Gaussian")
    
    axs[3].plot(x, y_identity)
    axs[3].set_title("Identity")
    
    axs[4].plot(x, y_piecewise)
    axs[4].set_title("Piecewise")
    
    axs[5].plot(x, y_relu)
    axs[5].set_title("ReLU")
    
    axs[6].plot(x, y_sinusoidal)
    axs[6].set_title("Sine")
    
    axs[7].plot(x, y_tanh)
    axs[7].set_title("Hyperbolic tangent")
    
    # Adjust the layour of the plots to avoid overlapping the figures
    plt.tight_layout()
    # Show the plots
    plt.show()

# This ensures that main() is executed only when the script is executed directly
if __name__ == "__main__":
    main()
