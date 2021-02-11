import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import spacy
import os
import numpy as  np
import re
import nlp

#function to generate a poem
def poem_generator(file, word, n_sents=4):
        #load the english model from Spacy
        #nlp = spacy.load('en_core_web_sm')
        nlp = spacy.load("pl_core_news_lg")
        init_str = nlp(word)
        path = os.getcwd()
        sentences = pd.read_csv(path+'/'+ file)
        sup_index= sentences.shape[0]
        poem_id = int()
        poem =[]
        #generate the sentences
        for i in range(n_sents):
            rand_sent_index = np.random.randint(0, sup_index, size=30)
            sent_list = list(sentences.sentence.iloc[rand_sent_index])
            #transform sentences to a Spacy Doc object
            docs = nlp.pipe(sent_list)
            sim_list = []
            #compute similarity for each sentence
            for sent in docs:
                similarity = (init_str.similarity(sent))
                sim_list.append(similarity)
            #saves similarity to DataFrame
            df_1 = pd.DataFrame({'similarity' : sim_list, 'doc_id' : sentences.doc_id.iloc[rand_sent_index] }, index=rand_sent_index)   
            df_1 = df_1[df_1.doc_id != poem_id]
            df_1.sort_values(by='similarity', inplace=True, ascending=False)
            sent_index= df_1.index[0]
            sent = sentences.sentence[sent_index]
            #erase line jumps and carriage return
            replace_dict = {'\n' :  '', '\r' :  ''}
            for x,y in replace_dict.items():
                sent = sent.replace(x, y)
            poem.append(sent)    
            poem_id = df_1.doc_id.iloc[0]
            init_str = nlp(sent)  
        #join the sentences with a line break
        str_poem = ("\n".join(poem)) 
        return str_poem

#generate a poem with initial word ='fear'
poem = poem_generator(file='sentences_poems.csv',word='piękna')

print(poem)


def format_poem(text):
    text = text[:1].upper() + text[1:]
    text = text[:-1] + '.'
    return text   

#print the poem with new format 
final_poem = format_poem(poem)
print(final_poem)