import scipy.signal as sc
import numpy as np
def peak_identifier(y,width):
    peaks_cwt = sc.find_peaks_cwt(y,widths=width)


    avg = np.mean(y)  #computes the average and std over the whole sample
    std = np.std(y)

    

    y2 = y.copy()

    y2 = [value for value in y if value <= avg + 2 * std] #this line rewrites a copy of our sample array without pulses above 4sigma
    
    avg = np.mean(y2) #recompute average and std, without the pulses, to obtain baseline
    std = np.std(y2)

    
    refined_peaks_cwt =[]

    for i in range(len(peaks_cwt)):
        if y[peaks_cwt[i]] > avg +2.5*std:
            refined_peaks_cwt.append(peaks_cwt[i])
    return len(refined_peaks_cwt), refined_peaks_cwt