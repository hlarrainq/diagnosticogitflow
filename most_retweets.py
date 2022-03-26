import json

def top_retweets(tweetfile, x):
    tweets = {}
    file = open(tweetfile, 'r')
    for line in file:
        try:
            tweet = json.loads(line)
        except:
            continue
        tweets[tweet['url']] = int(tweet['retweetCount'])
    # convert to list
    tweets = dict(sorted(tweets.items(), key=lambda item: item[1], reverse=True))
    top = list(tweets.keys())[0:x]
    return top