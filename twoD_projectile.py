import numpy as np

g = 9.8   #m/s^2

del_y = float(input('del_y (in meters) = '))     # distance that the ball goes up minus launch position
theta = float(input('theta (in degrees) = '))    # the angle you want to shoot the ball at
#y0 = float(input('y0 (in meters) = '))           # height of launch position above table surface

# del_y = 1.16 # meters
# theta = 30   # degrees
y0 = 0.265   # meters

v0 = (2*g*del_y)**0.5
#v0 = 4 #m/s 
v0x = v0*np.cos(theta*np.pi/180)
v0y = v0*np.sin(theta*np.pi/180)

a = -0.5*g
b = v0y
c = y0

t1 = (-b+np.sqrt(b**2-4*a*c))/(2*a)
t2 = (-b-np.sqrt(b**2-4*a*c))/(2*a)
print('time 1: %.2f seconds' % (t1))
print('time 2: %.2f seconds' % (t2))

x = v0x*t2
print('the x distance is %.2f meters' % (x))