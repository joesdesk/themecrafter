# Installation

* Dependencies
  * Python

## Dependencies

* Python



### Python

### Python Packages



For natural language processing
* `scikit-learn`, and its [dependencies](http://scikit-learn.org/stable/install.html#installing-the-latest-release)
### gensim
* https://radimrehurek.com/gensim/install.html

* `nltk` (3.3) [link](http://www.nltk.org/api/nltk.html)
* `spacy`

### textblob 0.15.1
```
pip install -U
python -m textblob.download_corpora
```

### Beautiful Soup
* `beautifulsoup4`, a python package called [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
*
Documentation:
* BeautifulSoup 4 Reference. [link](http://omz-software.com/pythonista/docs/ios/beautifulsoup_ref.html)
* Doesn't support xpath. [link](https://stackoverflow.com/questions/11465555/can-we-use-xpath-with-beautifulsoup)


### Third Party Packages
* `stanford`

NLTK can make calls to the server (see [link](https://github.com/nltk/nltk/wiki/Installing-Third-Party-Software)).

```
cd stanford-corenlp-full-2016-10-31
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer \
    -preload tokenize,ssplit,pos,lemma,parse,depparse \
    -status_port 9000 -port 9000 -timeout 15000
```



### Graphical User Interface
* `wxPython`, and its [dependencies](https://github.com/wxWidgets/Phoenix#prerequisites)
  * Because wxPython is responsible for the graphical user interface, it's dependencies for linux will include gtk 3 libraries



# Requirements:
