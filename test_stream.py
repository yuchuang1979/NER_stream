#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

from annotated_text import annotated_text

import spacy

nlp = spacy.load('en_core_web_sm')

#https://github.com/tvst/st-annotated-text

#x = st.slider('Select a value')

sentence = st.text_input('Input your sentence here:') 

st.write('The input sentence is: \n', sentence)

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
        ent = None
        
def generate_ents(doc):
    list_param = []
    if doc.ents:
        i = 0
        for token in doc:
            extended_token = token.text + " "
            if token.idx < doc.ents[i].start_char:
                #print(token.text)
                #print(token.idx)
                list_param.append(extended_token)
            elif token.idx < doc.ents[i].end_char:
                #print("passed")
                #print(token.text)
                #print(token.idx)
                pass
            else:
                cur_color = get_color(doc.ents[i].label_)
                extended_ent = doc.ents[i].text + " "
                if cur_color:
                    list_param.append((extended_ent, doc.ents[i].label_, cur_color))
                else:
                    list_param.append(extended_ent)
                i = i + 1
                list_param.append(extended_token)
    else:
        for token in doc:
            extended_token = token.text + " "
            list_param.append(extended_token)
    
    return list_param


doc = nlp(sentence)
show_ents(doc)
list_param = generate_ents(doc)
print(list_param)


        
        
        
    
#def list_annotate(*params):
#    if params:
        
annotated_text(*list_param)
#print(list_param)  


# In[ ]:




