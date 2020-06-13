from math import pi
import numpy as np
from matplotlib import pyplot as plt


angle = (2/10)
domain = np.arange(0, 4*pi+0.05, 0.0001)

max_amplitude = 1
frequency_amplitude = (5*pi/((2*pi)))

horizontal_shift = (2*pi)/(1*10)
frequency_curve = ((0+2*6)*5*2*pi/(2*pi))

amplitude = abs(max_amplitude*np.sin(frequency_amplitude*(domain)))

image = angle*domain + amplitude * \
    np.cos(frequency_curve*(domain-horizontal_shift))

plt.plot(domain, image)
plt.margins(0)
plt.xticks([0, 2, 4, 6, 8, 10, 12, 14])
plt.yticks([-1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5])

plt.show()
