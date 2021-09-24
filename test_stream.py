#!/usr/bin/env python
# coding: utf-8

# In[1]:

#from __future__ import unicode_literals, print_function
import streamlit as st
from annotated_text import annotated_text
import spacy
#from spacy.lang.en import English # updated

nlp = spacy.load('en_core_web_sm')

#https://github.com/tvst/st-annotated-text

#x = st.slider('Select a value')

sentences = st.text_input('Input your sentences here:') 

#st.write('The input sentences are: \n', sentences)

def show_ents(doc): 
    if doc.ents: 
        for ent in doc.ents: 
            print(ent.text + ' - ' +
                  str(ent.start_char) +' - ' + 
                  str(ent.end_char) + ' - ' + 
                  ent.label_+ ' ') 
                  #+ str(spacy.explain(ent.label_)))
    else: 
        print('No named entities found.')
        

#nlp = English()
#nlp.add_pipe(nlp.create_pipe('sentencizer')) # updated
doc = nlp(sentences)
#sentences = [sent.string.strip() for sent in doc.sents]

def get_color(ent):
    if ent == "PERSON":
        return "#8ef"
    elif ent == "DATE":
        return "#faa"
    elif ent == "GPE":
        return "#afa"
    elif ent == "ORG":
        return "#afe"
    else:
        return None
        
def generate_ents(doc):
    list_param = []
    if doc.ents:
        i = 0
        len_ents = len(doc.ents)
        ent_appended = False
        for token in doc:
   
            extended_token = token.text + " "
            if i < len_ents and token.idx < doc.ents[i].start_char:
                list_param.append(extended_token)
            elif i < len_ents and token.idx < doc.ents[i].end_char:
                if not ent_appended:
                    #print(doc.ents[i].label_)
                    cur_color = get_color(doc.ents[i].label_)
                    #print(cur_color)
                    extended_ent = doc.ents[i].text + " "
                    if cur_color:
                        list_param.append((extended_ent, doc.ents[i].label_, cur_color))
                    else:
                        list_param.append(extended_ent)
                    ent_appended = True
                if token.idx + token.__len__() == doc.ents[i].end_char: #the token is the last token in ent
                    ent_appended = False
                    i = i + 1
            else:
                list_param.append(extended_token)
            #print(list_param)
            #input("input any")
    else:
        for token in doc:
            extended_token = token.text + " "
            list_param.append(extended_token)
    
    return list_param


doc = nlp(sentences)
#show_ents(doc)
#print(doc.ents)
list_param = generate_ents(doc)


        
        
        
    
#def list_annotate(*params):
#    if params:
        
annotated_text(*list_param)
#print(list_param)  


# In[ ]: