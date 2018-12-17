
import argparse
import configparser

from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import re
import jsonlines
from tqdm import tqdm

HASHTAG_REGEX = re.compile(r"#(\w+)")

class TwitterReader(object):
    def __init__(self, tweets_to_read, output_file, debug=False):
        self._tweets_to_read = tweets_to_read
        self._config = None
        self._output = output_file
        self._debug = debug
        self._read_config_file()

    def _read_config_file(self):
        self._config = configparser.ConfigParser()
        self._config.read('../config/config.properties')

    def read_tweets(self):
        auth = self._create_auth()
        api = tweepy.API(auth)

        user = api.me()

        with tqdm(total=self._tweets_to_read) as pbar:
            with jsonlines.open(self._output, 'w') as writer:
                for tweet in tweepy.Cursor(api.search,
                                           "*",
                                           lang="en").items(self._tweets_to_read):

                    hashtags = self._get_hashtags(tweet=tweet.text)

                    self._write_to_file(writer=writer,
                                        tweet_text=tweet.text,
                                        hashtags=hashtags)
                    pbar.update(1)

    def _write_to_file(self, writer, tweet_text, hashtags):
        data = {}
        data['text'] = tweet_text
        data['hashtags'] = hashtags
        writer.write(data)

        if self._debug:
            print(tweet_text)
            print(re.findall(r"#(\w+)", tweet_text))
            print(60 *'-' + '\n')

    def _get_hashtags(self, tweet):
        return re.findall(HASHTAG_REGEX, tweet)

    def _create_auth(self):
        auth = OAuthHandler(self._config['CONSUMER_API_KEYS']['consumer_key'],
                            self._config['CONSUMER_API_KEYS']['consumer_secret'])

        auth.set_access_token(self._config['ACCESS_TOKES']['access_token'],
                              self._config['ACCESS_TOKES']['access_token_secret'])
        return auth


def run(args):
    twitter_reader = TwitterReader(tweets_to_read=args.num_of_tweets,
                                   output_file=args.output,
                                   debug=args.debug)
    twitter_reader.read_tweets()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='parser')
    parser.add_argument('--num-of-tweets', help='Number tweets to read',
                        type=int, required=True)
    parser.add_argument('--output', help='File to write the Tweets to',
                        type=str, required=True)
    parser.add_argument('--debug', help='Prints debug information',
                        action="store_true")

    args = parser.parse_args()
    run(args)
