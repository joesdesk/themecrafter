# Filter out stop words and punctuations

from string import punctuation
punctuation = list(punctuation)

from nltk.corpus import stopwords
nltk_stopwords = stopwords.words('english')

from gensim.parsing.preprocessing import STOPWORDS
gensim_stopwords = list(STOPWORDS)
