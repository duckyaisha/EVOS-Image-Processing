#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 13:09:11 2025

@author: Alexander.Morano
"""

import os
import re
import sys
import glob
import shutil
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from datetime import date
import matplotlib.pyplot as plt
import argparse
import csv

root_path = '/Users/Alexander.Morano/Desktop/data/2025_01_16_NRXN1/R/results'

df = pd.read_csv("/Users/Alexander.Morano/Desktop/data/2025_01_16_NRXN1/R/results/finalresultsalpha.csv")
#df.replace({'0.1_ug_mL': 0.1, '1_ug_mL': 1, '10_ug_mL': 10}, inplace=True)

unique_conditions = df['Antibody'].unique()
filtered_unique_conditions = unique_conditions[1:10]


filtered_unique_conditions = filtered_unique_conditions[3:]


for condition in filtered_unique_conditions:
    subset = df[df['Antibody'] == condition]
    
    human = subset[subset['Antigen'] == 'hNRXN1b']
    print(subset)
    
    mouse = subset[subset['Antigen'] == 'mNRXN1b']
    control = subset[subset['Antigen'] == 'WY0041']
    fig, ax = plt.subplots(1) 
    handles, labels = ax.get_legend_handles_labels()
    ax.scatter(human['Concentration'], human['Data'], s=30, c='b', marker='o', label='human')
    ax.plot(human['Concentration'], human['Data'], c='b')
   
    ax.scatter(mouse['Concentration'], mouse['Data'], s=30, c='r', marker='o', label='mouse')
    ax.plot(mouse['Concentration'], mouse['Data'], c='r')
    ax.scatter(control['Concentration'], control['Data'], s=30, c='g', marker='o', label='Ctl')
    ax.set_title(condition)
    ax.set_xlabel('Concentration (uM)')
    ax.set_ylabel('MFI')
    ax.set_xscale('log')
    ax.legend(handles, labels)
    plt.legend() 
    plt.savefig(os.path.join(root_path,condition+'.png'), format = "png")
    plt.show()
    plt.close()
