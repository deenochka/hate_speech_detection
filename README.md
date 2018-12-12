# Hate Speech Detection

This project is part of the https://www.meetup.com/Data-for-Good-Israel/ and its scope to detect hate speeches on Twitter (especialy racism, harassment and homophobic speeches)

### Installation
HateSpeachDetector runs on python 3.5.2

**Get the code:**
```
$ git clone https://github.com/salexln/hate_speech_detection.git
```
**Install the dependencies:**
```
$ cd hate_speech_detection
$ pip3 -r src/requirements.txt  
```

**Configuration & Twitter API keys:**

In order to connect to Twitter API, you must sign-in for Twitter, and request develper account - https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html

Then you must get 4 keys:
* consumer_key
* consumer_secret_key
* access_token
* access_token_secret_key

When you have the keys, do the following:
```
$ cd hate_speech_detection
$ mkdir config
$ cd config
$ touch config.properties
```
Open config.properties in some text editor, and edit it in the follwoing way:
```
CONSUMER_API_KEYS]
consumer_key=your_consumer_key
consumer_secret=your_consumer_secret_key

[ACCESS_TOKES]
access_token=your_access_token
access_token_secret=your_access_token_secret_keys
```

### How to run:
**Getting Tweets:**
```
$ cd hate_speech_detection/src/
$ python3 twitter_reader.py --num-of-tweets 4
```
