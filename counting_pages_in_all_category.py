#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:24:36 2019

@author: louisalu
"""


import os
import pandas as pd


def main():
    #os.chdir('/Users/louisalu/Documents/wikiproject')
    
    # read into the all category: chuck only later
    cat_file_name='title_cat_sample_10k.csv'
    chucksize=50
    
    results=pd.concat([chuck.apply(pd.Series.value_counts) for chuck in pd.read_csv(cat_file_name, error_bad_lines=False, usecols=[2], 
                       sep='\\t', header=None, chunksize=chucksize)])
    final_results=results.groupby(results.index).sum()
    final_results.to_csv("outputcattest.csv", index=True, header=False, chunksize=chucksize)

    

if __name__=="__main__":
    main()



    

    
    
