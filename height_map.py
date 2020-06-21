import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

print("Enter file path : ")
path = input()
print("Enter number of planes to be aggregated: ")
z = int(input())
# path="C:/Users/sony/Downloads/Pf01.bin/Pf01.bin"
f=open(path, "rb");

data = np.fromfile(f, dtype='>f');

datad = []
outlier = str(1.e+35)
for index in range(data.size):
    if (str(data[index]) != outlier):
        datad.append(data[index])

dim_x = 500
dim_y = 500
dim_z = 100
n = int(dim_z/z)
aggData = [[[0 for i in range(dim_y)] for j in range(dim_x)] for k in range(n)]

p=0
for indexNz in range(n):
    for indexX in range(500):
        for indexY in range(500):
            totalValue = 0.0;
            for indexZ in range(p,p+z):
                totalValue = data[(indexX + (500*(indexY + (500*(indexZ)))))] + totalValue
            avgValue = totalValue/10;
            aggData[indexNz][indexX][indexY] = avgValue
    p=p+z

xmind=min(data)
xmaxd=max(datad)

z = np.array([[0 for i in range(dim_y)] for j in range(dim_x)])
x = np.arange(0,500,100)
y = np.arange(0,500,100)
X,Y = np.meshgrid(x,y)

for indexZ in range(n):
    for indexX in range(dim_x):
        for indexY in range(dim_y):
            if (aggData[0][indexX][indexY] < xmaxd) :
                z[indexX][indexY] = ((aggData[indexZ][indexX][indexY]))

    x, y = np.meshgrid(range(z.shape[0]), range(z.shape[1]))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x,y,z, color='blue')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()