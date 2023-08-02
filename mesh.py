import gmsh
import meshio
import sys

gmsh.initialize()
gmsh.model.add("Haiti")

lc = 5e-3
l1 = gmsh.model.geo.addPoint(0.01, 1-0.823, 0, lc, 1)
l2 = gmsh.model.geo.addPoint(0.023, 1-0.850, 0, lc, 2)
l3 = gmsh.model.geo.addPoint(0.043, 1-0.863, 0, lc, 3)
l4 = gmsh.model.geo.addPoint(0.210, 1-0.962, 0, lc, 4)
l5 = gmsh.model.geo.addPoint(0.254, 1-0.956, 0, lc, 5)
l6 = gmsh.model.geo.addPoint(0.232, 1-0.925, 0, lc, 6)
l7 = gmsh.model.geo.addPoint(0.292, 1-0.895, 0, lc, 7)
l8 = gmsh.model.geo.addPoint(0.593, 1-0.920, 0, lc, 8)
l9 = gmsh.model.geo.addPoint(0.848, 1-0.890, 0, lc, 9)
l10 = gmsh.model.geo.addPoint(0.946, 1-0.956, 0, lc, 10)
l11 = gmsh.model.geo.addPoint(0.970, 1-0.848, 0, lc, 11)
l12 = gmsh.model.geo.addPoint(0.866, 1-0.754, 0, lc, 12)
l13 = gmsh.model.geo.addPoint(0.949, 1-0.752, 0, lc, 13)
l14 = gmsh.model.geo.addPoint(0.958, 1-0.380, 0, lc, 14)
l15 = gmsh.model.geo.addPoint(0.592, 1-0.293, 0, lc, 15)
l16 = gmsh.model.geo.addPoint(0.368, 1-0.344, 0, lc, 16)
l17 = gmsh.model.geo.addPoint(0.367, 1-0.394, 0, lc, 17)
l18 = gmsh.model.geo.addPoint(0.605, 1-0.473, 0, lc, 18)
r1 = gmsh.model.geo.addPoint(0.614, 1-0.523, 0, lc, 19)
r2 = gmsh.model.geo.addPoint(0.605, 1-0.541, 0, lc, 20)
r3 = gmsh.model.geo.addPoint(0.834, 1-0.682, 0, lc, 21)
r4 = gmsh.model.geo.addPoint(0.822, 1-0.698, 0, lc, 22)
l19 = gmsh.model.geo.addPoint(0.583, 1-0.613, 0, lc, 23)
l20 = gmsh.model.geo.addPoint(0.746, 1-0.733, 0, lc, 24)
l21 = gmsh.model.geo.addPoint(0.740, 1-0.778, 0, lc, 25)
l22 = gmsh.model.geo.addPoint(0.647, 1-0.773, 0, lc, 26)
l23 = gmsh.model.geo.addPoint(0.620, 1-0.817, 0, lc, 27)
l24 = gmsh.model.geo.addPoint(0.092, 1-0.730, 0, lc, 28)
l25 = gmsh.model.geo.addPoint(0.029, 1-0.751, 0, lc, 29)


gmsh.model.geo.addLine(l1, l2, 1)
gmsh.model.geo.addLine(l2, l3, 2)
gmsh.model.geo.addLine(l3, l4, 3)
gmsh.model.geo.addLine(l4, l5, 4)
gmsh.model.geo.addLine(l5, l6, 5)
gmsh.model.geo.addLine(l6, l7, 6)
gmsh.model.geo.addLine(l7, l8, 7)
gmsh.model.geo.addLine(l8, l9, 8)
gmsh.model.geo.addLine(l9, l10, 9)
gmsh.model.geo.addLine(l10, l11, 10)
gmsh.model.geo.addLine(l11, l12, 11)
gmsh.model.geo.addLine(l12, l13, 12)
gmsh.model.geo.addLine(l13, l14, 13)
gmsh.model.geo.addLine(l14, l15, 14)
gmsh.model.geo.addLine(l15, l16, 15)
gmsh.model.geo.addLine(l16, l17, 16)
gmsh.model.geo.addLine(l17, l18, 17)
gmsh.model.geo.addLine(l18, r1, 18)
gmsh.model.geo.addLine(r1, r3, 19)
gmsh.model.geo.addLine(r3, r4, 20)
gmsh.model.geo.addLine(r4, r2, 21)
gmsh.model.geo.addLine(r2, l19, 22)
gmsh.model.geo.addLine(l19, l20, 23)
gmsh.model.geo.addLine(l20, l21, 24)
gmsh.model.geo.addLine(l21, l22, 25)
gmsh.model.geo.addLine(l22, l23, 26)
gmsh.model.geo.addLine(l23, l24, 27)
gmsh.model.geo.addLine(l24, l25, 28)
gmsh.model.geo.addLine(l25, l1, 29)

gmsh.model.geo.addLine(r2, r1, 30)


gmsh.model.geo.addCurveLoop(range(1,30), 1)
gmsh.model.geo.addCurveLoop([19,20,21,30], 2)

gmsh.model.geo.addPlaneSurface([1], 1)
gmsh.model.geo.addPlaneSurface([2], 2)

gmsh.model.geo.synchronize()

landarray = list(range(1, 30))
landarray.remove(19)
landarray.remove(20)
landarray.remove(21)

gmsh.model.addPhysicalGroup(1, landarray, name="LandBoundary")
gmsh.model.addPhysicalGroup(1, [20], name="Inflow")
gmsh.model.addPhysicalGroup(1, [30], name="Outflow")
gmsh.model.addPhysicalGroup(1, [19, 21], name="NoSlip")
gmsh.model.addPhysicalGroup(2,[1],name="Land")
gmsh.model.addPhysicalGroup(2,[2],name="River")

gmsh.model.mesh.generate(2)


gmsh.option.setNumber("Mesh.MshFileVersion",2.2)   

gmsh.write("Haiti.msh")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()