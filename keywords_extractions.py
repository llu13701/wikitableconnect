#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#https://stackoverflow.com/questions/49500259/how-to-find-most-frequently-used-words-used-on-data-using-python
"""
Created on Tue Apr 23 13:41:15 2019
@author: louisalu
"""

import os
import pandas as pd
import spacy
from spacy import displacy
import en_core_web_sm
nlp = en_core_web_sm.load()

from collections import Counter
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk, punkt,sent_tokenize,regexp_tokenize,FreqDist
from nltk.corpus import stopwords
from sklearn.datasets import fetch_20newsgroups
from wordcloud import WordCloud, STOPWORDS



#preprocessing the questions for POS analysis
def preprocess(sent):
    sent=nltk.word_tokenize(sent)
    sent=nltk.pos_tag(sent)
    return sent

def tokenize(text, pat='(?u)\\b\\w\\w+\\b', stop_words='english', min_len=2):
    if stop_words:
        stop = set(stopwords.words(stop_words))
    return [w
            for w in regexp_tokenize(text.casefold(), pat)
            if w not in stop and len(w) >= min_len]

# so training words distribution with the 20newsgroups
def get_data(): 
    twenty_train = \
        fetch_20newsgroups(subset='all', shuffle=True)
    
    X_train = pd.DataFrame(twenty_train.data, columns=['text'])
    return X_train



def main():
    os.chdir('/Users/amit/Desktop/wikitableconnect')
    question_file_name='question_testing_sample.csv'
    sample_question=pd.read_csv(question_file_name, header=None, encoding='latin1')
    sample_question.columns=['Question']
    num_lines=len(sample_question['Question'])
    for i in range(num_lines):
        print (i, "out of", num_lines, "\n")
        question=sample_question.iloc[i]
        # relate all the special character
        question=question.str.replace(r'\W+', ' ')
        question=question.to_string()
        # using nltk to find noun and so
        question_pos_analysis = preprocess(question)
        ner_one=nlp(question)
        
        #X-train represents the articles from all category
        X_train = get_data()
        words = tokenize(question, min_len=3)
        # remove the "question:
        words.remove('question')
        
        for i in words:
            #single_word=words[i]
            single_word='mblawson' # this is just for testing
            



