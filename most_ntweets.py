import json

def top_user_ntweets(tweetfile, x):
    users = {}
    file = open(tweetfile, 'r')
    for line in file:
        try:
            tweet = json.loads(line)
        except:
            continue
        user = tweet['user']['username']
        if user not in users.keys():
            users[user] = 1
        else:
            users[user] += 1
    # convert to list
    users = dict(sorted(users.items(), key=lambda item: item[1], reverse=True))
    top = list(users.keys())[0:x]
    values = list(users.values())[0:x]
    return top, values
