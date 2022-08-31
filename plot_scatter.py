def get_data(file):
  x = []; y = []
  with open(file) as f:
    for line in f:
      cols = line.rstrip().split(",")
      x.append(float(cols[0]))
      y.append(float(cols[1]))
  return x,y
px,py = get_data("sample_2d.csv")
print(px,py)
import matplotlib.pyplot as plt
import numpy as np
a,b = np.polyfit(px,py,1)
rx = [min(px),max(px)]
ry = [a*x+b for x in rx]
plt.plot(rx,ry)
plt.scatter(px,py)
plt.show()