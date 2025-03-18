import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from peak_threshold3 import peak_threshold_finder3

def correlation_test(signal, model):
    n, p, crossings = peak_threshold_finder3(signal)

    y = signal.copy()
    snippet_length = len(model)

    f = np.zeros((n, 2))  # Proper initialization

    for j in range(n):
        best_parameters = np.zeros((6, 2))  # Store (rho, p_value)
        
        for i in range(6):
            start = crossings[j] - 7 + i
            end = start + snippet_length
            
            # Ensure indices are within bounds
            if start < 0 or end > len(y):
                continue
            
            comparison = y[start:end]
            rho, p_value = pearsonr(model, comparison)
            best_parameters[i, 0] = rho
            best_parameters[i, 1] = p_value

        f[j, 0] = crossings[j]  # Store peak location
        f[j, 1] = np.max(best_parameters[:, 0])  # Store best correlation
        
    output = f.copy()
    yn = (output[:,1]>0.5).astype(bool).reshape(-1,1)
    output2 = np.hstack((output,yn))
    dfoutput = pd.DataFrame(output2,columns=['Peak location','Correlation value', 'Is it a pulse?']) #Pack the results in a nicer pandas dataframe
    dfoutput['Is it a pulse?'] = dfoutput['Is it a pulse?'].astype(bool) 
    dfoutput['Is it a pulse?'] = dfoutput['Is it a pulse?'].apply(lambda x: 'Yes' if x else 'No')

    
    return dfoutput

