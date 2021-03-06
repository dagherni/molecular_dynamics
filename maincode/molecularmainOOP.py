from molecularfunctionsOOP import particleClass
from molecularPhysicalQuantities import PlotPQs
import numpy as np
from JosPlotPy import AnimatedScatter
import molecularPhysicalQuantities as PQ

#matplotlib.pyplot.close("all") #closing all the figures

#set global constants
Np=108
deltat=.004
mass = 1
dens = .85
temp = .10
amountoftimesteps=1000
inittau=0 #tau is the correlation time
endtau=100
amountoftau=20

particles = particleClass(Np, dens, temp,mass)
plots=PlotPQs(particles,amountoftimesteps,deltat)
plots.PlotThings(particles,deltat)


#PQ.plotcorr(particles,inittau,endtau,amountoftau,amountoftimesteps,deltat)
Animation=AnimatedScatter(particles,deltat)
Animation.show()








