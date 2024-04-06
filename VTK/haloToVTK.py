from sdfpy import load_sdf
from thingking import loadtxt
import vtk
import numpy as np
from Halo_loader import Halo

time = 0.11
t = 11
prefix = "../../project/data/ds14_scivis_0128/"
# filename = prefix + "rockstar/hlists/hlist_{0}000.list".format(time)

for i in range(89):
    time += 0.01
    t += 1
    filename = prefix + "rockstar/hlists/hlist_{0:.2f}000.list".format(time)
    print(filename)

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

    for i in range(n):
        if haloData.Tree_root_ID[i] == 676638:
            x, y, z = haloData.position[i]
            points.InsertNextPoint(x, y, z)

            id = abs(haloData.id[i])
            haloId_array.InsertNextValue(id)

            scale = abs(haloData.scale[i])
            scale_array.InsertNextValue(scale)

            time_array.InsertNextValue(t)
            print(t)

    # create vtkPolyData object
    polydata = vtk.vtkPolyData()
    polydata.SetPoints(points)

    polydata.GetPointData().AddArray(haloId_array)
    polydata.GetPointData().AddArray(time_array)
    polydata.GetPointData().AddArray(scale_array)

    # create VTK object
    writer = vtk.vtkPolyDataWriter()
    writer.SetFileName("./halos/{0:.2f}.vtk".format(time))
    writer.SetInputData(polydata)
    writer.Write()