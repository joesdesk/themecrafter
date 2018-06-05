# Filter out stop words and punctuations

from string import punctuation
punctuation = frozenset(punctuation)

from nltk.corpus import stopwords as nltk_stopwords
nltk_stopwords = frozenset(nltk_stopwords.words('english'))

from gensim.parsing.preprocessing import STOPWORDS as gensim_stopwords


all_stopwords = nltk_stopwords | gensim_stopwords