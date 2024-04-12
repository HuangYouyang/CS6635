from sdfpy import load_sdf
from thingking import loadtxt
import vtk
import numpy as np
from Halo_loader import Halo

time = 0.11
t = 11
prefix = "../../project/data/ds14_scivis_0128/"
# filename = prefix + "rockstar/hlists/hlist_{0}000.list".format(time)
filename = prefix + "rockstar/hlists/hlist_1.00000.list"

for i in range(1):
    time += 0.01
    t += 1
    # filename = prefix + "rockstar/hlists/hlist_{0:.2f}000.list".format(time)

    haloData = Halo(filename)

    n = haloData.x.shape[0]
    points = vtk.vtkPoints()

    # Create an array to store the halo id
    haloId_array = vtk.vtkFloatArray()
    haloId_array.SetNumberOfComponents(1)
    haloId_array.SetName("haloID")

    # Create an array to store time
    time_array = vtk.vtkFloatArray()
    time_array.SetNumberOfComponents(1)
    time_array.SetName("time")

    # Create an array to store scale
    scale_array = vtk.vtkFloatArray()
    scale_array.SetNumberOfComponents(1)
    scale_array.SetName("scale")

    # Create an array to store the velocity
    velocity_array = vtk.vtkFloatArray()
    velocity_array.SetNumberOfComponents(3)
    velocity_array.SetName("Velocity")

    for i in range(n):
        x, y, z = haloData.position[i]
        points.InsertNextPoint(x, y, z)

        vx, vy, vz = haloData.velocity[i]
        velocity_array.InsertNextTuple([vx, vy, vz])

        id = abs(haloData.id[i])
        haloId_array.InsertNextValue(id)

        scale = abs(haloData.scale[i])
        scale_array.InsertNextValue(scale)

        time_array.InsertNextValue(t)

    # create vtkPolyData object
    polydata = vtk.vtkPolyData()
    polydata.SetPoints(points)

    polydata.GetPointData().AddArray(haloId_array)
    polydata.GetPointData().AddArray(time_array)
    polydata.GetPointData().AddArray(scale_array)
    polydata.GetPointData().AddArray(velocity_array)

    # create VTK object
    writer = vtk.vtkPolyDataWriter()
    # writer.SetFileName("./halos/{0:.2f}.vtk".format(time))
    writer.SetFileName("./Time_{0}.vtk".format(t))
    writer.SetInputData(polydata)
    writer.Write()