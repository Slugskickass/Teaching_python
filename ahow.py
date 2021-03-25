import matplotlib.pyplot as plt
import numpy as np

def phi(x,y):
    '''This is a function for The quantum wave function for a particle in a 2D box of side L
    variables are:
    x,y,nx,ny,L'''


    return (2/L)*(np.sin((nx*np.pi*x)/L))*(np.sin((ny*np.pi*y)/L))



n=100 #using 100 data points between 0 and 1

x=np.linspace(0,1,n)
y=np.linspace(0,1,n)
nx,ny=1,2
L=1

X,Y=np.meshgrid(x,y)

phia = np.vectorize(phi) # was getting this error so had to put in this line 'only size-1 arrays can be converted to python scalars'

#print(phia)

fig=plt.figure()
ax=fig.gca(projection='3d')
ax.plot_surface(X, Y, phia(X, Y), cmap='Reds')
plt.xlabel('x')
plt.ylabel('y')    # labeling axis'
ax.set_zlabel('phi')
plt.minorticks_on()  #adds indents to axis to make it easier to read
plt.title('graph for phi')   # adds title to graph
plt.show()

fig=plt.figure()
con=plt.contourf(X, Y, phia(X, Y))  # contour
cbar=fig.colorbar(con)
cbar.set_label('phi')
plt.xlabel('x')
plt.ylabel('y')
plt.title('contour for phi')
plt.show()

my_data = phi(0.5, y)
plt.plot(my_data)
plt.show()
