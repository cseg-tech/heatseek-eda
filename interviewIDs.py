#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:46:19 2019

@author: naviyamakhija
"""

import csv

files = ['./data/2018-2019 data pt 1_Oct 01 2018 to Jan 31 2019.csv', './data/2018-2019 data pt 2_ Feb 01 2019 to May 31 2019.csv']
id_dict = dict()
f = open("senors-reinstalled.txt", "a+")
userID = '509'

with open('dorothy_data.csv', mode='w') as dorothy_data:
    dorothy_writer = csv.writer(dorothy_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    with open(files[0]) as csv_file1:
        csv_reader1 = csv.reader(csv_file1, delimiter=',')
    
        for row1 in csv_reader1:
            if(row1[0] == userID):
                dorothy_writer.writerow(row1)
        
        with open(files[1]) as csv_file2:
            csv_reader2 = csv.reader(csv_file2, delimiter=',')
    
            for row2 in csv_reader2:
                if (row2[0] == userID):
                    dorothy_writer.writerow(row2)
            
