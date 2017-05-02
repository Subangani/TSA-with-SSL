from __future__ import division

def uppercasedWordsInTweet(tweet):
    count=0
    if(len(tweet) != 0):
        for w in tweet.split():
            if w.isupper():
                count =count+1;
    return count

def punctuationCount(tweet):
    exclamation = tweet.count("!");
    question = tweet.count("?")
    return tuple(exclamation,question);


def capitalCountInAWord(tweet):
    count=0
    if (len(tweet) != 0):
        for c in tweet:
            if (str(c).isupper()):
                count=count+1
    return count


tweet="Hi there i am PLAYING Clash of Clans"
print capitalCountInAWord(tweet);
print punctuationCount(tweet);

