import tweepy, time


CONSUMER_KEY = 'ZVOiKcVTOlWIZT81yq1JQ'
CONSUMER_SECRET = '2RkDz6ZkwgUUfTYBPCAK9HmhMzKLCRB2Ot54GaRz34'
ACCESS_TOKEN = '1423605462-X6XBRejy5PK2kkWpxF4aiIuzwzexDhSq8Jyx9H6'
ACCESS_TOKEN_SECRET = 'SRuIGvgT4OLchsDrqB9af4PjBf6HGswH1BJfJ1sgCMLVI'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def followers(screen_name):

    print(screen_name)
    followers_and_counts = {}

    for follower in tweepy.Cursor(api.followers, screen_name=screen_name).items(5):
        followers_and_counts[follower.screen_name] = follower.followers_count
        try:
            api.create_friendship(follower.id)
        except:
            continue

    return followers_and_counts


def retweet(screen_name):

    last_tweet = api.user_timeline(screen_name = screen_name, count = 1)[0]
    api.retweet(last_tweet.id)


def tweetit(tweet_body):

    api.update_status(tweet_body)


