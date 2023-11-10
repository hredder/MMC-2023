from matplotlib import pyplot as plt
import numpy as np

count = 1000
data_x = np.random.uniform(33.75578655156453, 36.733972442257816, count)
data_y = np.random.uniform(-84.41352382914673, -75.3388168853683, count)

plt.scatter(data_x, data_y)
plt.show()

print(data_x)
print(data_y)