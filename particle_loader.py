import numpy as np
import sdf

class particleSDF(object):
    def __init__(self, filename, cMpc=True):
        super(particleSDF, self).__init__()
        self.isCoMoving = cMpc
        self.init(filename)
        # self.setDomain()

    def init(self, filename):
        self.Particles = sdf.load_sdf(filename)
        self.Positions = self.getPosition() # the position of the particles
        self.Velocity = self.getVelocity() # the velocity of the particles
        self.Acceleration = self.getAcceleration() # the acceleration of the particles
        self.Num = self.Particles.parameters['npart_orig']
        self.Phi = self.Particles['phi']

    # get the position of the particles
    def getPosition(self):
        x = self.Particles['x']
        y = self.Particles['y']
        z = self.Particles['z']
        xyz = np.dstack((x,y,z))[0]
        if self.isCoMoving:
            return self.toCoMoving(xyz)
        else:
            return xyz

    # get the velocity of the particles
    def getVelocity(self):
        vx = self.Particles['vx']
        vy = self.Particles['vy']
        vz = self.Particles['vz']
        return np.dstack((vx, vy, vz))[0]

    # get the acceleration of the particles
    def getAcceleration(self):
        ax = self.Particles['ax']
        ay = self.Particles['ay']
        az = self.Particles['az']
        return np.dstack((ax, ay, az))[0]

    def toCoMoving(self, property):
        h_100 = self.Particles.parameters['h_100']
        width = self.Particles.parameters['L0']
        cosmo_a = self.Particles.parameters['a']
        kpc_to_Mpc = 1. / 1000
        sl = slice(0, None)
        convert_to_cMpc = lambda proper: (proper + width / 2.) * h_100 * kpc_to_Mpc / cosmo_a
        return convert_to_cMpc(property)