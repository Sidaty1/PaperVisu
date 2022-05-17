from vedo import Mesh, show, Points
#import os

boundery_conditions = []

# Get the beam left side points considered as boundery conditions
for i in [0, -7.5, 7.5]:
    for j in [0, -7.5, 7.5]:
        boundery_conditions.append([i, j, 0])

# Beams boundery counditions
bc_p1 = Points(boundery_conditions)
bc_q1 = Points(boundery_conditions).y(50)

# Undeformed P1 and Q1 beams, update the color in the c function 
beam_p1 = Mesh('./data/undeformed/beam_p1.vtu').lighting('ambient').c("red").lw(3)
beam_q1 = Mesh('./data/undeformed/beam_q1.vtu').lighting('ambient').c("yellow").lw(3).y(50)

# Deformed P1 and Q1 beams, update the color in the c function 
deformed_p1 = Mesh('Add deformed p1 mesh here ').c("red").lw(3)  # Can be generated with FEniCS or with the sofa STLExport component 
deformed_q1 = Mesh('Add deformed p2 mesh here').c("yellow").lw(3).y(50) # Can be generated with FEniCS or with the sofa STLExport component 

# Showing everything
show(beam_p1, beam_q1, bc_p1, bc_q1, deformed_p1, deformed_q1,  axes=1).close()