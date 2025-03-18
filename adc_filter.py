import numpy as np
def adc_filter_func(array,coeff, noise=True):
    '''
    Input: array = array with delta pulses, coeff = 2elements tuple, 
    coeff is defined as coeff[i] = timestep /(timestep + RC-tau)

    Output = double low filtered array

    '''
    ph = array.copy()
    for j in range(2):
        accu = ph[0]
        for i in range(len(ph)):
            accu = accu + coeff[j]*(ph[i] - accu)
            ph[i] = accu
    
    if noise == True:
        noise = np.random.normal(0,5,int((len(ph)/4)))
        s = np.array([np.zeros(int(len(ph)/4)),noise])
        noise = np.ravel(s,order='F')
        
        s1 = np.array([np.zeros(len(noise)),noise])
        noise = np.ravel(s1, order= 'F')


        ph = np.add(ph,noise)
    return ph