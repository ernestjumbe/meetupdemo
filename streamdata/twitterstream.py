import re
from meetupdemo import settings
from twitter import *
from swampdragon.pubsub_providers.data_publisher import publish_data

r = re.compile(r"(http://[^ ]+)")

ckey = settings.TWITTER_CONSUMER_KEY
csecret = settings.TWITTER_CONSUMER_SECRET
atoken = settings.TWITTER_ACCESS_TOKEN
asecret = settings.TWITTER_ACCESS_TOKEN_SECRET

auth = OAuth(
    consumer_key=ckey,
    consumer_secret=csecret,
    token=atoken,
    token_secret=asecret
)
twitter_stream = TwitterStream(auth=auth, domain='stream.twitter.com')
# Put your search term in the tack variable
iterator = twitter_stream.statuses.filter(track='#django')

def get_tweets():


	for tweet in iterator:
		text = tweet.get('text')
		text = r.sub(r'<a href="\1" target="_blank">\1</a>', text)
		if not text:
			continue
		publish_data(channel='tweet', data={'text': text})

