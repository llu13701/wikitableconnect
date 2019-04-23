#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 13:41:15 2019

@author: louisalu
"""

import os
import pandas as pd
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp=en_core_web_sm.load()

def main():
    os.chdir('/Users/louisalu/Documents/wikiproject')
    question_file_name='question_testing_sample.csv'
    sample_question=pd.read_csv(question_file_name, header=None, encoding='latin1')
    sample_question.columns=['Question']
    num_lines=len(sample_question['Question'])
    for i in range(num_lines):
        print (i, "out of", num_lines, "\n")
        question=sample_question.iloc[i]
        # relate all the special character
        question=question.str.replace(r'\W+', ' ')

        
