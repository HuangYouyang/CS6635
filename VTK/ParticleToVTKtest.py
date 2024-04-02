# Look at sdf_example.py in the examples/ directory for more detail

from sdfpy import load_sdf
from thingking import loadtxt
import vtk
import numpy as np

# Load N-body particles from a = 1.0 dataset. Particles have positions with
# units of proper kpc, and velocities with units of km/s.
prefix = "../../project/data/ds14_scivis_0128/"
particles = load_sdf(prefix + "ds14_scivis_0128_e4_dt04_1.0000")
xx, yy, zz = particles['x'], particles['y'], particles['z']

# convert
h_100 = particles.parameters['h_100']
width = particles.parameters['L0']
cosmo_a = particles.parameters['a']
kpc_to_Mpc = 1. / 1000
sl = slice(0, None)

# Define a simple function to convert proper to comoving Mpc/h.
convert_to_cMpc = lambda proper: (proper + width / 2.) * h_100 * kpc_to_Mpc / cosmo_a

# shift it to start at 0
particles_x = convert_to_cMpc(xx[sl])
particles_y = convert_to_cMpc(yy[sl])
particles_z = convert_to_cMpc(zz[sl])
particles_x = particles_x - particles_x.min()
particles_y = particles_y - particles_y.min()
particles_z = particles_z - particles_z.min()

n = len(particles_x)
pts = vtk.vtkPoints()
for i in range(n):
    pts.InsertNextPoint(particles_x[i], particles_y[i], particles_z[i])

# 创建 vtkPolyData 对象
polydata = vtk.vtkPolyData()
polydata.SetPoints(pts)

# 创建VTK object
writer = vtk.vtkPolyDataWriter()
writer.SetFileName("output.vtk")
writer.SetInputData(polydata)
writer.Write()

# # 创建点的可视化表示
# points_glyph = vtk.vtkVertexGlyphFilter()
# points_glyph.SetInputData(polydata)
#
# # 创建 mapper 和 actor
# mapper = vtk.vtkPolyDataMapper()
# mapper.SetInputConnection(points_glyph.GetOutputPort())
#
# actor = vtk.vtkActor()
# actor.SetMapper(mapper)
# actor.GetProperty().SetColor(1.0, 0.0, 0.0)  # 设置为红色
#
# # 创建渲染器和渲染窗口
# ren = vtk.vtkRenderer()
# ren.SetBackground(1.0, 1.0, 1.0)
# ren.AddActor(actor)
# ren.ResetCamera()
#
# renWin = vtk.vtkRenderWindow()
# renWin.SetSize(2560, 1600)
# renWin.AddRenderer(ren)
#
# # 创建交互器并启动交互
# iren = vtk.vtkRenderWindowInteractor()
# iren.SetRenderWindow(renWin)
# iren.Start()
