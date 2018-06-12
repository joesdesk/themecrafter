# SPECIAL TOKENS


# Utilities to write and read list of stopwords from files

def writelines(file, text):
    with open(file, 'w') as f:
        for t in text:
            f.write(t)
            f.write('\n')
            

def readlines(file):
    with open(file, 'r') as f:
        text = [line.rstrip('\n') for line in f]
        return text
        
        
# The 1000 most used words
# http://splasho.com/upgoer5/
# http://splasho.com/upgoer5/phpspellcheck/dictionaries/1000.dicin
most_frequent_1000 = readlines('themecrafter/nlp/tokens/top1000en.txt')
most_frequent_1000 = frozenset(most_frequent_1000)

# from gensim.parsing.preprocessing import STOPWORDS as gensim_stopwords
gensim_stopwords = readlines('themecrafter/nlp/tokens/gensim_stopwords.txt')
gensim_stopwords = frozenset(gensim_stopwords)

# python's list of punctuations
from string import punctuation
punctuation = frozenset(punctuation)

# NLTK Stopwords: https://pythonspot.com/nltk-stop-words/
from nltk.corpus import stopwords as nltk_stopwords
nltk_stopwords = frozenset(nltk_stopwords.words('english'))


all_stopwords = nltk_stopwords | gensim_stopwords
