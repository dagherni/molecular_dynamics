import numpy as np
#plotting
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# 3D plotting
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d.art3d import juggle_axes

class AnimatedScatter(object):
    def __init__(self, particles,deltat):      
        self.deltat=deltat
        self.particles=particles
        self.angle = 30
        self.fig = plt.figure(figsize=(16,12))
        self.FLOOR = 0.0
        self.CEILING = self.particles.L
        self.ax = self.fig.add_subplot(111,projection = '3d')
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=1, 
                                           init_func=self.setup_plot,blit=False)

    def setup_plot(self):
        """ Set world coordinates, colors, symbol size ('s') """
        x, y, z = next(self.stream())
        self.scat = self.ax.scatter(x, y, z,c='b', s=10, animated=False)
        self.ax.set_xlim3d(self.FLOOR, self.CEILING)
        self.ax.set_ylim3d(self.FLOOR, self.CEILING)
        self.ax.set_zlim3d(self.FLOOR, self.CEILING)
        return self.scat

    def stream(self):
        """ 
           Calls particle update routine, yield transposed particle positions
        """
        data = np.transpose(self.particles.positions)
        while True:
            self.particles.update(self.deltat)
            data=np.transpose(self.particles.positions)
            yield data
            
    def update(self, i):
        """ Use new particle position for drawing next frame """
        data =next(self.stream())
        self.scat._offsets3d = juggle_axes(data[0,:],data[1,:],data[2,:], 'z')
        self.ax.view_init(10,self.angle)
        plt.draw()
        return self.scat,

    def show(self):
        plt.show()
