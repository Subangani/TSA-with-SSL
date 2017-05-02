from __future__ import division
import re

def loadWords(filename):
    f=open(filename,'r')
    words={}
    line=f.readline();
    lines=line.split(",");
    return lines

def getScore(tweet,posW,negW):
    score=0;
    for w in tweet.split():
        if w in posW:
		score+=1;
	if w in negW:
		score-=1;
	if w.endswith("_NEG"):
		if len(w) > 4:
			if(w[0:len(w)-5]) in posW:
				score -=1;
			if(w[0:len(w)-5]) in negW:
				score +=1;
    return score;
	
tweet="hi there i am worse_NEG whatsapp";
pos=loadWords("../resource/positive.txt");
neg=loadWords("../resource/negative.txt");
print getScore(tweet,pos,neg);
