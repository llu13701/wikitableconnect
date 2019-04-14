#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 18:17:37 2019

@author: louisalu
"""

import pandas as pd

readpage = pd.read_csv('wikipage.csv', delimiter=',', header=None, usecols=[0,2])
readtopic = pd.read_csv('topiccat.csv', delimiter=',', header=None, usecols=[0, 1])

readpage.columns=['col1', 'col2']
readtopic.columns=['col1', 'col2']

results=pd.merge(left=readtopic, right=readpage, how='left', on='col1')
