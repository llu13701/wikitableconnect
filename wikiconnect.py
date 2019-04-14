#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 18:17:37 2019

@author: louisalu
"""

import pandas as pd
import dask.dataframe as dd


readpage = dd.read_csv('wikipage.csv', sep='\t', lineterminator='\r', header=None, usecols=[0,2])
readtopic = dd.read_csv('topiccat.csv', sep='\t', lineterminator='\r', header=None, usecols=[0, 1])

readpage.columns=['col1', 'col2']
readtopic.columns=['col1', 'col2']

results=dd.merge(left=readtopic, right=readpage, how='left', on='col1')

results.to_csv('file3.csv', index=False)

