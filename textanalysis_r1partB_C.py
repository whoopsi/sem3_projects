# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 19:21:31 2016

@authors: gupta, mdavila
"""
import json
import os
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import string
import nltk
path= '/Users/gupta/Downloads/data science/PJ1/data/'
tweets=[]
usrtweets = {}
for fname in os.listdir(path):
    #print fname
    if not fname.startswith('.') and os.path.isfile(os.path.join(path, fname)):
        with open(path + fname,'r') as a:
            content= json.load(a)
            for i in range(0,len(content)):
                tweets.append(content[i]['text'])
                usrtweets[content[i]['user']['screen_name'].encode('utf-8')] = content[i]['text'] #storing user id and tweet text in dict
#print len(tweets)
#print tweets[:10]
# Cleaning the tweets for punctuations and digits which is data 2
data1=[]
data2=[]
usrpol = {}
usrsub = {}
stopwords = nltk.corpus.stopwords.words('english')
stopwords2= ['co','RT','rt','https','via','anti','says','...rt']
stopwords.extend(stopwords2)
for twt in tweets:
    p = string.punctuation
    d = string.digits
    table_p = string.maketrans(p, len(p) * " ")
    table_d = string.maketrans(d, len(d) * " ")
    #print(type(table_p))
    #print(twt.encode('utf-8').translate(table_p))
    data1.append(twt.encode('utf-8').translate(table_p))
    #data2.append(data1.translate(table_d))
### Sentiment Analysis
for key, value in usrtweets.iteritems(): #performing sentiment analysis and storing polarity scores in dict 
    blob = TextBlob(value)
    usrpoltmp = {}
    usrpoltmp[key] = [blob.sentiment.polarity]
    usrtwtcnt = 0
    for key, value in usrpoltmp.iteritems():
        if key in usrpol.iterkeys():
            usrpol[key] = ([usrpol.get[key] + blob.sentiment.polarity])/usrtwtcnt 
        else:
            usrpol[key] = [blob.sentiment.polarity]
    usrtwtcnt = usrtwtcnt + 1
for key, value in usrtweets.iteritems(): #performing sentiment analysis and storing subjectivity scores in dict and outputting min and max scores
    blob = TextBlob(value)
    usrsubtmp = {}
    usrsubtmp[key] = [blob.sentiment.subjectivity]
    usrtwtcnt = 0
    for key, value in usrsubtmp.iteritems():
        if key in usrsub.iterkeys():
            usrsub[key] = ([usrsub.get[key] + blob.sentiment.subjectivity])/usrtwtcnt 
        else:
            usrsub[key] = [blob.sentiment.subjectivity]
        usrtwtcnt = usrtwtcnt + 1
topusrslst = [max(usrpol.items(), key=lambda k: k[1]), min(usrpol.items(), key=lambda k: k[1]),max(usrsub.items(), key=lambda k: k[1]),min(usrsub.items(), key=lambda k: k[1])]
topusrs = [max(usrpol.items(), key=lambda k: k[1])[0], min(usrpol.items(), key=lambda k: k[1])[0],max(usrsub.items(), key=lambda k: k[1])[0],min(usrsub.items(), key=lambda k: k[1])[0]]
topusrtwts = []
for key, value in usrtweets.items():
    if key in topusrs:
        topusrtwts.append(value.encode('utf-8'))
        
print 'The user with the highest polarity is {0} with \"{1}\"\n'.format(topusrslst[0], topusrtwts[0])
print 'The user with the lowest polarity is {0} with \"{1}\"\n'.format(topusrslst[1], topusrtwts[1])
print 'The user with the highest subjectivity is {0} with \"{1}\"\n'.format(topusrslst[2], topusrtwts[2])
print 'The user with the lowest subjectivity is {0} with \"{1}\"\n'.format(topusrslst[3], topusrtwts[3])

#converting the list into string
d=''.join(data1).decode('utf-8')
#getting the words
words =d.lower().split()
#stopwords = nltk.corpus.stopwords.words('english')
#stopwords2= ['co','RT','rt','https','via','anti','says','...rt']
#stopwords.extend(stopwords2)
words2 = [w for w in words if w not in stopwords and len(w) > 1]
freq2 = nltk.FreqDist(words2)
freq2.plot(30)
words3=' '.join(words2)
wordcloud = WordCloud(max_font_size=40).generate(words3)

plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()




    
    