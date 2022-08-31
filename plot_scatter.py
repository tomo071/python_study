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
plt.scatter(px,py)
plt.show()