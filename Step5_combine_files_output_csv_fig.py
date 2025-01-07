#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 09:53:02 2025

@author: Alexander.Morano
"""

import os 
import pandas as pd
import matplotlib.pyplot as plt

root_path = "/Users/Alexander.Morano/Desktop/data/2024_12_19_GPCs_final_test/remnantplate/results/"

for root, sub, files in os.walk(root_path):
    filenames = [os.path.join(root, filename) for filename in files 
                 if filename.endswith('.csv')]
    
    flist = []
    plt.clf()
    for filename in filenames:
        print(os.path.join(root, filename))
        df = pd.read_csv(filename)
        flist.append(df)
        df_out = pd.concat(flist)
        df_out.loc['mean of cells'] = df_out.mean()
        df_out.to_csv(os.path.join(root, 'combined.csv'))
        fig = df_out['Mean'].hist(bins=[0, 100, 500, 1000, 2000, 3000, 4000])
        plt.savefig(os.path.join(root, 'fig'))
