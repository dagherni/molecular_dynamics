import numpy as np
import matplotlib.pyplot as plt
import math 
import mpl_toolkits.mplot3d.axes3d as p3
#import fill_init_pos, fill_init_mom, particleClass, calc_force, sum_forces, plotthings, changemom, changepos from 
import moleculardynamicsfinal as mo

#set global constants
Np=864
m = int((Np/4)**(1.0/3)+0.01) #amount of unit cells per direction
sigma=445
epsilon=5
deltat=.000000006
mass=6.63*10**(-23)


particles = mo.particleClass(Np,m)
for i in range(5):
    mo.particles.momenta=mo.changemom(deltat,mo.particles.momenta,mo.particles.forces)
    mo.particles.positions=m.changepos(deltat,mo.particles.momenta,mo.particles.positions,mass)
    mo.particles.forces=m.sum_forces(mo.particles.positions,mo.partilces.forces,Np,m,sigma,epsilon)
    mo.plotthings(mo.particles.positions,Np)

