from collections import namedtuple
from math import sin,pi
import numpy as np

import matplotlib.pyplot as plt

#Constants section
MAX_HARMONIC = 91


TIME_RISE = 100 # seconds
TIME_FALL = 100e-9 #seconds
TIME_MIN = min(TIME_RISE,TIME_FALL)
CARRIER_FREQ = 1e6 #hz
PERIOD = 1/CARRIER_FREQ
AMPLITUDE = 1#amps
DUTY_CYCLE = 0.5
LOOP_AREA = 10e-3 * 10e-3 #m^2



def harmonic_current(amplitude,t_min,duty,carrier_freq,harmonic):
    term1 = harmonic * pi * duty
    term2 = (harmonic * pi * t_min) * carrier_freq

    sine1 = (sin(term1)/term1)
    sine2 = (sin(term2) / term2)

    harmonic_current = 2 * amplitude * duty * sine1 * sine2
    #return sin(term1)
    return harmonic_current

def harmonic_field_strength(freq,loop_area, current):
    field_strength = 87.6e-16 * ( freq * freq * loop_area * current)
    return field_strength


def harmonic_current_envelope(first_harmonic_current, t_min):
    pass


harmonics = range(1,MAX_HARMONIC,2)
harmonics_current = []

harmonics_str = []


fig,ax = plt.subplots()

#TODO hardcoded for now
envelope_x = [1,1/(pi*TIME_MIN)]

envelope_y = [0.64,]

for harm in harmonics:
    current = harmonic_current(AMPLITUDE,TIME_MIN,DUTY_CYCLE,CARRIER_FREQ,harm)
    harmonics_current.append(abs(current))
    field_str = harmonic_field_strength(CARRIER_FREQ * harm,LOOP_AREA,current)
    harmonics_str.append(field_str)




ax.stem(harmonics,harmonics_current)
ax.plot()

ax.grid(True)




plt.xlabel("nth harmonic")
plt.ylabel("Current (mA)")
plt.title("Harmonic current of a pure square wave")
plt.xscale("log")


plt.show()


