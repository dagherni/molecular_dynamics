import numpy as np
import matplotlib.pyplot as plt
import math 
import mpl_toolkits.mplot3d.axes3d as p3
#import matplotlib.animation as animation

from moleculardynamicsfinal import fill_init_pos, fill_init_mom, particleClass, calc_force, sum_forces, plotthings, changemom, changepos, checkEnergy, checkMomenta,checkPotential,checkpotentialSUM
#import moleculardynamicsfinal as mo

#set global constants
Np=108
sigma=1
epsilon=1
deltat=.0000004
mass = 1
dens = 0.85
temp = 0.9

particles = particleClass(Np, dens, temp)
print "Starting Energy: ",checkEnergy (Np,particles.momenta,particles.positions,mass,particles.L)
print "Starting Momentum: ",checkMomenta(particles.momenta)

for i in range(10):
  particles.momenta=changemom(deltat,particles.momenta,particles.forces)
  particles.positions=changepos(deltat,particles.momenta,particles.positions,mass, particles.L)
  particles.forces=sum_forces(particles.positions,particles.forces,Np,particles.L)
  #print i,"th Energy: ",checkEnergy(Np,particles.momenta,particles.positions,mass,particles.L)
 # print i, "the potenital: ",checkpotentialSUM(particles.positions,Np,particles.L)
  #print i,"th Momentum: ",checkMomenta(particles.momenta)
  #plotthings(particles.positions,Np)

print "End Energy: ",checkEnergy (Np,particles.momenta,particles.positions,mass,particles.L)
print "End Momentum: ",checkMomenta(particles.momenta)

"""
particles = mo.particleClass(Np,m)
#for i in range(5):
mo.particles.momenta=mo.changemom(deltat,mo.particles.momenta,mo.particles.forces)
mo.particles.positions=mo.changepos(deltat,mo.particles.momenta,mo.particles.positions,mass)
mo.particles.forces=mo.sum_forces(mo.particles.positions,mo.partilces.forces,Np,m,sigma,epsilon)
mo.plotthings(mo.particles.positions,Np)

"""
