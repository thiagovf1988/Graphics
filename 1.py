from math import pi
from tkinter import *
import numpy as np
from matplotlib import pyplot as plt


def image_maker(angle, domain, frequency_amplitude, horizontal_shift):
    max_amplitude = 1
    amplitude = max_amplitude*np.cos(domain*frequency_amplitude)

    image = angle*domain + amplitude * \
        np.cos(frequency_curve*(domain-horizontal_shift))
    return image


angle = (2/10)
domain = np.arange(0, 4*pi, 0.0001)

max_amplitude = 1
frequency_amplitude = (5*pi/((2*pi)))

horizontal_shift = (2*pi)/(1*10)
# horizontal_shift = 0
frequency_curve = ((0+2*6)*5*2*pi/(2*pi))

amplitude = max_amplitude*np.cos(frequency_amplitude*(domain-horizontal_shift))

image = angle*domain + amplitude * \
    np.cos(frequency_curve*(domain-horizontal_shift))

f1 = frequency_amplitude
d1 = horizontal_shift
f2 = frequency_curve
d2 = horizontal_shift
# y2 = angle*domain + (np.cos(f1*(domain-d1)))*np.cos(f2*(domain-d2))
y2 = angle*domain + (np.cos(f1*domain-f1*d1+f2*domain-f2*d2)) + \
    np.cos(f1*domain-f1*d1-f2*domain+f2*d2)
y4 = np.cos(frequency_curve*(domain-horizontal_shift))
y5 = max_amplitude*np.cos(frequency_amplitude*(domain-horizontal_shift))
y6 = np.cos(frequency_curve*(domain-horizontal_shift)) * \
    np.cos(frequency_amplitude*(domain-horizontal_shift))


frequency_amplitude2 = (5*pi/((2*pi)))
amplitude2 = max_amplitude*np.sin(frequency_amplitude2*(domain))
amplitude2 = abs(max_amplitude*np.sin(frequency_amplitude2*(domain)))
y2 = angle*domain + amplitude2 * \
    np.cos(frequency_curve*(domain-horizontal_shift))
# y2 = amplitude2

domaint = 0
for i in range(1245, 1317):
    domaint = i*2*pi/(100*f2)
    y3 = angle*domaint + (np.cos(f1*domaint-f1*d1+f2*domaint-f2*d2)) + \
        np.cos(f1*domaint-f1*d1-f2*domaint+f2*d2)
    if (i == 1246):
        print(y3)
        print(domaint)
        print(np.cos(f1*domaint-f1*d1+f2*domaint-f2*d2))
        print(np.cos(f1*domaint-f1*d1-f2*domaint+f2*d2))
        print(np.cos(f2*(domaint-d2)))
    elif (i == 1314):
        print(y3)
        print(domaint)
        print(np.cos(f1*domaint-f1*d1+f2*domaint-f2*d2))
        print(np.cos(f1*domaint-f1*d1-f2*domaint+f2*d2))
        print(np.cos(f2*(domaint-d2)))
domaint = 0
for i in range(1):
    domaint = i*2*pi/(100*f2)
    y3 = angle*domaint + (np.cos(f1*domaint-f1*d1+f2*domaint-f2*d2)) + \
        np.cos(f1*domaint-f1*d1-f2*domaint+f2*d2)
    if (i == 0):
        print(y3)
        print(domaint)
        print(np.cos(f1*domaint-f1*d1+f2*domaint-f2*d2))
        print(np.cos(f1*domaint-f1*d1-f2*domaint+f2*d2))
        print(np.cos(f2*(domaint-d2)))
    # print(y3)
    # print(i*2*pi/(10*f2))
    # print(i)
    # print(y3)

# print(f2)
print(2*pi/f2)
print(2*pi/f1)
# print(d2)
# print(np.cos(f2*(0-d2)))
# print(np.cos(f2*(((2*pi)/(5*13)))-d2))
plt.plot(domain, y2)

plt.show()
