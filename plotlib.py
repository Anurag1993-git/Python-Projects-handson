from matplotlib import pyplot as plt
import numpy as np

langs = ['C','C++','JAVA','PYTHON','PHP']
students = [23,17,35,29,12]
plt.bar(langs,students)
ypoints = np.array([3,8,1,10])
plt.plot(ypoints, color='r')
plt.plot(ypoints, linewidth='20.5')
plt.show()
