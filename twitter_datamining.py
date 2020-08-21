import tweepy, logging, re
from confs import *
import sys

logger = logging.getLogger()

class Twitter_streamer(tweepy.StreamListener):

    def __init__(self):
        super().__init__()
        self.api = self.create_api()
        self.me = self.api.me()
        self.file = open('twitter.txt', "a+", encoding='utf-8')
        self.counter = 0

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
        self.counter += 1
        return ' '.join(re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\ / \ / \S+)", " ", tweet).split())

    def stream(self,tweets_listener, keywords):
        stream = tweepy.Stream(self.api.auth, tweets_listener)
        stream.filter(track=keywords, languages=["en"])

    def on_status(self, tweet):
        print(f"{self.counter} tweet's collected.")
        text = {
            "text" : f"{self.clean_tweets(tweet.text)}"
        }
        self.file.write(str(text))
        self.file.write('\n')

    def on_error(self, status):
        self.file.close()
        logger.error(status)

def main(keywords):
    if len(keywords) == 0:
        print("Enter at least 1 keyword like:\npython twitter_datamining.py apple")
        exit()
    print(keywords)
    tweets_obj = Twitter_streamer()
    tweets_obj.stream(tweets_obj, keywords)

if __name__ == "__main__":
    main(sys.argv[1:])
