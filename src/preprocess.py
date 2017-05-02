import re
import csv
#start getStopWordList
def loadStopWordList():
    fp =  open("../resource/stopWords.txt",'r')
    #read the stopwords file and build a list
    stopWords = []
    stopWords.append('at_user')
    stopWords.append('url')
    line = fp.readline()
    while line:
        word = line.strip()
        stopWords.append(word)
        line = fp.readline()
    fp.close()
    return stopWords

def removeStopWords(tweet,stopWords):
    result=''
    for w in tweet:
        if w in stopWords:
            None
        else:
            result=result+w+' '
    return result



#start loading slangs list from file
def loadInternetSlangsList():
    fi=open('../resource/internetSlangs.txt','r')
    slangs={}

    line=fi.readline()
    while line:
        l=line.split(r',%,')
        if len(l) == 2:
            slangs[l[0]]=l[1][:-2]
        line=fi.readline()
    fi.close()
    return slangs

#start replace slangs
def replaceSlangs(tweet,slangsList):
    result=''
    words=tweet.split()
    for w in words:
        if w in slangsList.keys():
            result=result+slangsList[w]+" "
        else:
            result=result+w+" "
    return result

#start replaceTwoOrMore
def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)
#end

#start process_tweet
def preProcessTweet(tweet): # arg tweet, stopWords list and internet slangs dictionnary
    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','url',tweet)
    tweet = re.sub('((www\.[^\s]+)|(http?://[^\s]+))','url',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','at_user',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    tweet = tweet.strip('\'"') # removing sepcial caracter
    processedTweet=replaceTwoOrMore(tweet) # replace multi-occurences by two
    slangs = loadInternetSlangsList()
    words=replaceSlangs(processedTweet,slangs).split()
    stopWords = loadStopWordList()
    preprocessedtweet = removeStopWords(words,stopWords)
    return preprocessedtweet
#end

def process(filename, preprocessedFilename):
    f0=open(filename,"r")
    f1 = open(preprocessedFilename,"w")
    reader = csv.reader(f0)
    for row in reader:
        a = row[2]
        tweet= preProcessTweet(a)
        f1.write(tweet + '\n')
    f0.close()
    f1.close()

#pre-processing positive twits
positiveFilename= "../dataset/positive.csv"
positivePreprocessedFilename = "../dataset/positiveProcessed.txt"
print "preprocessing positive tweets"
process(positiveFilename,positivePreprocessedFilename)

#pre-processing negative twits
negativeFilename= "../dataset/negative.csv"
negativePreprocessedFilename = "../dataset/negativeProcessed.txt"
print "processing negative twits"
process(negativeFilename,negativePreprocessedFilename)

#pre-processing positive twits
neutralFilename= "../dataset/neutral.csv"
neutralPreprocessedFilename = "../dataset/neutralProcessed.txt"
print "preprocessing neutral tweets"
process(neutralFilename,neutralPreprocessedFilename)



