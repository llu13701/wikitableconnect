#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 18:17:37 2019

@author: louisalu
"""

import pandas as pd
import os
import dask.dataframe as dd


os.chdir('/Users/louisalu/Documents/wikiproject')

readpage = pd.read_csv('pageoutput2.csv', sep='\t', header=None, usecols=[0,2])
readtopic = pd.read_csv('topicoutput2.csv', sep='\t', header=None, usecols=[0, 1])
readpage.columns=['col1', 'col2']
readtopic.columns=['col1', 'col2']


out_csv='/Users/louisalu/Documents/wikiproject/output.csv'

number_lines=len(readtopic['col1'])

chucksize=500

for i in range(1, number_lines, chucksize):
    print (i, "out of", number_lines/chucksize, "\n")
    
    readtopicchuck=pd.read_csv('topicoutput2.csv', sep='\t', header=None, 
                              usecols=[0,1], nrows=chucksize, skiprows=i)
    readtopicchuck.columns=['col1', 'col2']
    results=pd.merge(left=readpage, right=readtopicchuck, how='right', on='col1')
    if i==1:
        results.columns=['id', 'title', 'topics']
    results.to_csv(out_csv, index=False, header=False,
                   mode='a',sep='\t',
                   chunksize=chucksize)
        
    
