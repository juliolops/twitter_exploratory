import requests
import os
import json
import pandas as pd
import csv
import datetime
import dateutil.parser
import unicodedata
import time
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import nltk
from unicodedata import normalize as norm
import re



def plot_bar_count_words(text_column=None,
                         label_column=None,
                         name_class=None,
                         dataframe=None,
                         metric='SUM',
                         top=50,return_df=True, ngram = (1,1)):
    
    corpus = dataframe[text_column].values
    
 
    
    vectorizer = CountVectorizer(ngram_range=ngram)
    data_vect = vectorizer.fit_transform(corpus)
    data_vect = data_vect.toarray()
    
    
    df_count_words =  pd.DataFrame({
    "WORDS":vectorizer.get_feature_names() ,
    "MEAN":data_vect.mean(axis=0),
    "SUM":data_vect.sum(axis=0),
    "STD":data_vect.std(axis=0),
    }) 
    
    

    if return_df:
    
        return df_count_words[[metric,'WORDS']].sort_values(by=[metric],ascending=False)[0:top]
    
    else:
        
        fig = plt.figure(figsize=(15,10))
        
        ax = sns.barplot(x=metric, 
                 y="WORDS", 
                 data=df_count_words[[metric,'WORDS']].sort_values(by=[metric],
                                                                            ascending=False)[0:top])


def convert_text_to_no_repeat_words(text):

    text_with_no_repeat_words = text.split(" ")

    text_with_no_repeat_words = [i for i in text_with_no_repeat_words if i!=""]

    text_with_no_repeat_words = set(text_with_no_repeat_words)

    text_with_no_repeat_words = list(text_with_no_repeat_words)

    text_with_no_repeat_words = " ".join(text_with_no_repeat_words)

    return text_with_no_repeat_words
        



def extract_hashtags_citations(tweet,extract="both", remove_content_tweet=True, content=""):


    string_only_hashtags = ""
    string_only_citations = ""

    if extract == "hashtag" or extract == "both":

        list_hashtags = re.findall(r"#[a-zA-Zà-úÀ-Ú0-9]+",tweet)
        
        string_only_hashtags = " ".join(list_hashtags)

    if extract == "citation" or extract == "both":

        list_citations = re.findall(r"@[a-zA-Zà-úÀ-Ú0-9]+",tweet)
        
        string_only_citations = " ".join(list_citations)

    if remove_content_tweet:

        string_only_hashtags = re.sub(r"(?i)\#{0}\s|\s\#{0}$|^\#{0}\s|^\#{0}$".format(content)," ",string_only_hashtags)

        string_only_citations = re.sub(r"(?i)\@{0}\s|\s\@{0}$|^\@{0}\s|^\@{0}$".format(content)," ",string_only_citations)
    
    
    return string_only_hashtags + string_only_citations



def text_cleaner(text,stop_words_domain =[],rmv_citations=False,rmv_hashtags=False,rmv_stop_words=True):


    if rmv_hashtags:

        text = re.sub("#[a-zA-Zà-úÀ-Ú0-9]+"," ",text)

    if rmv_citations:

        text = re.sub("@[a-zA-Zà-úÀ-Ú0-9]+"," ",text)

    
    nltk_stopwords =  stopwords.words('portuguese') + stop_words_domain

    nltk_stopwords_processed = [norm('NFKD', i).encode('ascii', 'ignore').decode().lower() for i in nltk_stopwords]

    regex_stop_words = '|'.join(nltk_stopwords)

    
    regex_remove_https = 'https([a-zA-Zà-úÀ-Ú0-9]|[-()\#/@;:<>{}`+=~|.!?,])+'


    text_without_https = re.sub(r"(\s|^){0}(\s{0})*($|\s)".format(regex_remove_https)," ",text)


    text_without_special_caracteres = re.sub(r"[^a-zA-ZÀ-Úà-ú]+"," ",text_without_https)

    text_without_alone_caractere = re.sub(r"\s[a-zA-ZÀ-Úà-ú]\s|\s[a-zA-ZÀ-Úà-ú]$|^[a-zA-ZÀ-Úà-ú]\s"," ",text_without_special_caracteres)
    

    text_pattern_space = re.sub(r"\s+"," ",text_without_alone_caractere)

    
    text_split = text_pattern_space.split(" ")

    
    text_list = [i for i in text_split  if norm('NFKD', i).encode('ascii', 'ignore').decode().lower() not in nltk_stopwords_processed]


    text_final = " ".join(text_list)


    return text_final


def text_easy_cleaner(text,rmv_https=True,rmv_content=True,content=None,rmv_hashtags=True,rmv_citations=True):


    if rmv_hashtags:

        text = re.sub("#[a-zA-Zà-úÀ-Ú0-9]+","",text)

    if rmv_citations:

        text = re.sub("@[a-zA-Zà-úÀ-Ú0-9]+","",text) 


    if rmv_https:

        regex_remove_https = 'https([a-zA-Zà-úÀ-Ú0-9]|[-()\#/@;:<>{}`+=~|.!?,])+'


        text = re.sub(r"(\s|^){0}(\s{0})*($|\s)".format(regex_remove_https)," ",text)

    
    if rmv_content and content is not None:
        

        text = re.sub(r"(\s|^){0}(\s{0})*($|\s)".format(content)," ",text)

 

    return text

