# Model Development

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
* Student reviews on StudentsReview. [link](http://www.studentsreview.com/)

__Other Potential Sources__

These sources of text data are potential additions to the project.

* The python Natural Language Tookit (NLTK). [link](http://www.nltk.org/nltk_data/)
  * Movie Review Data by Bo Pang, Lillian Lee, and Shivakumar Vaithyanathan. [link](http://www.cs.cornell.edu/people/pabo/movie-review-data/)
* Yelp reviews. [link](https://www.yelp.com/dataset)
