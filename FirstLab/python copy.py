import os
tweetsPath = "./tweets.txt"
score=0
rank = {}
tweetsFile= open(tweetsPath,"r")
tweets=tweetsFile.read().split("\n")
for i in tweets:
    if i=="":
        tweets.remove('')
        
#print(tweets)
tweetsFile.close
wordsNegativePath = "./words_negative.txt"
negative= open(wordsNegativePath)
wordsPositivePath ="./words_positive.txt"
positive= open(wordsPositivePath)
positive=positive.read().split("\n")
for i in positive:
    if i=="":
        positive.remove('')
#print(positive)
negative=negative.read().split("\n")
for i in negative:
    if i=="":
        negative.remove('')
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
for value,key in rankedByScore:
   # final.append(value)
   ranks+=1
   final+=str(ranks)+" "+value+"\n"
print(final)