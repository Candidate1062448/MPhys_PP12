import numpy as np

from S1_generator.adc_filter import adc_filter_func
from S1_generator.high_pass_filter import high_pass

def S1_event(n):
    '''
    Input: n = number of events
    Output: y(nparray) = array of signal, 
    n(int) = # of photons, 
    p(list) = postion of photons
    '''
    number_of_photons = n
    signal_lenght = 3500
    photons_position =[]
    zeros= np.zeros(1000)
    photo_electrons = np.zeros(signal_lenght)
    s = np.random.exponential(1, number_of_photons)
    count, bins = np.histogram(s, signal_lenght, density=True)
    for i in range(len(count)):
        if count[i]==0:
            count[i]=0
        else:
            count[i] = 5 * count[i] * n
            count[i] = (0.7+0.6*np.random.random())*count[i]

    photo_electrons = np.add(photo_electrons, count)
    arr = np.zeros(500)
    arr = np.append(arr,photo_electrons)
    arr = np.append(arr,zeros)
    for i in range(len(arr)):
        if arr[i]>10:
            photons_position.append(i)





    y= adc_filter_func(arr,[0.25,0.02])  #[0.01,0.012]
    y2 = high_pass(y,0.005) #0.005

    return y2, number_of_photons, photons_position


