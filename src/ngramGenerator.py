import nltk
import operator
# extract k most frequent words from the sorted list
def mostFreqList(l,k):
    m=[w[0] for w in l[0:k]]
    return m
#get all the words from sorted list
def getSortedWordCount(filename,gram):
    d = get_word_features(ngramText(filename,gram))
    l = sortList(d)
    print l
    return l
# from a list of words returns a dictionary with word, freq as key, value
def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    result=[]
    for k in wordlist.keys():
        result.append([k,wordlist[k]])
    return result
# generate vector of unigrams in text file
def ngramText(filename,gram):
    textWords=[]
    f=open(filename,"r")
    line=f.readline()
    while line:
        textWords.extend(ngram(line,gram))
        line=f.readline()
    f.close()
    print textWords
    return textWords

def ngram(text,grams):
    text = text.split(" ")
    model=[]
    count=0
    for token in text[:len(text)-grams+1]:
       model.append(tuple(text[count:count+grams]))
       count=count+1
    return model

def sortList(x):
    return list(reversed(sorted(x, key=operator.itemgetter(1))))

positivePreprocessed = "../dataset/positiveProcessed.txt"
negativePreprocessed = "../dataset/positiveProcessed.txt"
neutralPreprocessed = "../dataset/positiveProcessed.txt"

getSortedWordCount(positivePreprocessed,1)
#getSortedWordCount(positivePreprocessed,2)
#getSortedWordCount(positivePreprocessed,3)
