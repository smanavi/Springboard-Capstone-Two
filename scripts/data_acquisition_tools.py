import os
import tweepy
import json
from datetime import datetime, timedelta, timezone
# from . import twitter_api_access
#
# api = twitter_api_access.access_api()

def test_sys_things():
    import sys
    print(sys.path)

def api_search(query, filename, todate=None, n_items=500, return_dict=False):
    '''searches and saves a json of search results for a particular query using the standard twitter api search.
    params:
        query: string containing your search query
        filename: full path of to-be-written json
        todate: return tweets before the date, must be in YYYY-MM-DD format
        n_items: int, max number of tweets to return, default 500
        return_dict: bool, whether to return the dictionary item created
    returns:
        dictionary item if return_dict set to True

    '''

    cursor = tweepy.Cursor(api.search, q=query, until=todate, tweet_mode='extended').items(n_items)

    tweets = {}
    for n,t in enumerate(cursor):
        tweets[n] = t._json
    tweets['query'] = query

    with open(filename, 'w') as j:
        json.dump(tweets, j, indent=4)
    j.close()

    if return_dict==True:
        return tweets

def api_advanced_search(query, filename, which_api, todate=None, fromdate=None, n_items=500, return_dict=False):
    '''searches and saves a json of search results for a particular query using either the 30 day or full archive api.
    params:
        query: string containing your search query. char limit is 128 for full archive, 256 for 30day
        filename: full path of to-be-written json
        which_api: either "30day" or "full"
        n_items: int, max number of tweets to return, default 500
        return_dict: bool, whether to return the dictionary item created
    returns:
        dictionary item if return_dict set to True

    '''
    if which_api == "30day":
        API = api.search_30_day
        env = '30day'
    elif which_api == "full":
        API = api.search_full_archive
        env = 'full'

    cursor = tweepy.Cursor(API,
                           environment_name= env,
                           toDate = todate,
                           fromDate = fromdate,
                           query=query,
                           # tweet_mode = "extended",
                          wait_on_rate_limit=True,
                          wait_on_rate_limit_notify=True).items(n_items)

    tweets = {}
    for n,t in enumerate(cursor):
        tweets[n] = t._json
    tweets['query'] = query

    with open(filename, 'w') as j:
        json.dump(tweets, j, indent=4)
    j.close()

    if return_dict==True:
        return tweets


def timestamp_to_toDate(timestamp):
    """takes a timestamp from twitter created_at object and returns a datetime object and str formatted
    for tweepy date searches."""

    frm = "%a %b %d %H:%M:%S %z %Y"
    to = "%Y%m%d%H%M"
    toDate_dt = datetime.strptime(timestamp, frm)
    toDate_str = toDate_dt.strftime(to)
    return toDate_dt, toDate_str


def access_api():
    """This is here to illustrate the way I access the twitter API, but the function with my access
    Access_token = ""
    Access_token_secret = ""
    Bearer_token = ""
    Consumer_key = ""
    Consumer_key_secret = ""
    keys is stored elsewhere."""

    auth = tweepy.OAuthHandler(Consumer_key, Consumer_key_secret)
    auth.set_access_token(Access_token, Access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    return api
