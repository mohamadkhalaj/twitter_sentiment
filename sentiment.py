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

    def get_tweet_sentiment(self, tweet):

        analysis = TextBlob(self.clean_tweets(tweet))
        if analysis.sentiment.polarity > 0:
            return 'positive'

        elif analysis.sentiment.polarity == 0:
            return 'neutral'

        else:
            return 'negative'
