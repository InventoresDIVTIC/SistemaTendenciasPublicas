import csv
import snscrape.modules.twitter as sntwitter
import pandas as pd 
from time import sleep 
from tqdm import tqdm

#colect data in general https://www.youtube.com/watch?v=QLIYJoRvd-M


tweet_data =[]

username=input('enter what do you want to searcg')
number=10000

for i, tweets in enumerate (sntwitter.TwitterTweetScraper({}))