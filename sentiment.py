from textblob import TextBlob
import json

class Sentiment_twiiter:
    def __init__(self):
        self.tfile = open('twitter.txt', 'r', encoding='utf-8')
        self.tweets = [json.loads(line.strip().replace("'",'"')) for line in self.tfile.readlines()]
        self.tweets_sentimanted = []

    def analyze(self):

        self.get_tweet_sentiment()
        positives = 0
        negatives = 0
        neutral = 0
        all = 0

        for tweet in self.tweets_sentimanted:
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

    def get_tweet_sentiment(self):

        for tw in self.tweets:
            analysis = TextBlob(tw['text'])
            if analysis.sentiment.polarity > 0:
                self.tweets_sentimanted.append(
                    {
                        'text' : tw['text'],
                        'sentiment' : 'positive'
                    }
                )

            elif analysis.sentiment.polarity == 0:
                self.tweets_sentimanted.append(
                    {
                        'text': tw['text'],
                        'sentiment': 'neutral'
                    }
                )

            else:
                self.tweets_sentimanted.append(
                    {
                        'text': tw['text'],
                        'sentiment': 'negative'
                    }
                )

ob = Sentiment_twiiter()
ob.analyze()
