from vedo import Mesh, show, Points
#import os

boundery_conditions = []

# Get the beam left side points considered as boundery conditions
for i in [0, -7.5, 7.5]:
    for j in [0, -7.5, 7.5]:
        boundery_conditions.append([i, j, 0])

bc_p1 = Points(boundery_conditions)
bc_q1 = Points(boundery_conditions).y(50)

    
beam_p1 = Mesh('./data/undeformed/beam_p1.vtu').c("red", 0.3).lw(3)
beam_q1 = Mesh('./data/undeformed/beam_q1.vtu').c("grey3", 0.3).lw(3).y(50)

bc_p1 = beam_p1.clone().cutWithPointLoop(bc_p1, invert=False)
bc_p1.c('grey5').lw(2)

bc_q1 = beam_q1.clone().cutWithPointLoop(bc_q1, invert=False)
bc_q1.c('grey5').lw(2)

show(beam_p1, beam_q1, bc_p1, bc_q1, axes=1).close()