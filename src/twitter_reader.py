
import argparse
import configparser

from tweepy import OAuthHandler
from tweepy import Stream
import tweepy

class TwitterReader(object):
    def __init__(self, tweets_to_read):
        self._tweets_to_read = tweets_to_read
        self._config = None
        self._read_config_file()

    def _read_config_file(self):
        self._config = configparser.ConfigParser()
        self._config.read('../config/config.properties')

    def read_tweets(self):
        auth = self._create_auth()
        api = tweepy.API(auth)

        user = api.me()

        for tweet in tweepy.Cursor(api.search, "*", lang="en").items(self._tweets_to_read):
            print(tweet.text)
            print('\n-------------------------------------------------------\n')

    def _create_auth(self):
        auth = OAuthHandler(self._config['CONSUMER_API_KEYS']['consumer_key'],
                            self._config['CONSUMER_API_KEYS']['consumer_secret'])

        auth.set_access_token(self._config['ACCESS_TOKES']['access_token'],
                              self._config['ACCESS_TOKES']['access_token_secret'])
        return auth


def run(args):
    twitter_reader = TwitterReader(tweets_to_read=args.num_of_tweets)
    twitter_reader.read_tweets()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='parser')
    parser.add_argument('--num-of-tweets', help='Number tweets to read',
                        type=int, required=True)

    args = parser.parse_args()
    run(args)
