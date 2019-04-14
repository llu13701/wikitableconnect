#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 18:17:37 2019

@author: louisalu
"""

#import pandas as pd
import os
import dask.dataframe as dd

#change the directory and also the file name
os.chdir('/Users/louisalu/Documents/wikiproject')

readpage = dd.read_csv('pageoutput2.csv', sep='\t', header=None, usecols=[0,2])
readtopic = dd.read_csv('topicoutput2.csv', sep='\t', header=None, usecols=[0, 1])

readpage.columns=['col1', 'col2']
readtopic.columns=['col1', 'col2']

#results=dd.merge(left=readtopic, right=readpage, how='left', on='col1')

results=dd.merge(left=readpage, right=readtopic, how='right', on='col1')

results.columns=['id', 'title', 'cat']

results.to_csv(r'*.csv', sep='\t', header=True, index=False)

