# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 19:21:31 2016

@authors: gupta, mdavila, Dr. Gene Moo Lee
"""
from __future__ import division, print_function
import json
import os
from gensim import corpora, models
import logging

logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logging.root.level = logging.INFO

path= '/Users/gupta/Downloads/data science/PJ1/data/'
names = []
docs = []
tweets= []
tweetwords = []
for fname in os.listdir(path):
    if not fname.startswith('.') and os.path.isfile(os.path.join(path, fname)):
        with open(path + fname,'r') as a:
            content= json.load(a)
            for i in range(0,len(content)):
                tweets.append(content[i]['text'])
for item in tweets:
    tweetwords.append(item.split())
    
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logging.root.level = logging.INFO

dic = corpora.Dictionary(tweetwords)

corpus = [dic.doc2bow(text) for text in tweetwords]
#print(type(corpus), len(corpus))
#for corp in corpus:
#    print(len(corp), corp[:10])
    
tfidf = models.TfidfModel(corpus)
#print(type(tfidf))
corpus_tfidf = tfidf[corpus]
#print(type(corpus_tfidf))

NUM_TOPICS = 20
model = models.ldamodel.LdaModel(corpus_tfidf, 
                                 num_topics=NUM_TOPICS, 
                                 id2word=dic, 
                                 update_every=1, 
                                 passes=1)
print("LDA model")
topics_found = model.print_topics(20)
counter = 1
for t in topics_found:
    print("Topic #{} {}".format(counter, t))
    counter += 1
NUM_TOPICS = 10
model = models.lsimodel.LsiModel(corpus_tfidf,
                                 id2word=dic,
                                 num_topics=NUM_TOPICS
                                )
model.print_topics()   