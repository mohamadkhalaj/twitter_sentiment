import tweepy, logging, re
from confs import *
from textblob import TextBlob

logger = logging.getLogger()


class Twitter_streamer(tweepy.StreamListener):

    def __init__(self):
        super().__init__()
        self.api = self.create_api()
        self.me = self.api.me()
        self.file = open('twitter.txt', "a+")

    def create_api(self):

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

        api = tweepy.API(auth, wait_on_rate_limit=True,
                         wait_on_rate_limit_notify=True)

        try:
            api.verify_credentials()
        except Exception as e:
            logger.error("Error creating API", exc_info=True)
            raise e
        logger.info("API created")
        return api

    def clean_tweets(self, tweet):

        return ' '.join(re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\ / \ / \S+)", " ", tweet).split())

    def get_tweets(self, keywords):

        tweets = self.api.search(q = keywords, lang = 'en', count = 1000)

        for tweet in tweets:
            parsed_tweet = {'text': tweet.text, 'sentiment': self.get_tweet_sentiment(tweet.text)}
            if tweet.retweet_count > 0:
                if parsed_tweet not in self.tweets:
                    self.tweets.append(parsed_tweet)
            else:
                self.tweets.append(parsed_tweet)
            print(parsed_tweet['sentiment'])

        self.analyze()


    def on_error(self, status):
        logger.error(status)

def main(keywords):
    tweets_obj = Twitter_streamer()
    tweets_obj.get_tweets(keywords)

if __name__ == "__main__":
    main("")
