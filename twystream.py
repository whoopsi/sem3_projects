# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 13:11:57 2016

@author: Project Team 8 Michael Davila, Anish Gupta
"""
from twython import TwythonStreamer
import sys
import json
import time
tweets = []
class MyStreamer(TwythonStreamer):
 
    # overriding
    def on_success(self, data):
        
        
        try:
            if data['lang'] == 'en':
                tweets.append(data)
                print 'received tweet #', len(tweets)
                
        except:
            print('Tweet lang key missing')

        if len(tweets) == 1000:
            self.store_json()           
            self.disconnect()
        if len(tweets) == 700:
            self.disconnect()
        if len(tweets) == 500:
            self.disconnect()        
        if len(tweets) == 200:
            self.disconnect()             

    # overriding
    def on_error(self, status_code, data):
        print status_code, data
        self.disconnect()

    def store_json(self):
        with open(r'tweet_stream_{0}_{1}_{2}.json'.format(keyword, len(tweets), time.strftime("%Y%m%d-%H%M%S")), 'w') as f:
            json.dump(tweets, f, indent=4)
            
if __name__ == '__main__':
    with open('mtc.json', 'r') as f:
        
        credentials = json.load(f)
#        for i in range(0,9):            
        CONSUMER_KEY = credentials['CONSUMER_KEY']
        CONSUMER_SECRET = credentials['CONSUMER_SECRET']
        ACCESS_TOKEN = credentials['ACCESS_TOKEN']
        ACCESS_TOKEN_SECRET = credentials['ACCESS_TOKEN_SECRET']
        
        stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        
        if len(sys.argv) >1:
            keyword = sys.argv[1]
        else:
            keyword = 'Obama'
     
        stream.statuses.filter(track=keyword)
        time.sleep(30)
        stream.statuses.filter(track=keyword)
        time.sleep(30)
        stream.statuses.filter(track=keyword)
        time.sleep(30)           
        stream.statuses.filter(track=keyword)
    
    #        easygui.msgbox("TweetStream Done", title="Finished")
    
            

            
