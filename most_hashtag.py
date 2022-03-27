import json
import re

def top_hashtag(tweetfile, x):
    hashtags = {}
    file = open(tweetfile, 'r')
    for line in file:
        try:
            tweet = json.loads(line)
        except:
            continue
        content = tweet['content']
        used = re.findall(r'(?i)\#\w+', content)
        for hashtag in used:
            if hashtag not in hashtags:
                hashtags[hashtag] = 1
            else:
                hashtags[hashtag] += 1
    # convert to list
    hashtags = dict(sorted(hashtags.items(), key=lambda item: item[1], reverse=True))
    top = list(hashtags.keys())[0:x]
    values = list(hashtags.values())[0:x]
    return top, values