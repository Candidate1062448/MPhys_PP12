import numpy as np

from S1_generator.adc_filter import adc_filter_func
from S1_generator.high_pass_filter import high_pass

def S1_event3(timesep):
    '''
    Input: timesep = timesep of 2 photons in 10ns units
    Output: y(nparray) = array of signal, 
    n(int) = # of photons, 
    p(list) = postion of photons
    '''

    arr = np.zeros(2000)
    arr[200] = 10000
    arr[200+timesep] = 10000

    photons_position = [200,200+timesep]
    number_of_photons = 2


    y= adc_filter_func(arr,[0.25,0.02])  #[0.01,0.012]
    y2 = high_pass(y,0.005) #0.005

    return y2, number_of_photons, photons_position