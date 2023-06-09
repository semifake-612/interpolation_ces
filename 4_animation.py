import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f2(x):
  #  xx = x[0]**2 - x[1] - 2
  #  yy = x[0] * x[1] + 1
    return np.array([x[0]**2 - x[1] - 2, x[0] * x[1] + 1])
def Df2(x):
 #   Dx0 = 2*x[0]
 #   Dx1 = x[1]
 #   Dy0 = -1
 #   Dy1 = x[0]
    return np.array([[2*x[0], x[1]], [-1, x[0]]])

def log_transform(l):
    return (2**(0.5 * l+1)) / (2**(0.5 * l) + 1) - 1
def atan_transform(l): #we could use this, but we don't.
    return (2*np.arctan(l)/np.pi)
# Generate the input values for the x and y axes using a meshgrid
def error (x1, x0):
    return np.linalg.norm(x1-x0, ord=2)

epsilonJacobian = 0.01

def newton (x0, f, Df, tol, itmax, x = []):
    x = []
    x.append(x0)
    print(f(x0))
    print(Df(x0))
    try:
        x_new  = x[0] - np.linalg.inv(Df(x[0])).dot(f(x[0]))
    except np.linalg.LinAlgError: # be x a vector of real numbers
        epsilonJacobian = 0.01
        print("Jacobian is singular. x gets a slight offset")
        for i in x[0]:
            i -= epsilonJacobian
            x_new  = x[0] - np.linalg.inv(Df(x[0])).dot(f(x[0]))
    x.append(x_new)
    itmax = 0
    while error(x[itmax+1], x[itmax]) > tol * np.linalg.norm(x[itmax], ord=2):
        try:
            x_new  = x[itmax+1] - np.linalg.inv(Df(x[itmax+1])).dot(f(x[itmax+1]))
        except np.linalg.LinAlgError:
            
            print("Jacobian is singular. x gets a slight offset")
            for i in x[itmax + 1]:
                i -= epsilonJacobian
            x_new  = x[itmax+1] - np.linalg.inv(Df(x[itmax+1])).dot(f(x[itmax+1]))
        x.append(x_new)
        itmax += 1
    return x, itmax

def plot_R2(x_it, fx): # be x_it domain, and fx image
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    for i in range(len(x_it)):
        #coord = [x_it[i][0], x_it[i][1], fx[i][0]]
    #print(coord)
        print(fx[i][1])
        print("Color (normalized)")
        color__ = log_transform(fx[i][1]) 
        print(color__)
        if color__ >= 0:
            ax.scatter(x_it[i][0], x_it[i][1], fx[i][0], c = (1-color__, 1, 1), edgecolors = (0,0,0))
        else: 
            ax.scatter(x_it[i][0], x_it[i][1], fx[i][0], c = (1, 1-abs(color__), 1), edgecolors= (0, 0, 0))
    fig.show() 
    s = None
    while (input() == None):
        pass

def main():
    plt.ion()

    x1_0 = np.array ([1,2])
    itmax = 5
    print("Root starting at ") 
    print(x1_0)
    x_it, itmax = newton(x1_0, f2, Df2, 0.00001, itmax)
    print (x_it)
    print("Iterations")
    print (itmax)
    fx = []
    for i in x_it:
        fx.append(f2(i))
    print(fx)
    plot_R2(x_it, fx)


        
main()
