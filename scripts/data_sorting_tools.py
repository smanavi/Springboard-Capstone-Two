import os
import json
import pandas as pd
from . import twitter_api_access

api = twitter_api_access.access_api()

def json_to_df(file, keys, get_media=True, return_dict=False):
    """creates dataframe from tweets based on which tweet keys you want.
    output dict is keyed on tweet ID"""
    with open(file, 'r') as f:
        doc = json.load(f)
    try:
        del doc['query']
    except:
        pass

    main_dict = {}
    for mainkey in doc.keys():
        temp = {}
        for k in keys:
            if type(k) is tuple:
                key = "{}_{}".format(k[0], k[1])
                temp[key] = doc[mainkey][k[0]][k[1]]
            # elif ("text" in k)==True:
            #     try:
            #         temp[k] = doc[mainkey]["full_text"]
            #     except:
            #         temp[k] = doc[mainkey][k]
            else:
                temp[k] = doc[mainkey][k]
            # try:
            #     temp[k] = doc[mainkey]["full_text"]
            # except:
            #     pass

        tid = doc[mainkey]['id']
        main_dict[tid] = temp

    df = pd.DataFrame(main_dict).T
    if get_media==True:
        media_df = get_media_info(doc)
        df = pd.concat([df, media_df], axis=1)
        df['media_count'] = df['media_count'].fillna(0)
        df['media_types'] = df['media_types'].fillna('none')

    if return_dict == True:
        return df, main_dict
    else:
        return df

def get_media_info(tweets_json):

    media_dict = {}
    for key in tweets_json.keys():
        temp = {}
        if "extended_entities" in tweets_json[key].keys():
            dk = tweets_json[key]['id']
            temp['media_count'] = len(tweets_json[key]['extended_entities']['media'])
            temp['media_types'] = tweets_json[key]['extended_entities']['media'][0]['type']
            # [t['type'] for t in tweets_json[key]['extended_entities']['media']]
            media_dict[dk] = temp
    media_df = pd.DataFrame(media_dict).T
    return media_df

def fix_truncated_tweets(tweets_json):
    """part of code from tweepy extended_tweets documentation"""

    tweet_dict = tweets_json
    for key in tweets_json.keys():
        if ('query' in key)==False:
            if tweets_json[key]['truncated'] == True:
                tid = tweets_json[key]['id']
                try:
                    status = api.get_status(tid, tweet_mode="extended")
                    try:
                        full_text = status.retweeted_status.full_text
                    except AttributeError:
                        full_text = status.full_text
                    tweet_dict[key]['full_text']=full_text
                except:
                    pass
            else:
                try:
                    full_text = tweets_json[key]['retweeted_status']['extended_tweet']['full_text']
                    tweet_dict[key]['full_text']=full_text
                except KeyError:
                    pass

    return tweet_dict
