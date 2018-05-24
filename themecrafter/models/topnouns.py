 # This model takes as its topics the top n nouns.
 # Then, each document is tokenized by sentence and the sentiment of each
 # sentence is analyzed which is the sentence associated with each topic if it
 # appears in the sentence.
 
 
 def TopNWords:
 
    def __init__(self):
        pass