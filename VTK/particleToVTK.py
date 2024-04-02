'''
convert particle data into VTK object
'''

from sdfpy import load_sdf
from thingking import loadtxt
import vtk
import numpy as np
from particle_loader import particleSDF

prefix = "../../project/data/ds14_scivis_0128/"
filename = prefix + "ds14_scivis_0128_e4_dt04_1.0000"

particle = particleSDF(filename)

n = particle.Num
points = vtk.vtkPoints()

# Create an array to store the velocity
velocity_array = vtk.vtkFloatArray()
velocity_array.SetNumberOfComponents(3)  # Number of components per tuple (3 for vectors)
velocity_array.SetName("Velocity")  # Name of the property

# Create an array to store the acceleration
acceleration_array = vtk.vtkFloatArray()
acceleration_array.SetNumberOfComponents(3)
acceleration_array.SetName("Acceleration")

# Create an array to store the potential
phi_array = vtk.vtkFloatArray()
phi_array.SetNumberOfComponents(1)
phi_array.SetName("Phi")

for i in range(n):
    x, y, z = particle.Positions[i]
    points.InsertNextPoint(x, y, z)

    vx, vy, vz = particle.Velocity[i]
    velocity_array.InsertNextTuple([vx, vy, vz])

    ax, ay, az = particle.Acceleration[i]
    acceleration_array.InsertNextTuple([ax, ay, az])

    phi = abs(particle.Phi[i])
    phi_array.InsertNextValue(phi)

# create vtkPolyData object
polydata = vtk.vtkPolyData()
polydata.SetPoints(points)

# Associate the property array with the points
polydata.GetPointData().AddArray(velocity_array)
polydata.GetPointData().AddArray(acceleration_array)
polydata.GetPointData().AddArray(phi_array)

# create VTK object
writer = vtk.vtkPolyDataWriter()
writer.SetFileName("output.vtk")
writer.SetInputData(polydata)
writer.Write()
