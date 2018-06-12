#!/usr/bin/env python -*- coding: utf-8 -*-
#
# Python Word Sense Disambiguation (pyWSD): all-words WSD
#
# Copyright (C) 2014-2017 alvations
# URL:
# For license information, see LICENSE.md

from string import punctuation

from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords

from pywsd.lesk import simple_lesk, original_lesk
from pywsd.similarity import max_similarity
from pywsd.utils import lemmatize, lemmatize_sentence

from nltk.stem import PorterStemmer, WordNetLemmatizer
from .nltklemmatizer import penn2wnpos as penn2morphy

"""
This is a module for all-words full text WSD
This would involve:
Step 1: First tokenize your text such that each token is separated by whitespace
Step 2: Iterates through the tokens and only disambiguate the content words.
"""

stopwords = stopwords.words('english') + list(punctuation)


# Overwrite the lemmatize function

porter = PorterStemmer()
wnl = WordNetLemmatizer()

def lemmatize_sentence(sentence: str, neverstem=False, keepWordPOS=False,
                       tokenizer=word_tokenize, postagger=pos_tag,
                       lemmatizer=wnl, stemmer=porter) -> list:

    words, lemmas, poss = [], [], []
    for word, pos_ in postagger(tokenizer(sentence)):
        pos = penn2morphy(pos_)
        lemmas.append(lemmatize(word.lower(), pos, neverstem,
                                lemmatizer, stemmer))
        poss.append(pos_)
        words.append(word)

    if keepWordPOS:
        return words, lemmas, poss#[None if i == '' else i for i in poss]

    return lemmas


# 
def disambiguate(sentence, algorithm=simple_lesk,
                 context_is_lemmatized=False, similarity_option='path',
                 keepLemmas=False, prefersNone=True, from_cache=True):
    tagged_sentence = []
    # Pre-lemmatize the sentnece before WSD
    if not context_is_lemmatized:
        surface_words, lemmas, morphy_poss = lemmatize_sentence(sentence, keepWordPOS=True)
        lemma_sentence = " ".join(lemmas)
    else:
        lemma_sentence = sentence # TODO: Miss out on POS specification, how to resolve?
    for word, lemma, pos_ in zip(surface_words, lemmas, morphy_poss):
        pos = penn2morphy(pos_)
        if lemma not in stopwords: # Checks if it is a content word
            try:
                wn.synsets(lemma)[0]
                if algorithm == original_lesk: # Note: Original doesn't care about lemmas
                    synset = algorithm(lemma_sentence, lemma, from_cache=from_cache)
                elif algorithm == max_similarity:
                    synset = algorithm(lemma_sentence, lemma, pos=pos, option=similarity_option)
                else:
                    synset = algorithm(lemma_sentence, lemma, pos=pos, context_is_lemmatized=True,
                                       from_cache=from_cache) 
                synset = synset.name()
            except: # In case the content word is not in WordNet
                synset = ''#'#NOT_IN_WN#'
        else:
            synset = ''#'#STOPWORD/PUNCTUATION#'
        if keepLemmas:
            tagged_sentence.append((word, lemma, pos_, synset))
    #    else:
    #        tagged_sentence.append((word, synset))
    # Change #NOT_IN_WN# and #STOPWORD/PUNCTUATION# into None.
    #if prefersNone and not keepLemmas:
    #    tagged_sentence = [(word, None) if str(tag).startswith('#')
    #                       else (word, tag) for word, tag in tagged_sentence]
    #if prefersNone and keepLemmas:
    #    tagged_sentence = [(word, lemma, None) if str(tag).startswith('#')
    #                       else (word, lemma, tag) for word, lemma, tag in tagged_sentence]
    return tagged_sentence
    
    
if __name__=='__main__':
    
    sentence = "I went to the bank to get a loan."
    
    surface_words, lemmas, morphy_poss = lemmatize_sentence(sentence, keepWordPOS=True)
    
    print(surface_words, lemmas, morphy_poss)
    
    result = disambiguate('I went to the bank to deposit my money', \
        keepLemmas=True, prefersNone=False)
    
    print(result)
    