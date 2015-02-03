import numpy as np
import matplotlib.pyplot as plt
import math 
import mpl_toolkits.mplot3d.axes3d as p3
#import fill_init_pos, fill_init_mom, particleClass, calc_force, sum_forces, plotthings, changemom, changepos from 
import moleculardynamicsfinal as m

#set global constants
Np=864
m = int((Np/4)**(1.0/3)+0.01) #amount of unit cells per direction
sigma=445
epsilon=5
deltat=.000000006
mass=6.63*10**(-23)


particles = m.particleClass(Np)
for i in range(5):
    m.particles.momenta=m.changemom(deltat,m.particles.momenta,m.particles.forces)
    m.particles.positions=m.changepos(deltat,m.particles.momenta,m.particles.positions,mass)
    m.particles.forces=m.sum_forces(m.particles.positions,m.partilces.forces,Np)
    
