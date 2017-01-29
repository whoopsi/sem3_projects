# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 19:21:31 2016

@authors: gupta, mdavila, Dr. Gene Moo Lee
"""
from __future__ import division
import json
import os
from sklearn import decomposition
import numpy as np  # a conventional alias
from sklearn.feature_extraction.text import TfidfVectorizer



path= '/Users/gupta/Downloads/data science/PJ1/data/'
tweets=[]
for fname in os.listdir(path):
    #print fname
    if not fname.startswith('.') and os.path.isfile(os.path.join(path, fname)):
        with open(path + fname,'r') as a:
            content= json.load(a)
            for i in range(0,len(content)):
                tweets.append(content[i]['text'])

vectorizer = TfidfVectorizer(stop_words='english', min_df=2)
dtm = vectorizer.fit_transform(tweets)
#print dtm.shape
vocab = vectorizer.get_feature_names() # list of unique vocab, we will use this later
#print len(vocab), '# of unique words'
#print vocab[-10:]
#print vocab[:10]

#print 'num of documents, num of unique words'
#print (dtm.shape)

num_topics = 20

clf = decomposition.NMF(n_components=num_topics, random_state=1)
doctopic = clf.fit_transform(dtm)
print (num_topics, clf.reconstruction_err_)

topic_words = []
num_top_words = 5
for topic in clf.components_:
    #print topic.shape, topic[:5]
    word_idx = np.argsort(topic)[::-1][0:num_top_words] # get indexes with highest weights
    #print 'top indexes', word_idx
    topic_words.append([vocab[i] for i in word_idx])
    #print topic_words[-1]
    #print        
for t in range(len(topic_words)):
    print "Topic {}: {}".format(t, ' '.join(topic_words[t][:15]))

print dtm.shape

for n in range(1, 10):    
    num_topics = 5*n
    num_top_words = 10
    clf = decomposition.NMF(n_components=num_topics, random_state=1)
    doctopic = clf.fit_transform(dtm)
    print num_topics, clf.reconstruction_err_
