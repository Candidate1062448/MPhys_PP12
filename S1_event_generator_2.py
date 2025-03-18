import numpy as np

from S1_generator.adc_filter import adc_filter_func
from S1_generator.high_pass_filter import high_pass

def S1_event2(n,t_low_1, t_low_2,t_high,signal_lenght,noise_up= True, noise_level = 0.07):
    '''
    Input: n = number of events
    Output: y(nparray) = array of signal, 
    n(int) = # of photons, 
    p(list) = postion of photons
    '''
    number_of_photons = n
    signal_lenght 
    photons_position =[]
    zeros= np.zeros(40)  #have to change this
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
    arr = np.zeros(10)
    arr = np.append(arr,photo_electrons)
    arr = np.append(arr,zeros)
    for i in range(len(arr)):
        if arr[i]>10:
            photons_position.append(i)



    coeff1 = 10/(10+t_low_1)
    coeff2 = 10/(10+t_low_2)
    coeffh = 10/(10+t_high)

    y= adc_filter_func(arr,[coeff1,coeff2],noise = False)  #[0.01,0.012]
    y2 = high_pass(y,coeffh) #0.005
    max = np.max(y2)
    if noise_up==True:
        for i in range(len(y2)):
            y2[i]=y2[i]+noise_level*np.random.random()*max


    return y2, number_of_photons, photons_position