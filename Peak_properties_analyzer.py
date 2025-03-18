import numpy as np
import pandas as pd
def peak_properties(positions, array, mode):
    output =np.zeros((len(positions),7))
    output[:,0] = positions


    valid = {'Threshold', 'CWT', 'CNN','Autoencoder'}
    if mode not in valid:
        raise ValueError("results: status must be one of %r." % valid)
    

    noise_mean = np.mean(array[0:100])
    noise_std = np.std(array[0:100])
    rise_times = []
    fall_times = []
    total_times = []
    Integrated_rise_area = []
    Integrated_area_under = []
    magnitudes = []
    if mode in ['CNN', 'Autoencoder']:
        for i in positions:
            start = i
            stop = len(array)
            
            peak = np.argmax(array[i:i+100])+i
            magnitudes.append(array[peak])
            rise_times.append(peak-i)

            for j in np.arange(peak,stop,1):
                if array[j]<(noise_mean-noise_std):
                    fall_end = j
                    break
            fall_times.append(fall_end-peak)

            total_times.append(fall_end-i)

            down_end = i+700

            for j in np.arange(start-20,stop,1):
                if array[j]>(noise_mean+2*noise_std) and array[j+2]>(noise_mean+2*noise_std):
                    up_start = j
                    break
            
            for j in np.arange(up_start,stop,1):     
                if array[j]<(noise_mean) and array[j+2]<(noise_mean):
                    up_end = j
                    break

            for j in np.arange(up_end,stop,1):
                if array[j]>(noise_mean+0.2*noise_std) and array[j+2]>(noise_mean+0.2*noise_std):
                    down_end = j
                    break

            if down_end == i+700 and i>3500:
                down_end = stop 

                    
                
                
            upper_area = np.trapz(array[up_start:up_end],dx=1)
            down_area = np.trapz(array[up_end:down_end],dx=1)
            Integrated_rise_area.append(upper_area)   
            Integrated_area_under.append(down_area)
    output[:,1] = rise_times
    output[:,2] = fall_times
    output[:,3] = total_times
    output[:,4] = magnitudes        
    output[:,5] = Integrated_rise_area
    output[:,6] = Integrated_area_under
    inde = np.arange(0,len(positions),1)
    column_names = ['Position','Rise time','Fall time','total time','Pulse magnitude','Integrated area above', 'Integrated area below']

    df = pd.DataFrame(output,index=inde, columns=column_names)
    return df#, up_end, up_start, down_end
                
            


                
