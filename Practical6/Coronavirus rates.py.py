dict={'USA':29862124,'India':11285561,'Brazil':11205972,'Russia':4360823,'UK':4234924}
print(dict)

import matplotlib.pyplot as plt
labels = 'USA','India','Brazil','Russia','UK'# define tag
sizes = [29862124, 11285561, 11205972, 4360823, 4234924]#each value
explode =(0,0,0,0,0)# Split a piece. The larger the value, the larger the gap
plt.pie(sizes,
           explode=explode,
           labels=labels,
           autopct = '%3.2f%%',# Values remain fixed decimal places
           shadow = False, # No shadow Settings
           pctdistance = 0.6)# Distance multiple of the center radius from the value
plt.axis('equal')# The X and Y axes are set to the same scale to ensure the pie is round
plt.show()
