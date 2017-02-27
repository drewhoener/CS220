import json
import math

with open("tweets.json", "r") as tweet_db:
    tweets = json.load(tweet_db)


def flatten(xs):
    return list([val for a_list in xs for val in a_list])


def difference(xs, ys):
    dif = list(filter(lambda x: (x not in ys), xs))
    dif_left = list(filter(lambda x: (x not in xs), ys))
    return flatten([dif, dif_left])


def to_text(tweet_list):
    return list(map(lambda dic: dic["content"], tweet_list))


def to_lowercase(tweet_list):
    lower = lambda val: (val[0], val[1].lower() if val[0] == "content" else val[1])
    return list(map(lambda entry: dict(map(lower, entry.items())), tweet_list))


def nonempty(tweet_list):
    return list(filter(lambda entry: entry["content"] != "", tweet_list))


def total_word_count(tweet_list):
    return sum(list(map(lambda entry: len(entry["content"].split(" ")), nonempty(tweet_list))))


def hashtags(tweet):
    return list(filter(lambda val: val.startswith("#"), tweet["content"].split(" ")))


def mentions(tweet):
    return list(filter(lambda val: val.startswith("@"), tweet["content"].split(" ")))


def all_hashtags(tweet_list):
    return flatten(map(lambda entry: hashtags(entry), tweet_list))


def all_mentions(tweet_list):
    return flatten(map(lambda entry: mentions(entry), tweet_list))


def all_caps_tweets(tweet_list):
    return list(filter(lambda entry: entry["content"] == entry["content"].upper(), nonempty(tweet_list)))


def count_individual_words(tweet_list):
    words = flatten(list(map(lambda entry: entry["content"].split(' '), nonempty(tweet_list))))
    return dict(map(lambda val: (val, words.count(val)), words))


def count_individual_hashtags(tweet_list):
    words = flatten(list(map(lambda entry: hashtags(entry), nonempty(tweet_list))))
    return dict(map(lambda val: (val, words.count(val)), words))


def count_individual_mentions(tweet_list):
    words = flatten(list(map(lambda entry: mentions(entry), nonempty(tweet_list))))
    return dict(map(lambda val: (val, words.count(val)), words))


def n_most_common(n, word_count):
    return sorted(word_count.items(), lambda val: (val[1], val[0]), reverse=True)[0:n]


def iphone_tweets(tweet_list):
    return list(filter(lambda entry: entry["source"].find("iPhone") != -1, tweet_list))


def android_tweets(tweet_list):
    return list(filter(lambda entry: entry["source"].find("Android") != -1, tweet_list))


def average_favorites(tweet_list):
    return round(sum(map(lambda entry: entry["favorites"], tweet_list)) / len(tweet_list))


def average_retweets(tweet_list):
    return round(sum(map(lambda entry: entry["retweets"], tweet_list)) / len(tweet_list))


def sort_by_favorites(tweet_list):
    return sorted(tweet_list, key=lambda val: val["favorites"])


def sort_by_retweets(tweet_list):
    return sorted(tweet_list, key=lambda val: val["retweets"])


def upper_quartile(tweet_list):
    return tweet_list[int(math.floor(len(tweet_list) * 0.75))]


def lower_quartile(tweet_list):
    return tweet_list[int(math.floor(len(tweet_list) * 0.25))]


def top_quarter_by(tweet_list, factor):
    top_tweet = upper_quartile(tweet_list)
    return list(filter(lambda entry: entry[factor] >= top_tweet[factor], tweet_list))


def bottom_quarter_by(tweet_list, factor):
    bottom_tweet = lower_quartile(tweet_list)
    return list(filter(lambda entry: entry[factor] <= bottom_tweet[factor], tweet_list))
