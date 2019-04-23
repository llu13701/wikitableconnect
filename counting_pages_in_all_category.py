#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 19:57:29 2019

@author: amit
"""

import os
import pandas as pd
import dask.dataframe as dd


def main():
    os.chdir('/Users/amit/Desktop/wikitableconnect')
    
    # read into the all category: chuck only later
    file_all_cat=pd.read_csv('title_cat_sample_10k.csv', sep='\\t', header=None, usecols=[2])
    
    # counting the category of the unqiue values
    count_cat=pd.Series(file_all_cat.values.ravel()).dropna().value_counts()



    

    
    
