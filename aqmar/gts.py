# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 15:38:06 2020

@author: Hussam Hallak
"""

from googletrans import Translator
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import os
import glob
  
def printArray(array, array_name):
    print (array_name + ":" + "\n" + "--------------")
    for item in array:
        if item is not None:
            translator = Translator()
            ar_item = translator.translate(item, src='en', dest='ar')
            if ar_item is not None:
                print (ar_item.text)

java_path = "C:\Program Files (x86)\Java\jre1.8.0_251/java.exe"
os.environ['JAVAHOME'] = java_path

st = StanfordNERTagger(r'stanford-ner-4.0.0/stanford-ner-4.0.0/classifiers/english.all.3class.distsim.crf.ser.gz',
					   r'stanford-ner-4.0.0/stanford-ner-4.0.0/stanford-ner.jar',
					   encoding='utf-8')

files = glob.glob(r'.\aqmar\translated_articles\*.txt')

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

for file in files:
    iFile = open(file, 'r')
    oFileL = open(THIS_FOLDER + file + ".locations.txt", 'w')
    oFileO = open(THIS_FOLDER + file + ".organizations.txt", 'w')
    oFileP = open(THIS_FOLDER + file + ".persons.txt", 'w')
    text = iFile.read() 
    tokenized_text = word_tokenize(text)
    classified_text = st.tag(tokenized_text)
    locations = []
    persons = []
    organizations = []
    for word in classified_text:
        if word[1] == "LOCATION":
            locations.append(word[0])
        if word[1] == "PERSON":
            persons.append(word[0])
        if word[1] == "ORGANIZATION":
            organizations.append(word[0]) 
    for entry in locations:
        oFileL.write(entry + "\n")
    for entry in organizations:        
        oFileO.write(entry + "\n")
    for entry in persons:
        oFileP.write(entry + "\n")
    iFile.close()
    oFileL.close()
    oFileO.close()
    oFileP.close()
    
    '''
    printArray(locations, "Locations")
    printArray(organizations, "Organizations")
    printArray(persons, "Persons")
    
'''