import nltk

def posTag(tweet):
    tweetWords = tweet.split()
    taggedTweet = nltk.pos_tag(tweetWords)
    return taggedTweet

"""
#pre-processing positive twits
neutralPreprocessedFilename = "../dataset/neutralProcessed.txt"
print "preprocessing neutral tweets"
f = open(neutralPreprocessedFilename,"r")
line=f.readline()
while line:
    posTag(line)
    line =f.readline()
"""
#posTag("I am a girl")


