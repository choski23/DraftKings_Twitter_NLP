from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import datetime

class TweetMiner(object):

    result_limit    =   1
    data            =   []
    api             =   False

    twitter_keys = {
        'consumer_key':        'Y6mRvbhFaZinGb3HMbaekWLk9',
        'consumer_secret':     'R1IWmvvddzAwoJsB3iBogjm8dbncGfiPep5T56D05tZPfUUwBa',
        'access_token_key':    '2888838179-DPfnSZyVwbzIDoXOYOeFfsnA83ySwM2ApgRIHtA',
        'access_token_secret': 'jIw68X4pGlSV3cb58urKrL8mm7EobdtBf9d6XE6XS5MEg'
    }

    def __init__(self, keys_dict=twitter_keys, api=api, result_limit = result_limit):

        self.twitter_keys = keys_dict

        auth = OAuthHandler(keys_dict['consumer_key'], keys_dict['consumer_secret'])
        auth.set_access_token(keys_dict['access_token_key'], keys_dict['access_token_secret'])

        self.api = API(auth)

        self.result_limit = result_limit


    def mine_user_tweets(self, user="lindamcho1123",
                         mine_rewteets=False,
                         max_pages=5):

        data           =  []
        last_tweet_id  =  False
        page           =  1

        while page <= max_pages:
            if last_tweet_id:
                statuses   =   self.api.user_timeline(screen_name=user,
                                                     count=self.result_limit,
                                                     max_id=last_tweet_id - 1,
                                                     tweet_mode = 'extended',
                                                     include_retweets=True
                                                    )
            else:
                statuses   =   self.api.user_timeline(screen_name=user,
                                                        count=self.result_limit,
                                                        tweet_mode = 'extended',
                                                        include_retweets=True)

            for item in statuses:

                mined = {
                    'tweet_id':        item.id,
                    'name':            item.user.name,
                    'screen_name':     item.user.screen_name,
                    'retweet_count':   item.retweet_count,
                    'text':            item.full_text,
                    'mined_at':        datetime.datetime.now(),
                    'created_at':      item.created_at,
                    'favourite_count': item.favorite_count,
                    'hashtags':        item.entities['hashtags'],
                    'status_count':    item.user.statuses_count,
                    'location':        item.user.location,
                    'source_device':   item.source
                }

                try:
                    mined['retweet_text'] = item.retweeted_status.full_text
                except:
                    mined['retweet_text'] = 'None'
                try:
                    mined['quote_text'] = item.quoted_status.full_text
                    mined['quote_screen_name'] = status.quoted_status.user.screen_name
                except:
                    mined['quote_text'] = 'None'
                    mined['quote_screen_name'] = 'None'

                last_tweet_id = item.id
                data.append(mined)

            page += 1

        return data