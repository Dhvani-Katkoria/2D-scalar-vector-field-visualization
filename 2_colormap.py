import matplotlib.pyplot as plt
import numpy as np

print("Enter file path : ")
path = input()
print("Enter number of planes to be aggregated: ")
z=int(input())
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
            avgValue = totalValue/z;
            aggData[indexNz][indexX][indexY] = avgValue
    p=p+z

xmind=min(data)
xmaxd=max(datad)

colormap = []
colorGreen = [0,255,0]
colorBlue = [0,0,255]
colorYellow = [255,255,0]
colorBlack = [0,0,0]
colorRed = [255,0,0]
colorViolet = [148,0,211]
colorIndigo = [75,0,130]
colorOrange = [255,127,0]
colorOrangeRed = [255,65,0]
colorPoint = []
image = np.zeros((dim_x,dim_y,3), np.uint32)

alpha = 0.0
for i in range(n):
    for indexX in range(image.shape[0]):
        for indexY in range(image.shape[1]):
            if (aggData[i][indexX][indexY] > xmaxd) :
                colorPoint = np.add(np.multiply((1 - alpha), colorGreen), np.multiply(alpha, colorBlue))
            else:
                alpha = ((aggData[i][indexX][indexY]) - xmind)/ (xmaxd - xmind)
                colorPoint = np.add(np.multiply((1 - alpha), colorBlue), np.multiply(alpha, colorGreen))
            image[indexX,indexY] = tuple(colorPoint)

    plt.imshow(image)
    plt.show()