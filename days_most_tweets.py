import json

def top_retweets(tweetfile, x):
    dates = {}
    file = open(tweetfile, 'r')
    for line in file:
        try:
            tweet = json.loads(line)
        except:
            continue
        date = tweet['date'][0:10]
        if date not in dates.keys():
            dates[date] = 1
        else:
            dates[date] += 1
    # convert to list
    dates = dict(sorted(dates.items(), key=lambda item: item[1], reverse=True))
    top = list(dates.keys())[0:x]
    return top