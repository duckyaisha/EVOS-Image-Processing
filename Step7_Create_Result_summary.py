#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 09:54:02 2025

@author: Alexander.Morano
"""

import os 
import pandas as pd
import matplotlib.pyplot as plt

root_path = '/Users/Alexander.Morano/Desktop/data/2025_01_16_NRXN1/results'

import csv

#as long as we set up plate maps with 0.1 1 and 10 and each column corresponds to an antibody with a certain number of rows corresponding to an antigen, this will work 
#you just have to save 'ablist' as a list of abs on the plate as a csv
#then manually change the antigens because there are usually only a few.

antibodylist = []
with open('/Users/Alexander.Morano/Desktop/data/2025_01_16_NRXN1/ablist.csv') as inputfile:
    for row in csv.reader(inputfile):
        antibodylist.append(row[0])

#remove the space from the beginning of the name of the first antibody. this happens when I convert excel to csv for some reason.
antibodylist[0] = antibodylist[0][1:]

root_path = '/Users/Alexander.Morano/Desktop/data/2025_01_16_NRXN1/results'

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

#now we can add antibody name. 
def antibody(subfolder): 
    #extract the first character of the well
    letter = subfolder[0]
    #convert the number part of the wellto an integer
    number = int(subfolder[1:])
    
    if letter == 'A' and number == 1:
        return "V5_CTL"
    elif letter == 'B' and number == 1:
        return "V5_CTL"
    elif letter == 'B' and number == 11:
        return "V5_CTL"
    elif letter == 'E' and number == 1:
        return "V5_CTL"
    elif letter == 'E' and number == 11:
        return "V5_CTL"
    elif letter == 'C' and number == 1:
        return "Isotype_CTL"
    elif letter == 'F' and number == 1:
        return "Isotype_CTL"
    elif letter == 'H' and number == 1:
        return "Isotype_CTL"
    elif letter == 'C' and number == 11:
        return "Isotype_CTL"
    elif letter == 'F' and number == 11:
        return "Isotype_CTL"
    
    elif letter >= 'A' and letter <= 'G' and number == 2:
        return antibodylist[0]
    elif letter >= 'A' and letter <= 'G' and number == 3:
       return antibodylist[1]
    elif letter >= 'A' and letter <= 'G' and number == 4:
      return antibodylist[2]
    elif letter >= 'A' and letter <= 'G' and number == 5:
      return antibodylist[3]
    elif letter >= 'A' and letter <= 'G' and number == 6:
      return antibodylist[4]
    elif letter >= 'A' and letter <= 'G' and number == 7:
      return antibodylist[5]
    elif letter >= 'A' and letter <= 'G' and number == 8:
      return antibodylist[6]
    elif letter >= 'A' and letter <= 'G' and number == 9:
      return antibodylist[7]
    elif letter >= 'A' and letter <= 'G' and number == 10:
      return antibodylist[8]
  
oqdf['Antibody'] = oqdf['Subfolder'].apply(antibody)

#now we can add antibody concentration
#these will stay the same. 

def concentration(subfolder):
    letter = subfolder[0]
    number = int(subfolder[1:])
    
    if letter == 'A':
        return 1
    elif letter == 'D' or letter == 'G':
        return 10
    elif letter == 'C' or letter == 'F' or letter == 'H':
        return 1
    elif letter == 'B' or letter == 'E':
        return 0.1


oqdf['Concentration'] = oqdf['Subfolder'].apply(concentration)

#now we're adding antigens. make sure this makes sense and aligns with the platemap. 

def antigen(subfolder):
    letter = subfolder[0]
    number = int(subfolder[1:])
    
    if letter >= 'B' and letter <= 'D' and number >= 1 and number <= 4:
        return 'hNRXN1a'
    elif letter >= 'E' and letter <= 'G'and number >= 1 and number <=4:
        return 'mNRXN1a'
    elif letter >= 'B' and letter <= 'D'and number >= 5:
        return 'hNRXN1b'
    elif letter >= 'E' and letter <= 'G'and number >= 5:
        return 'mNRXN1b'
    elif letter == 'A':
        return 'WY0041'
    elif letter == 'H':
        return 'WY0041'
    
oqdf['Antigen'] = oqdf['Subfolder'].apply(antigen)

#now we can add the antigen name

sorted_oqdf = oqdf.sort_values(by='Subfolder')
print(sorted_oqdf)
sorted_oqdf.to_csv(os.path.join(root_path,r'finalresults2alpha.csv'))

