import os

score=0
rank = {}
def removeWhitespace(filePath):
    
    file= open(filePath,"r")
    list=file.read().split("\n")
    for i in list:
        if i=="":
            list.remove('')
    return list
tweetsPath = "./tweets.txt"
tweets= removeWhitespace(tweetsPath)
print(tweets)

wordsNegativePath = "./words_negative.txt"
negative= removeWhitespace(wordsNegativePath)
wordsPositivePath ="./words_positive.txt"
positive= removeWhitespace(wordsPositivePath)
#print(positive)
#print(negative)
for tweet in tweets:
        for char in tweet:
            if char ==".":
               tweet= tweet.replace(".","") 
        currentscore=0
        for word in tweet.split(" "):
             if word in negative:
                currentscore-=1
             if word in positive:
                 currentscore+=1
        rank[tweet]=currentscore

rankedByScore=sorted(rank.items(), key=lambda x:x[1], reverse=True)  
final=""
ranks=0
for key,value in rankedByScore:
   # to display in a list rather than a string remove the bellow two lines and add this command:  final.append(value)
   ranks+=1
   final+=str(ranks)+"- ("+str(key)+") with a score of: "+str(value) +"\n"
print(final)