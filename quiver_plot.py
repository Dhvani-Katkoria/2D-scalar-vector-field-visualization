import numpy as np
import matplotlib.pyplot as plt

print("Enter x,y file path : ")
pathX = input()
pathY = input()
print("Enter number of planes to be aggregated: ")
z = int(input())

# path="C:/Users/sony/Downloads/Uf01.bin/Uf01.bin"
f1=open(pathX, "rb")
# path="C:/Users/sony/Downloads/Uf01.bin/Uf01.bin"
f2=open(pathY, "rb")

dataX = np.fromfile(f1, dtype='>f')
dataY = np.fromfile(f2, dtype='>f')

outlier = 1.e+35;
dim_x = 500
dim_y = 500
dim_z = 100
n = int(dim_z/z)
aggDataX = [[[0 for i in range(dim_y)] for j in range(dim_x)] for k in range(n)]
aggDataY = [[[0 for i in range(dim_y)] for j in range(dim_x)] for k in range(n)]

normDataX = [[[0 for i in range(150)] for j in range(150)] for k in range(n)]
normDataY = [[[0 for i in range(150)] for j in range(150)] for k in range(n)]

p=0
for indexNz in range(n):
    for indexX in range(dim_x):
        for indexY in range(dim_y):
            totalValue = 0.0;
            for indexZ in range(p,p+z):
                totalValueX = dataX[(indexX + (500 * (indexY + (500 * (indexZ)))))] + totalValue
                totalValueY = dataY[(indexX + (500 * (indexY + (500 * (indexZ)))))] + totalValue
            avgValueX = totalValueX / z;
            avgValueY = totalValueY / z;
            aggDataX[indexNz][indexX][indexY] = avgValueX
            aggDataY[indexNz][indexX][indexY] = avgValueY
    p=p+z

p=50
x=0
y=0
U = DataX[:,:,10]
V = DataY[:,:,10]
P = DataP[:,:,10]
normDataX = [[0 for i in range(p)] for j in range(p)]
normDataY = [[0 for i in range(p)] for j in range(p)]
normDataP = [[0 for i in range(p)] for j in range(p)]

for indexX in range(0,dim_x,10):
    for indexY in range(0,dim_y,10):
#         if (str(aggDataX[indexX][indexY])!=str(outlier) and str(aggDataY[indexX][indexY])!=str(outlier)):
        normDataX[x][y] = U[indexX][indexY]
        normDataY[x][y] = V[indexX][indexY]
        normDataP[x][y] = P[indexX][indexY]
        
#         else:
#             normDataX[x][y] = 0.0#aggDataX[indexX][indexY]
#             normDataY[x][y] = 0.0#aggDataY[indexX][indexY]
        y=y+1
    x=x+1
    y=0
    
fig = plt.figure()
ax = fig.add_subplot()
plt.tight_layout()

# im = ax.imshow(normDataP[::-1], cmap=plt.cm.viridis, origin='lower')
# fig.colorbar(im)
# plt.show()
ax.quiver(normDataX[::-1], normDataY[::-1],color='b')
# plt.quiver(U[::-1], V[::-1],color='b')
# plt.matshow(DataP[::-1], cmap=plt.cm.viridis, origin='lower')
plt.show()
