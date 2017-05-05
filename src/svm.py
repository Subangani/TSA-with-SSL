import  ngramGenerator

neutralPreprocessedFilename = "../dataset/positiveProcessed.txt"
print "preprocessing neutral tweets"
f = open(neutralPreprocessedFilename,"r")
line=f.readline()
while line:
    print ngramGenerator.getSortedWordCount(neutralPreprocessedFilename,1)
    line =f.readline()