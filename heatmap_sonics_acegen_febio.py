import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x = ["FEBio", "SOniCS", "ACEFEM"]
y = ["FEBio", "SOniCS", "ACEFEM"]

harvest = np.array([[0.0, 10.92, 14.19], 
                    [10.92, 0.0, 3.33], 
                    [14.19, 3.33, 0.0]])

# FEBio x Acegn: 14,19 %
# FEBio x Sonics: 10,92 %
# ACEGen x Sonics: 3.33 %

fig, ax = plt.subplots()
im = ax.imshow(harvest, cmap='Blues')

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(x)))
ax.set_yticks(np.arange(len(y)))

# ... and label them with the respective list entries
ax.set_xticklabels(x)
ax.set_yticklabels(y)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(x)):
    for j in range(len(y)):
        text = ax.text(j, i, harvest[i, j],
                       ha="center", va="center", color="w")

#ax.set_title("ACEGen vs FEBio vs SOniCS for Money Rivlin material with Q1 discretization")
fig.tight_layout()
plt.show()