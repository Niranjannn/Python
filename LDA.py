#Group 12
from __future__ import division, print_function
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import string
from gensim import corpora, models, similarities, matutils
import re
import nltk
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
import logging
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logging.root.level = logging.INFO  # ipython sometimes messes up the logging setup; restore


stopwords = nltk.corpus.stopwords.words('english')+['trump','donald','https','gt','dems','block','agree','amp','used','co', 'rt', 'say','says','goes','retweet','yes' ]
text = open('oneKTweetsFLGAKYNCSCMS.txt','r')
table_p = string.maketrans(string.punctuation, len(string.punctuation) * " ")
table_d = string.maketrans(string.digits, len(string.digits) * " ")
x=[]
test=[]
corpus = []
#stemming
for line in text.readlines():
	ps=PorterStemmer()
	for line1 in line.split():
		w=line1.lower().translate(table_p).translate(table_d).decode('utf-8')
		x.append(ps.stem(w))
for words in x:
	if words not in stopwords:
		test.append(words.split())
dic= corpora.Dictionary(test)
print (dic)
for checkWord in test:
	corpus.append(dic.doc2bow(checkWord))
tfidf = models.TfidfModel(corpus)
#print(type(tfidf))
corpus_tfidf = tfidf[corpus]
#print(type(corpus_tfidf))

NUM_TOPICS = 3
model = models.ldamodel.LdaModel(corpus_tfidf, 
                                 num_topics=NUM_TOPICS, 
                                 id2word=dic, 
                                 update_every=1, 
                                 passes=500)


print (model.print_topics(NUM_TOPICS))

model.log_perplexity(corpus)
