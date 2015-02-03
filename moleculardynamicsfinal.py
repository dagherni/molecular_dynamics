import numpy as np
import matplotlib.pyplot as plt
import math 
import mpl_toolkits.mplot3d.axes3d as p3
Np=864
m = int((Np/4)**(1.0/3)+0.01) #amount of unit cells per direction
sigma=445
epsilon=5
print "hello world!"

def fill_init_pos(m, positions):
  print "m: ",m
  a=(4.0/n)**(1./3)
  #do things
  positions[0]=[0.0,0.0,0.0]
  positions[1]=[0.5,0.5,0.0]
  positions[2]=[0.5,0.0,0.5]
  positions[3]=[0.0,0.5,0.5]
  counter=0
  for i in xrange(0,m):
    for j in xrange(0,m):
      for k in xrange(0,m):
        positions[counter:counter+4]=positions[0:4]+[i,j,k]
        counter+=4 
  return positions

def fill_init_mom(n,momenta):
  mean,standdev=0,5
  momenta[:,0]=np.random.normal(mean,standdev,n)
  momenta[:,1]=np.random.normal(mean,standdev,n)
  momenta[:,2]=np.random.normal(mean,standdev,n)
  return momenta

class particleClass:
  def __init__(self, n):
    self.positions=np.zeros((n,3),dtype=float)
    self.momenta=np.zeros((n,3),dtype=float)
    self.forces=np.zeros((n,3),dtype=float)
    self.positions = fill_init_pos(n, self.positions)
    self.momenta = fill_init_mom(n, self.momenta)
    self.forces=sum_forces(self.positions,self.forces,n)
  def show(self):
    print "Positions: ", self.positions
    print "Momenta: ", self.momenta
    print "Forces: ",self.forces

def calc_force(particle1,particle2,m,sigma,epsilon):
  deltax= particle2[0]-particle1[0]
  delx2= (m-deltax)
  deltay=(particle2[1]-particle1[1])
  dely2= (m-deltay)
  deltaz=(particle2[2]-particle1[2])
  delz2= (m-deltaz)
  if abs(deltax)>abs(delx2):
    deltax=delx2
  if abs(deltay)>abs(dely2):
    deltay=dely2
  if abs(deltaz)>abs(delz2):
    deltaz=delz2
  r=math.sqrt(deltax**2+deltay**2+deltaz**2)
  F=4*epsilon*((12*sigma**12)/r**13 - (6*sigma**6)/r**7)
  Fx=F*deltax/r 
  Fy=F*deltay/r 
  Fz=F*deltaz/r
  return [Fx,Fy,Fz]

def sum_forces(positions,forces,Np):
	for i in xrange(0,Np):
		for j in xrange(0,Np):
			if i!=j:
				forces[i]+=calc_force(positions[i],positions[j]) 
 	return forces

def plotthings(positions,Np):
    fig= plt.figure()
    ax = fig.gca(projection='3d')
    #ax=Axes3D(fig)
    #plotaxis(5)
    for i in range (0,Np):
        xs,ys,zs = positions[i]
        ax.scatter(xs,ys,zs)
    plt.show()
    
    
def changemom(deltat,momenta,forces):
    momenta += forces*deltat
    return momenta

def changepos(deltat,momenta,positions,mass):
    for i in range(0,m):
        positions[i] += momenta[i]*(deltat/mass)
        for j in positions[i]:
            if j>m:
                j=j-m
    return positions




  
particles = particleClass(Np)
particles.show()
plotthings(particles.positions,Np)

print calc_force(particles.positions[0],particles.positions[1])
