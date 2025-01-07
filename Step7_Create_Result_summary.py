#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 09:54:02 2025

@author: Alexander.Morano
"""

import os 
import pandas as pd
import matplotlib.pyplot as plt

root_path = '/Users/Alexander.Morano/Desktop/data/2024_12_19_GPCs_final_test/humanplate/results_35diam/'

overall_quant = []

for root, sub, files in os.walk(root_path):

   filenames = [os.path.join(root, filename) for filename in files 
                 if filename.startswith('combined')]
   
   for filename in filenames:
        print(os.path.join(root, filename))
        x = os.path.join(root, filename)
        y = x.split('/')[-2]
        df = pd.read_csv(filename)
        mean_combined = df['Mean'].mean()
       
        if mean_combined > 100: #you can change this value depending on the intensity of the far red channel
            result = 'Positive'
        else:
            result = 'Negative'
                
        overall_quant.append({'Subfolder': y, 'Data': mean_combined, 'Results': result})
        

oqdf = pd.DataFrame(overall_quant)
sorted_oqdf = oqdf.sort_values(by='Subfolder')
print(sorted_oqdf)
sorted_oqdf.to_csv('/Users/Alexander.Morano/Desktop/data/2024_12_19_GPCs_final_test/humanplate/results_35diam/finalresultsalpha.csv')