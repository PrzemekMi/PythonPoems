import os
import pandas as pd
import numpy as  np
import re
import spacy


#function that split the poems in sentences, clean them and save them to a  *.csv
def docs_to_sentences(file, split=r"\n"):
    path = os.getcwd()
    df_docs = pd.read_csv(path+"/" + file)
    number_docs = df_docs.shape[0]
    df_sentences = pd.DataFrame(columns=['doc_id','sentence'])  
    for i in range(number_docs):
        text = df_docs.text[i]
        print("text type", type(text))
        #dictionary to replace unwanted elements
        replace_dict = {'?«' :  '«', '(' :  '', ')' : '', ':' : ',', '.' : ',', ',,,' : ','}
        for x,y in replace_dict.items():
            text = text.replace(x, y)
        text = text.lower()   
        #split into sentences
        sentences = re.split(split, text)
        len_sentences = len(sentences)   
        doc_id = [i] * (len_sentences)
        #save sentence and poem_id
        doc_sentences = pd.DataFrame({'doc_id' : doc_id, 'sentence' : sentences})
        df_sentences = df_sentences.append(doc_sentences)   
    #extra cleaning and reset index
    df_sentences = df_sentences[df_sentences.sentence != '']
    df_sentences.reset_index(drop=True, inplace=True)  
    #saves clean sentences to a .csv file 
    df_sentences.to_csv("sentences_" + file)
    
#saves sentences to  sentences_poems.csv file 
df = docs_to_sentences(file='poems.csv', split=r"\n")