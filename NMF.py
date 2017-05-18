import numpy as np  
import glob
import os
#Group 12
import string
import nltk
from sklearn.metrics.pairwise import euclidean_distances, cosine_similarity
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import string
import sys
from wordcloud import WordCloud
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import decomposition



text = open('tenKTweets2.txt','r')

strtweet=''
listTweet=[]

table_p = string.maketrans(string.punctuation, len(string.punctuation) * " ")
table_d = string.maketrans(string.digits, len(string.digits) * " ")
       
words = ''
stopwords = nltk.corpus.stopwords.words('english')+['trump','https', 'co', 'rt','https','tdon','tisn','tcan','ryou','alawcm','walkpetejohn','tdosesn','timall','retweet','timall' ]

for line in text.readlines():
    if len(line.strip())>1:
       strtweet=' '
       line=line.lower().translate(table_p).translate(table_d).decode('utf-8')

       for wrd in line.split():
           if wrd not in stopwords and len(wrd)>2 and not wrd.startswith("https") and not wrd.endswith("co") and not wrd.startswith("trump") and not wrd.endswith("trump")\
					and not wrd.startswith("tdon") and not wrd.endswith("tdon") \
					and not wrd.startswith("tisn") and not wrd.endswith("tisn") \
					and not wrd.startswith("tcan") and not wrd.endswith("tcan") \
					and not wrd.startswith("ryou") and not wrd.endswith("ryou") \
					and not wrd.startswith("alawcm") and not wrd.endswith("alawcm") \
					and not wrd.startswith("walkpetejohn") and not wrd.endswith("walkpetejohn")\
					and not wrd.startswith("tdosesn") and not wrd.endswith("tdosesn") \
					and not wrd.startswith("timall") and not wrd.endswith("timall")\
					and not wrd.startswith("rt") and not wrd.endswith("rt")\
					and not wrd.startswith("timall") and not wrd.endswith("timall")\
                	and not wrd.startswith("retweet") and not wrd.endswith("retweet"):
              strtweet+=' '+ wrd
       listTweet.append(strtweet)



names = []
#Vectorizer
vectorizer = TfidfVectorizer(stop_words='english', min_df=2)
doc_term_matrix = vectorizer.fit_transform(listTweet)
vocab = vectorizer.get_feature_names()

num_topics = 10

clf = decomposition.NMF(n_components=num_topics, random_state=1)
doctopic = clf.fit_transform(doc_term_matrix)

topic_words = []
num_top_words = 5

print (vocab[100])
for topic in clf.components_:
    word_idx = np.argsort(topic)[::-1][0:num_top_words]
    topic_words.append([vocab[i] for i in word_idx])

for t in range(len(topic_words)):
    print ("Topic {}: {}".format(t, ' '.join(topic_words[t][:15])))


