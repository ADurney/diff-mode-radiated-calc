from collections import namedtuple
from math import sin,pi
import numpy as np

import matplotlib.pyplot as plt

#Constants section
MAX_HARMONIC = 91


TIME_RISE = 100e-9 # seconds
TIME_FALL = 100e-12 #seconds
CARRIER_FREQ = 1e6 #hz
AMPLITUDE = 1e-3#amps
DUTY_CYCLE = 0.5
LOOP_AREA = 10e-3 * 10e-3 #m^2


def harmonic_current(amplitude,t_min,duty,carrier_freq,harmonic):
    term1 = harmonic * pi * duty
    term2 = (harmonic * pi * t_min) * carrier_freq

    sine1 = (sin(term1)/term1)
    sine2 = (sin(term2) / term2)

    harmonic_current = 2 * amplitude * duty * sine1 * sine2
    return harmonic_current

def harmonic_field_strength(freq,loop_area, current):
    field_strength = 87.6e-16 * ( freq * freq * loop_area * current)
    return field_strength



harmonics = range(1,MAX_HARMONIC,2)
harmonics_current = []
harmonics_str = []


fig,ax = plt.subplots()

for harm in harmonics:
    current = harmonic_current(AMPLITUDE,TIME_RISE,DUTY_CYCLE,CARRIER_FREQ,harm)
    harmonics_current.append(current*1e3)
    field_str = harmonic_field_strength(CARRIER_FREQ * harm,LOOP_AREA,current)
    harmonics_str.append(field_str)


ax.stem(harmonics,harmonics_current)
ax.grid(True)
ax.plot()




plt.xlabel("nth harmonic")
plt.ylabel("Current (mA)")
plt.title("Harmonic current of a pure square wave")
#plt.ylim(top=abs(harmonics_current[4])*1.1)


plt.show()


