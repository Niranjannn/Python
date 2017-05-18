#Sentiment Analysis and WordCloud creation
import json
import nltk
import string
import matplotlib.pyplot as plt
from textblob import TextBlob

text = open('oneKTweetsCENE.txt','r')
x=[]
z=[] 
#Sentiment Analysis
for twt in text:
	y=twt.decode('utf-8')
	tb = TextBlob(y)
	x.append(tb.sentiment.polarity) 
	z.append(tb.sentiment.subjectivity)
#Plotting Polarity  	
plt.hist(x, bins=20) #, normed=1, alpha=0.75)
plt.xlabel('polarity score:avg {}'.format(sum(x)/len(x)))
plt.ylabel('sentence count')
plt.grid(True)
plt.show()

#Plotting Subjectivity
plt.hist(z, bins=20) #, normed=1, alpha=0.75)
plt.xlabel('subjectivity score:avg {}'.format(sum(z)/len(z)))
plt.ylabel('sentence count')
plt.grid(True)
plt.savefig('subjectivity.pdf')
plt.show()
