#from sdfpy import load_sdf
#from thingking import loadtxt
import vtk
import numpy as np

time = 0.11
t = 11
prefix = "../../project/data/ds14_scivis_0128/"
# filename = prefix + "rockstar/hlists/hlist_{0}000.list".format(time)
filename = prefix + "rockstar/trees/tree_0_0_0.dat"

trees = {}
particle = []
lines = []

with open(filename, 'r') as f:
    for line in f:
        lines.append(line)

for index, line in enumerate(lines):
    if line[:5]=="#tree":
        treeId = int(line.split()[1])
        next_line_index = index + 1
        while next_line_index < len(lines):
            next_line = lines[next_line_index]
            if next_line[:5] == "#tree":
                break
            else:
                p = [float(x) for x in next_line.split()]
                particle.append(p)
            next_line_index += 1
        #print(particle)
        trees[treeId] = particle
        particle = []  # 重新创建空列表

for i in range(1):
    time += 0.01
    t += 1
    treeId = 679582
    # filename = prefix + "rockstar/hlists/hlist_{0:.2f}000.list".format(time)

    haloData = trees[treeId]

    n = len(haloData)
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

    # Create an array to store mass
    mass_array = vtk.vtkFloatArray()
    mass_array.SetNumberOfComponents(1)
    mass_array.SetName("mass")

    # Create an array to store the velocity
    velocity_array = vtk.vtkFloatArray()
    velocity_array.SetNumberOfComponents(3)
    velocity_array.SetName("Velocity")

    for i in range(n):
        #x, y, z = haloData[i]
        points.InsertNextPoint(haloData[i][17], haloData[i][18], haloData[i][19])

        #vx, vy, vz = haloData.velocity[i]
        velocity_array.InsertNextTuple([haloData[i][20], haloData[i][21], haloData[i][22]])

        id = abs(haloData[i][1])
        haloId_array.InsertNextValue(id)

        scale = abs(haloData[i][0])
        scale_array.InsertNextValue(scale)

        mass = haloData[i][10]
        mass_array.InsertNextValue(mass)

        time_array.InsertNextValue(t)

    # create vtkPolyData object
    polydata = vtk.vtkPolyData()
    polydata.SetPoints(points)

    polydata.GetPointData().AddArray(haloId_array)
    polydata.GetPointData().AddArray(time_array)
    polydata.GetPointData().AddArray(scale_array)
    polydata.GetPointData().AddArray(mass_array)
    polydata.GetPointData().AddArray(velocity_array)

    # create VTK object
    writer = vtk.vtkPolyDataWriter()
    # writer.SetFileName("./halos/{0:.2f}.vtk".format(time))
    writer.SetFileName("./Tree_{0}.vtk".format(treeId))
    writer.SetInputData(polydata)
    writer.Write()