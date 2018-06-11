import math , numpy as np
#import math


x1=[103.36,129.2,152,161.5,103.36,161.5,161.5,107.67,123.05,198.77,143.55,80.75,136,152,89.1,152,129.2,123.05,136,107.67,129.2,89.1,99.38,68,123.05,61.52,129.2,95.7,129.2]
x2=[201,196,216,201,159,246,153,208,197,191,180,199,145,142,106,93,124,139,127,124,130,136,114,131,89,129,143,104,136]
y=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


w0 = 1
w1 = 1
w2 = 1
a = 0.2



x1min = min(x1)
x1max = max(x1)
x2min = min(x2)
x2max = max(x2)
x1avg = sum(x1)/len(x1)
x2avg = sum(x2)/len(x2)
x1diff = x1max - x1min
x2diff = x2max - x2min


for i in range(len(x1)):
    x1[i] = (x1[i]-x1min)/x1diff
    x2[i] = (x2[i]-x2min)/x2diff


for i in range(5000):
    for j in range(len(x1)):
        a = w0+w1*x1[j]+w2*x2[j]
        h = 1/(1+math.exp(-a))
        dj0 = ((h-y[i])/len(x1))
        dj1 = ((h-y[i])*x1[i]/len(x1))
        dj2 = ((h-y[i])*x2[i]/len(x1))
    w0 = w0 - a*dj0
    w1 = w1 - a*dj1
    w2 = w2 - a*dj2


while(True):
    tem = input('Enter the tempo')
    bt = input('Enter the beats')
    p = w1*tem + w2*bt
    if(p>w0):
        print("good")
    else:
        print("bad")