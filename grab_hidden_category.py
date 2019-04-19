#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:03:18 2019

@author: louisalu
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import re


def main():
    html_page = urlopen("https://en.wikipedia.org/wiki/Category:Hidden_categories")
    output_file="output_all_hidden_category.csv"
    #132 pages of worth of wiki-hidden-cat
    for i in range(133):
        print (i)
        row_list=[]
        soup = BeautifulSoup(html_page)
        #not working
        #html_next=soup.find_all(href=re.compile(r"^/w/index.php?title=Category:Hidden_categories&amp;subcatfrom"))
        
        for data in soup.findAll('a', {'class': 'CategoryTreeLabel CategoryTreeLabelNs14 CategoryTreeLabelCategory'}):
            row_list.append(data.text.strip())
        df=pd.DataFrame(row_list)
        if i==0:
            df.to_csv(output_file, sep="\t", index=False)
        else:
            df.to_csv(output_file, mode="a", sep="\t", index=False, header=False)
        
        #finding the next url before moving
        html_next=soup.find("a", string="next page")
        string_html="https://en.wikipedia.org"+html_next['href']
        html_page=urlopen(string_html)
    





if __name__=="__main__":
    main()
