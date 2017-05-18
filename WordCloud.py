#Group 12
from __future__ import division, print_function
import nltk
import string
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.stem.porter import PorterStemmer
#Stemming
ps = PorterStemmer()


text = open('oneKTweetsNY.txt','r')
#removing punctuation
table_p = string.maketrans(string.punctuation, len(string.punctuation) * " ")
table_d = string.maketrans(string.digits, len(string.digits) * " ")

words = ''
#List of stopwords 
stopwords = nltk.corpus.stopwords.words('english')+['trump','donald','https','gt','dems','block','agree','amp','used','co', 'rt', 'say','says','goes','retweet','yes' ]
#loop  to remove stopwords
for line in text.readlines():
    w=line.lower().translate(table_p).translate(table_d)
    for wrd in w.split():
        if wrd not in stopwords and len(wrd)>2 and not wrd.startswith("https") and not wrd.endswith("co") and not wrd.startswith("trump") and not wrd.endswith("trump")\
					and not wrd.startswith("tdon") and not wrd.endswith("tdon") \
					and not wrd.startswith("tisn") and not wrd.endswith("tisn") \
					and not wrd.startswith("the") and not wrd.endswith("the") \
					and not wrd.startswith("got") and not wrd.endswith("got") \
					and not wrd.startswith("alawcm") and not wrd.endswith("alawcm") \
					and not wrd.startswith("walkpetejohn") and not wrd.endswith("walkpetejohn") \
					and not wrd.startswith("tdosesn") and not wrd.endswith("tdosesn") \
					and not wrd.startswith("timall") and not wrd.endswith("timall")\
					and not wrd.startswith("rt") and not wrd.endswith("rt")\
					and not wrd.startswith("resist") and not wrd.endswith("resist"):
            words+=' '+wrd

#plotting Wordcloud
wordcloud2 = WordCloud(max_font_size=70).generate(words)
plt.figure()
plt.imshow(wordcloud2)
plt.axis('off')
plt.show()

