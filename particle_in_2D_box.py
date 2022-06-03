from mpl_toolkits import mplot3d
from matplotlib import pyplot as plt
import numpy as np


L=1

def f(x,y):
    return (2/L)*np.sin(((np.pi)*x)/L)*np.sin(((np.pi)*y)/L)

x = np.linspace(-1,1, 10)
y = np.linspace(-1,1,10)

X,Y = np.meshgrid(x,y)
Z = f(X,Y)

fig = plt.figure()

ax = plt.axes(projection='3d')

#ax.set_xvariable('x')
#ax.set_yvariable('y')
#ax.set_zvariable('z')


ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='viridis',edgecolor='none')
ax.set_title('Particle in 2D box')

plt.show()
