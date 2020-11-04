from textblob import TextBlob
import sys,tweepy
import matplotlib.pyplot as plt
from tkinter import *

top = Tk()
top.title("twitter sentiment analysis app")
top.geometry("400x250")

name = Label(top, text="hashtag to be checked").place(x=10, y=100)
#top.background()


sbmitbtn = Button(top, text="Go!", height="4" ,width="15", activebackground="green", activeforeground="blue").place(x=150, y=170)
#sbmitbtn.geometry("100x100")

searchTerm = Entry(top, bg="skyblue").place(x=150, y=100)


def percentage(part,whole):
    return 100*float(part)/float(whole)
consumerKey = "mFS0KnJiC4KSnj8wu2aDhnCoC"
consumerSecret = "kV4ccRp3icCHdsm3yLqst3RGCnYUZeksCtIo32imuU4FuM2xet"
accessToken = "1310137291034173442-h5g6KoTM9D72RFCdGKI6QaA9SCA8kV"
accessTokenSecret = "Ul0eT26pNQ6nBJjcP5dvickGvaTmSymuZFPYPhNmMZsVr"
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)
noOfSearchTerms = 10
#searchTerm = input("Enter keyword/Hashtag to search About : ")
#noOfSearchTerms = int(input("Enter how many tweets to analyse : "))
tweets = tweepy.Cursor(api.search,q=searchTerm).items(noOfSearchTerms)
positive = 0
negative = 0
neutral = 0
polarity = 0
for tweet in tweets:
   # print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity
    if(analysis.sentiment.polarity == 0):
        neutral += 1
    elif (analysis.sentiment.polarity < 0.00):
        negative += 1
    elif (analysis.sentiment.polarity > 0.00):
        positive += 1
positive = percentage(positive,noOfSearchTerms)
negative = percentage(negative,noOfSearchTerms)
neutral = percentage(neutral,noOfSearchTerms)
polarity = percentage(polarity,noOfSearchTerms)
positive = format(positive,'.2f')
negative = format(negative,'.2f')
neutral = format(neutral,'.2f')
print("how pepole are reacting on " + searchTerm +" after analysing " + str(noOfSearchTerms) + " tweets.")
if(polarity == 0):
    print("Neutral")
elif(polarity < 0.00):
    print("Negative")
elif(polarity > 0.00):
    print("positive")

labels = ['Positive ['+str(positive)+'%]','Negative ['+str(negative)+'%]','Neutral ['+str(neutral)+'%]']
size = [positive, negative , neutral]
colors = ['green', 'red', 'orange']
patches, texts = plt.pie(size, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title('how pepole are reacting on ' + searchTerm + ' after analysing ' + str(noOfSearchTerms) + ' tweets.')
plt.axis('equal')
plt.gcf().canvas.set_window_title('sentiment analysis by souravsing')
plt.tight_layout()
plt.show()
top.mainloop()
