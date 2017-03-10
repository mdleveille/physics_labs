import numpy as np
import matplotlib.pyplot as plt 

g = 9.8                     # m*s^-2
c_al = 900                  # J*kg^-1*degC^-1
r = 0.0265                  # cm
m = 0.202                   # kg
M = 5                       # kg 
def delT(N):
	return 2*np.pi*r*M*g*N/(m*c_al)

T = np.arange(5,47)
R = np.array([269.08,255.38,242.46,230.26,218.73,207.85,197.56,187.84,178.65,169.95,161.73,153.95,146.58,139.61,133,126.74,120.81,115.19,109.85,104.8,100,95.447,91.126,87.022,83.124,79.422,75.903,72.56,69.38,66.356,63.48,60.743,58.138,55.658,53.297,51.084,48.905,46.863,44.917,43.062,41.292,39.605])

plt.clf()
plt.plot(T, R,'-k',linewidth=3.0,markersize=5)
plt.xlabel(r'Temperature [$^{\circ}$C]')
plt.ylabel(r'Resistance [K$\Omega$]')
plt.xlim(5,45)
plt.minorticks_on() 
plt.grid(which='both',linestyle='-')

plt.show()