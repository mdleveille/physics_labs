"""define functions for use in calculating quantities in ballistic pendulum lab"""
import numpy as np
g = 9.81 # m/s**2

def vb(d,y0):
	"""computes the muzzle velocity of the ball given d and y0"""
	return d*(g/(2*y0))**0.5

def vbp(d,y0,mb,mp):
	"""computes the velocity of the ball/pendulum given d,y0,mb,mp"""
	return mb*vb(d,y0)/(mb+mp)

def theta(d,y0,mb,mp,l):
	"""computes the angle given d,y0,mb,mp, and l"""
	th = (180/np.pi)*np.arccos(1-vbp(d,y0,mb,mp)**2/(2*l*g))
	return th