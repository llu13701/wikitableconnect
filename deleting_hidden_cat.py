#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 23:41:55 2019

@author: louisalu
"""

# FIRST STEP IS TO CLEAN THE STRING WITHOUT THE UNDERLYING
# Second step is to match it with the table, maybe an inner join is the best way to do. 

import pandas as pd
import os
import dask.dataframe as dd


def main():
    os.chdir('/Users/louisalu/Documents/wikiproject')
    out_csv='/Users/louisalu/Documents/wikiproject/clean_cat.csv'

    #read all the hidden cat
    read_hidden_cat = pd.read_csv('output_all_hidden_category.csv', sep='\t', header=None, usecols=[0])
    read_hidden_cat.columns=['Cat']
    
    # conver space to _
    read_hidden_cat=read_hidden_cat.replace(' ', '_', regex=True)
    #replace all special character to none
    read_hidden_cat['Cat']=read_hidden_cat['Cat'].str.replace(r'\W+', '')
    
    
    
    # this is the file name for the all category
    all_cat_file_name='title_cat_sample_10k.csv'
    # change the chucksize
    chucksize=50
    
    
    read_all_cat=dd.read_csv(all_cat_file_name, error_bad_lines=False, header=None, sep='\\t')
    read_all_cat.columns=['ID', 'Page_title', 'Cat']

    number_lines=len(read_all_cat['Cat'])

    
    for i in range(1, number_lines, chucksize):
        print (i, "out of", number_lines, "\n")
        read_all_cat=pd.read_csv(all_cat_file_name, error_bad_lines=False, sep='\\t', header=None, 
                              nrows=chucksize, skiprows=i, engine='python')
        read_all_cat.columns=['ID', 'Page_title', 'Cat']
        #read_all_cat.head()
        #cleanup Cat empty space and special character
        read_all_cat['Cat']=read_all_cat['Cat'].str.replace(' ', '_')
        read_all_cat['Cat']=read_all_cat['Cat'].str.replace(r'\W+', '')
    
        #match read_all_cat hidden category with read_hidden_cat and then delete it
        # to delete based on contain
        
        searchfor=['Wikipedia','Articles_','_articles', 'Topimportance','WikiProject','_pages' ,'Redirects_',
                  '_redirects']
        read_all_cat=read_all_cat[~read_all_cat.Cat.str.contains("|".join(searchfor), na=False)]
        
        common=read_all_cat.merge(read_hidden_cat, on=['Cat'])
        results=read_all_cat[(~read_all_cat.Cat.isin(common.Cat))]
        if i==1:
            results.columns=['ID', 'Page_title', 'Cat']
            results.to_csv(out_csv, index=False, header=True, sep='\t', chunksize=chucksize)
        else:
            results.to_csv(out_csv, index=False, header=False,
                   mode='a',sep='\t',
                   chunksize=chucksize)
        



if __name__=="__main__":
    main()



