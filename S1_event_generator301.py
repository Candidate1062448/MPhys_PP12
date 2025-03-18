import numpy as np

from S1_generator.adc_filter import adc_filter_func
from S1_generator.high_pass_filter import high_pass

def S1_event301(timesep,t_low_1=2,t_low_2=30,t_high=150):
    '''
    Input: timesep = timesep of 2 photons in 10ns units
    Output: y(nparray) = array of signal, 
    n(int) = # of photons, 
    p(list) = postion of photons
    '''

    arr = np.zeros(550)
    arr[100] = 10000
    #arr[201] = 9000
    #arr[348] =11000
    #arr[466]=8000
    arr[100+timesep] = 10000

    photons_position = [200,200+timesep]
    number_of_photons = 5
    
    coeff1 = 10/(10+t_low_1)
    coeff2 = 10/(10+t_low_2)
    coeffh = 10/(10+t_high)

    y= adc_filter_func(arr,[coeff1,coeff2],noise = False)  #[0.01,0.012]
    y2 = high_pass(y,coeffh) #0.005

    for i in range(len(y2)):
        y2[i]=y2[i]+0.1*np.random.random()*np.max(y2)

    return y2, number_of_photons, photons_position