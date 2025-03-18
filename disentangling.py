import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from scipy.signal import argrelmax
from peak_threshold301 import peak_threshold_finder301


def find_coincidental_photons(signal):
    a = signal.copy()
    n,peaks, crossings, avg, std = peak_threshold_finder301(a)
    
    areas = np.zeros((len(crossings), 2))
    areas[:, 0] = crossings  

    for idx, cross in enumerate(crossings):  
        for j in range(40):
            pos = cross + j
            if pos >= len(a):  
                areas[idx, 1] = j 
                break
            if a[pos] > 1.1*avg:
                continue
            else:
                areas[idx, 1] = j  
                break
    
    interesting_areas = areas[areas[:,1]> (np.average(areas[:,1]) +0.1*np.average(areas[:,1]))]

    multiple_photon_crossings = []

    for i, cross in enumerate(interesting_areas[:, 0]):
        start = max(int(cross) - 1, 0)
        end = min(int(cross) + int(interesting_areas[i, 1]), len(a))

        segment = a[start:end]
        maxima = argrelmax(segment)

        if len(maxima[0]) > 1:
            multiple_photon_crossings.append(cross)

    return multiple_photon_crossings

