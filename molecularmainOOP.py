from molecularfunctionsOOP import particleClass

#set global constants
Np=108
deltat=.004
mass = 1
dens = 0.85
temp = 0.9

particles = particleClass(Np, dens, temp,mass)
particles.changeForces()
print "Begin:"
particles.checkEnergy ()
particles.checkMomenta()

for i in range(10000):
  #print "i= ",i
  particles.update(deltat)
  #particles.checkEnergy ()
  #particles.checkMomenta()

print "End: "
particles.checkEnergy ()
particles.checkMomenta()
