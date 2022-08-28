import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-7,7,201)
plt.plot(x,1/(1+np.exp(-x)))
plt.show()