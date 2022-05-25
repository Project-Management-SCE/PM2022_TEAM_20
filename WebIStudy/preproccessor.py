import nltk
from nltk.corpus import stopwords, words
import re

def String_connector(sentence):
    text = ' '
    for i in sentence:
        text += (' ' + i)
    return text

def String_Cleaner(subjects):
    return re.sub(r'[^\w\s]',' ',subjects)
  
def Remove_Stopwords(subjects):
                     
    filtered_words = []                              
    StopWords = set(stopwords.words('english'))       
    
    for i in subjects.split():                         
        if not i in StopWords:
            filtered_words.append(i)

    return String_connector(filtered_words)     
      
def Preprocessor(subjects):
    return Remove_Stopwords(String_Cleaner(subjects))
