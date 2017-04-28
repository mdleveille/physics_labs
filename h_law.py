# import matplotlib.pyplot as plt 
# import numpy as np
# from scipy import polyfit
from pylab import *
from scipy.constants import g

## near spring
# x0 = 0.852
# m = array([50,100,150,200,250,300,350,400,450,500,])
# x = array([81.6,78.2,74.7,71.3,67.8,64.3,60.7,57.4,53.8,50.2])


## middle spring
#x0 = 1.306
# m = array([200,300,400,500,600,700,800,900,1000,1500,2000])
# x = array([130.3,129.4,128.4,127.6,126.6,125.7,124.8,123.8,122.8,118.3,113.7])

## far spring
x0 = 0.893
m = array([50,100,150,200,250,300,350,400,450,500,])
x = array([86.0,82.6,79.1,75.6,72.00,68.6,65.1,61.5,58.0,54.3])

m = m/1000
x = x/100
del_x = x0-x

# Best fit line
slope,b = polyfit(del_x,m,1)


k = slope*g
print('The spring constant is %.2f N/m' % (k))

x_cont = linspace(x0-x[0],x0-x[len(x)-1])
m_cont = slope*x_cont + b

plot(del_x,m,'bo')
plot(x_cont,m_cont,'r-')
xlabel(r'Displacement, [$m$]')
ylabel(r'Mass, [$kg$]')
show()

def T(m):
	return 2*pi*sqrt(m/k)