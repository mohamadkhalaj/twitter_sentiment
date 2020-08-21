from textblob import TextBlob

class Sentiment_twiiter:
    def __init__(self):
        self.tfile = open('twitter.txt', 'r', encoding='utf-8')

    def analyze(self):

        positives = 0
        negatives = 0
        neutral = 0
        all = 0

        for tweet in self.tweets:
            if tweet['sentiment'] == 'positive':
                positives += 1
            elif tweet['sentiment'] == 'negative':
                negatives += 1
            else:
                neutral += 1
            all += 1

        print("positives: ", positives * 100 / all)
        print("negatives: ", negatives * 100 / all)
        print("neutral: ", neutral * 100 / all)

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


    def get_tweet_sentiment(self, tweet):

        analysis = TextBlob(self.clean_tweets(tweet))
        if analysis.sentiment.polarity > 0:
            return 'positive'

        elif analysis.sentiment.polarity == 0:
            return 'neutral'

        else:
            return 'negative'
