from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()

import tkinter as tk
from tkinter import ttk
from tkinter import *

def ask_searchTerm():
    searchTerm = simpledialog.askstring(title="souravs app", prompt="enter hashtag to be searched : ")
    noOfSearchTerms = simpledialog.askinteger(title='souravs app', prompt="enter number of tweets to analysis : ")
    def percentage(part, whole):
        return 100 * float(part) / float(whole)


    consumerKey = "mFS0KnJiC4KSnj8wu2aDhnCoC"
    consumerSecret = "kV4ccRp3icCHdsm3yLqst3RGCnYUZeksCtIo32imuU4FuM2xet"
    accessToken = "1310137291034173442-h5g6KoTM9D72RFCdGKI6QaA9SCA8kV"
    accessTokenSecret = "Ul0eT26pNQ6nBJjcP5dvickGvaTmSymuZFPYPhNmMZsVr"
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(auth)
    # searchTerm = input("Enter keyword/Hashtag to search About : ")
    # noOfSearchTerms = int(input("Enter how many tweets to analyse : "))
    tweets = tweepy.Cursor(api.search, q=searchTerm).items(noOfSearchTerms)
    positive = 0
    negative = 0
    neutral = 0
    polarity = 0
    for tweet in tweets:
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        polarity += analysis.sentiment.polarity
        if (analysis.sentiment.polarity == 0):
            neutral += 1
        elif (analysis.sentiment.polarity < 0.00):
            negative += 1
        elif (analysis.sentiment.polarity > 0.00):
            positive += 1
    positive = percentage(positive, noOfSearchTerms)
    negative = percentage(negative, noOfSearchTerms)
    neutral = percentage(neutral, noOfSearchTerms)
    polarity = percentage(polarity, noOfSearchTerms)
    positive = format(positive, '.2f')
    negative = format(negative, '.2f')
    neutral = format(neutral, '.2f')
    # polarity = format(polarity,'.2f')
    print("how pepole are reacting on " + searchTerm + " after analysing " + str(noOfSearchTerms) + " tweets.")
    if (polarity == 0):
        print("Neutral")
    elif (polarity < 0):
        print("Negative")
    elif (polarity > 0):
        print("positive")

    labels = ['Positive [' + str(positive) + '%]', 'Negative [' + str(negative) + '%]', 'Neutral [' + str(neutral) + '%]']
    size = [positive, negative, neutral]
    colors = ['green', 'red', 'orange']
    wp = {'linewidth': 1, 'edgecolor': "black"}
    patches, texts = plt.pie(size, colors=colors, startangle=90, shadow="true", labels=labels, wedgeprops=wp)
    plt.legend(patches, labels, loc="best")
    plt.title('how pepole are reacting on ' + searchTerm + ' after analysing ' + str(noOfSearchTerms) + ' tweets.')
    plt.axis('equal')
    plt.gcf().canvas.set_window_title('sentiment analysis by souravsing')
    plt.tight_layout()
    plt.show()
root = Tk()
root.geometry('891x592')
root.configure(background='#66CDAA')
root.title('Twitter Sentiment Analysis app ')

Label(root, text='Sentiment Analysis App Powered by Python', bg='#66CDAA', font=('verdana', 22, 'bold')).place(x=77, y=78)

Button(root, text='Fire the engine...!', bg='#008B8B', font=('verdana', 20, 'bold'), command=ask_searchTerm).place(x=290, y=260)

Label(root, text='This app is created by Souravsing with 🖤', bg='#66CDAA', font=('helvetica', 18, 'bold')).place(x=195, y=462)

root.mainloop()
