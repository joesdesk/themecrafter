# Model Development

## Qualitative Analysis of Surveys


* Medelyan, Alyona. _Your guide to open-end coding of customer surveys._ Thematic. 2017. [link](https://getthematic.com/coding-open-ended-questions/)
* Zapin, Marni. _The Challenge of Analyzing Open-Ended Survey Question_. SurveyGizmo. 2013. [link](https://www.surveygizmo.com/resources/blog/the-challenge-of-analyzing-open-ended-survey-questions/)
* Fusco, Carl. _How to Code Open-End Survey Question Responses_. LinkedIn. 2015. [link](https://www.linkedin.com/pulse/how-code-open-end-survey-question-responses-carl-fusco)

* infosurv. _How to Code Open-End Survey Question Responses_. [link](https://www.infosurv.com/how-to-code-open-end-survey-question-responses/)

## Models

### Semi-supervised Non-negative Matrix Factorization
This method extends regular NMF to allow reference matrices constructed by hand to be incorporated in the optimization process so that the resulting factored matrix not only tries to approximate the original matrix, but are also similar to the reference matrices.

Choo, Jaegul, Changhyun Lee, Chandan K. Reddy, and Haesun Park. "UTOPIAN: User-Driven Topic Modeling Based on Interactive Nonnegative Matrix Factorization." IEEE Transactions __19__, 12 (2013).




## Experimental Datasets

The [datasets.py](datasets.py) module contains python functions that makes it easy to load cleaned and tidied data for testing the models.

__Sources__

* The 20 newsgroups text dataset on scikit-learn. [link](http://scikit-learn.org/stable/datasets/twenty_newsgroups.html).
* Survey Data not included in this repository
* Public university/college reviews dataset scraped from GradReports. [link](www.gradreports.com)

__Other Potential Sources__

*
