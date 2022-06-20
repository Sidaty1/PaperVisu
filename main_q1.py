import vedo
from vedo import Mesh, show, Points, Plane, Latex, Arrows, Arrow
import colorcet
import numpy as np
import meshio

#import os

with meshio.xdmf.TimeSeriesReader("data/deformed/cube_hexa_1_solution.xdmf") as reader:
        points, cells = reader.read_points_cells()
        t, point_data, cell_data = reader.read_data(0)



dep = point_data["f"][:, 1]
dep = dep.tolist()
for i in range(len(dep)):
    dep[i] = int(dep[i])

beam_q1 = Mesh('./data/undeformed/cube_hexa_1.vtu', c='black').wireframe().lineWidth(0.1).x(50)

deformed_q1 = Mesh('data/deformed/deformed_fenics.vtu', c='black').lineWidth(0.1).lighting('').x(50) 
print(len(deformed_q1.points()))
forces_points_initial = deformed_q1.points()[-5:-1] 
forces_points_initial_1 = deformed_q1.points()[-10:-7] 
forces_points_initial_2 = deformed_q1.points()[-7:-6] 
forces_points_initial_3 = deformed_q1.points()[115:120] 

forces_points_final = np.array(forces_points_initial) + np.array([[0, -10, 0] for _ in range(len(forces_points_initial))] )
forces_points_final_1 = np.array(forces_points_initial_1) + np.array([[0, -10, 0] for _ in range(len(forces_points_initial_1))] )
forces_points_final_2 = np.array(forces_points_initial_2) + np.array([[0, -10, 0] for _ in range(len(forces_points_initial_2))] )
forces_points_final_3 = np.array(forces_points_initial_3) + np.array([[0, -10, 0] for _ in range(len(forces_points_initial_3))] )

a1 = Arrows(forces_points_initial_1, forces_points_final_1, c='blue')
a2 = Arrows(forces_points_initial, forces_points_final, c='blue')
a3 = Arrows(forces_points_initial_2, forces_points_final_2, c='blue')
a4 = Arrows(forces_points_initial_3, forces_points_final_3, c='blue')

fixed_plan = Plane(pos=(0, 0, 0), normal=[0, 0, 1],  sx=20, sy=20, c='black', alpha=0.8)
fixed_plan2 = Plane(pos=(50, 0, 0), normal=[0, 0, 1],  sx=20, sy=20, c='red', alpha=0.4)


dirichlet = vedo.Text3D("Gamma D", pos=(-7.5, 10, 50), s = 3).rotateY(90)
mycmap = colorcet.rainbow_bgyr_10_90_c83


deformed_q1.cmap(mycmap, dep).addScalarBar(nlabels=3, size=(100, 105))

gamma_d = r'\Gamma_{D}'
gamma_n = r'\Gamma_{N}'
omega = r'\Omega'


ltx_gamma_D = Latex(gamma_d, s=10, c='red')
ltx_gamma_D.pos(0, 30, 75)
ltx_gamma_D.rotateY(90)

ltx_omega = Latex(omega, s=10, c='black')
ltx_omega.pos(-40, 30, 75)
ltx_omega.rotateY(90)

ltx_gamma_N = Latex(gamma_n, s=10, c='blue')
ltx_gamma_N.pos(-80, 30, 75)
ltx_gamma_N.rotateY(90)


plt = vedo.Plotter()
plt.add([ltx_gamma_D, ltx_omega, ltx_gamma_N, a1, a2, a3, a4, beam_q1, deformed_q1, fixed_plan2, ])
plt.show().close()