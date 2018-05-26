import csv
import tweepy
from textblob import TextBlob


consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

with open('sentiments.csv', 'w') as csvfile:
	filewriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
	for tweet in public_tweets:
		sentiment = TextBlob(tweet.text).sentiment
		if sentiment.polarity > 0.0:
			polarity='positive'
		else:
			polarity='negative'

		filewriter.writerow([tweet.text, sentiment, polarity])


