import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x= mu + sigma * np.random.randn(10000)

plt.hist(x,100, normed=1, alpha =0.77)
plt.show()