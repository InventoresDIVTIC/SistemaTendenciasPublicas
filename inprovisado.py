
import pandas as pd
import numpy as np

data=pd.read_csv('entrenamiento/IMDB Dataset SPANISH.csv')

x=np.asanyarray(data.drop(columns=['Index','review_en','sentiment']))
print(x)

"""from bs4 import BeautifulSoup
import requests
import sys
import json


def usage():
    msg = 
    Please use the below command to use the script.
    python script_name.py twitter_username
    
    print(msg)
    sys.exit(1)

def get_tweet_text(tweet):
    tweet_text_box = tweet.find("p", {"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})
    if tweet_text_box:
        images_in_tweet_tag = tweet_text_box.find_all("a", {"class": "twitter-timeline-link u-hidden"})
        tweet_text = tweet_text_box.text
        for image_in_tweet_tag in images_in_tweet_tag:
            tweet_text = tweet_text.replace(image_in_tweet_tag.text, '')
        return tweet_text.strip()
    return None

def get_this_page_tweets(soup):
    tweets_list = list()
    tweets = soup.find_all("li", {"data-item-type": "tweet"})
    for tweet in tweets:
        tweet_data = get_tweet_text(tweet)
        if tweet_data:
            tweets_list.append(tweet_data)
            print(".", end="")
            sys.stdout.flush()
    return tweets_list

import twint

def get_tweets_data(username):
    c = twint.Config()
    c.Username = username
    c.Store_object = True
    c.Limit = 10  # Set the limit to the number of tweets you want
    twint.run.Search(c)
    tweets_list = [tweet.tweet for tweet in twint.output.tweets]
    return tweets_list


def dump_data(username, tweets):
    filename = username + "_twitter.json"
    print("\nDumping data in file " + filename)
    data = dict()
    data["tweets"] = tweets
    with open(filename, 'w') as fh:
        json.dump(data, fh)
    return filename

def get_username():
    # if username is not passed
    if len(sys.argv) < 2:
        usage()
    username = sys.argv[1].strip().lower()
    if not username:
        usage()
    return username

def start(username=None):
    username = get_username()
    url = "http://www.twitter.com/" + username
    print("\n\nDownloading tweets for " + username)
    response = None
    try:
        response = requests.get(url)
    except Exception as e:
        print(repr(e))
        sys.exit(1)

    if response.status_code != 200:
        print("Non-success status code returned " + str(response.status_code))
        sys.exit(1)

    soup = BeautifulSoup(response.text, 'html.parser')

    if soup.find("div", {"class": "errorpage-topbar"}):
        print("\n\n Error: Invalid username.")
        sys.exit(1)

    tweets = get_tweets_data(username, soup)
    # dump data in a text file
    dump_data(username, tweets)
    print(str(len(tweets)) + " tweets dumped.")

start()


"""
