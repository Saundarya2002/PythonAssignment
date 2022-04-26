import tweepy
import re
import pandas as pd
import matplotlib.pyplot as plt


def find_hashtags(tweet):
    return re.findall('(#[A-Za-z]+[A-Za-z0-9-_]+)', tweet)


consumer_key = 'SG0nzGdH1N2Kx1Nf72uSPjwrn'
consumer_secret = "mEW0vTDXMW8mBN6EoQyiywF6gCl08Lixq8yQ7saPWBOa9HjSr7"
access_token = '1515915987266473984-lANcv1p9iJFfcgCEiMOjaHXPOVFlBX'
access_secret = 'FOI33dQXZIuX4Ib5oYvrqEixfYtSN2Ms3XtdEBJPxf7FP'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
per_tweets = tweepy.Cursor(api.search, q=" elonmusk -filter:retweets", lang="en", show_user=True,
                           tweet_mode="extended").items(50)
per_tweets_list = [[tweet.created_at, tweet.place, tweet.user.name, tweet.full_text] for tweet in per_tweets]
print(len(per_tweets_list))
tweets_df = pd.DataFrame(per_tweets_list)

tweets_df.columns = ['Created at', 'Place', 'User', 'Text']

tweets_df.to_csv("per_tweets.csv", index=False)

tweets_df = pd.read_csv("per_tweets.csv", index_col=0)
tweets_df['hashtags'] = tweets_df.Text.apply(find_hashtags)
hashtag_list = tweets_df['hashtags'].to_list()
flat_hashtags_df = pd.DataFrame([item for sublist in hashtag_list for item in sublist])
flat_hashtags_df.shape

flat_hashtags_df.columns = ['hashtags']
flat_hashtags_df.head()
print("Total hashtags: ", len(flat_hashtags_df['hashtags']))
print("Repeated hashtags: ", len(flat_hashtags_df['hashtags'].unique()))
flat_hashtags_df['hashtags'].value_counts()[:10].plot(kind='barh')