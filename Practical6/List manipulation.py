gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]

#calculate the average exons.
average=[]
for i in range(0,10):
 y=gene_lengths[i]/exon_counts[i]
 average.append(y)

#manipulate sort
 average.sort()
 print (average)

import numpy as np
import matplotlib.pyplot as plt
n=10

plt.boxplot(x = average, # Specify the drawing data
            vert=True,
            whis=1.5,
            patch_artist=True,
            boxprops = {'color':'black','facecolor':'#9999ff'}, # Set box properties, fill color and border color
            flierprops = {'marker':'o','markerfacecolor':'red','color':'black'}, # Meanprops = {' Marker ':'D',' MarkerFaceColor ':' IndianRed '} # Set the outliers, the shape of the points, and the fill color
            medianprops = {'linestyle':'--','color':'white'}) # Sets the properties of the median line, the type and color of the line
plt.show()
