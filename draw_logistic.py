import matplotlib.pyplot as plt
px = [0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0]
py = [0.0,0.041,0.163,0.36,0.64,1.0,1.44,1.96,2.56,3.24,4.0]
qy = [3.0,2.76,2.52,2.28,2.04,1.8,1.56,1.32,1.08,0.84,0.6]
plt.plot(px,py,color="red",linestyle="dashed")
plt.plot(px,qy,color="gray")
plt.xlabel("time/min")
plt.ylabel("altitube/km")
plt.legend(["quadratic","linear"])
plt.title("Time dependence")
plt.show()