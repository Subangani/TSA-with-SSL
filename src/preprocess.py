import re
import csv
import postag
import ngramGenerator
import nltk
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

def negate(tweetWordList):
    fn =open("../resource/negation.txt",'r')
    line = fn.readline()
    negationList=[]
    while line:
        negationList.append(line[:-1]);
        line = fn.readline()
    fn.close();
    puncuationMarks = [".", ":", ";", "!", "?"]

    for i in range(len(tweetWordList)):
        if tweetWordList[i] in negationList:
            j = i + 1
            while j < len(tweetWordList):
                if (tweetWordList[j][-1] not in puncuationMarks):
                    tweetWordList[j] = tweetWordList[j] + "_NEG"
                    j = j + 1
                elif(tweetWordList[j][-1] in puncuationMarks):
                    tweetWordList[j] = tweetWordList[j][:-1] + "_NEG"
                    break;
            i = j
        return tweetWordList


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
    negatedTweets=negate(words)
    stopWords = loadStopWordList()
    preprocessedtweet = removeStopWords(negatedTweets,stopWords)
   # print preprocessedtweet
    postaggedTweet = postag.posTag(preprocessedtweet)
    #print postaggedTweet
    return postaggedTweet

#end

def process(filename, positiveUnigram,positiveBigram,positiveTrigram):
    f0=open(filename,"r")
    f1 = open(positiveUnigram,"w")
    f2 = open(positiveBigram, "w")
    f3 = open(positiveTrigram, "w")
    reader = csv.reader(f0)
    for row in reader:
        a = row[2]
        tweet= preProcessTweet(a)
        tweetUnigram = ngramGenerator.getSortedWordCount(tweet,1)
        for i in range(len(tweetUnigram)):
            f1.write(''.join('%s ' %  tweetUnigram[i][0]) +"\n")
        tweetBigram = ngramGenerator.getSortedWordCount(tweet,2)
        for i in range(len(tweetBigram)):
            f2.write(''.join('%s ' % str(tweetBigram[i][0]))+ "\n")
        tweetTrigram = ngramGenerator.getSortedWordCount(tweet,3)
        for i in range(len(tweetTrigram)):
            f3.write(''.join('%s ' %  str(tweetTrigram[i][0])) +"\n")

    f0.close()
    f1.close()

    f2.close()
    f3.close()

#pre-processing positive twits
positiveFilename= "../dataset/positive.csv"
positiveUnigramfile = "../dataset/positiveUnigram.txt"
positiveBigramfile = "../dataset/positiveBigram.txt"
positiveTrigramfile = "../dataset/positiveTrigram.txt"
print "preprocessing positive tweets"
process(positiveFilename,positiveUnigramfile,positiveBigramfile,positiveTrigramfile)



"""
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
"""

