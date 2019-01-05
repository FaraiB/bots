#reddit bot to reply to comments mentioning Zimbabwe
#zimbot1 04/01/2019

import praw
import time

def bot_login():
    print ("Logging into Reddit...")
    reply = praw.Reddit(username = "user_name",
                    password = "password",
                    client_id = "xxxXXXxxx",
                    client_secret = "XXXxxxXXX",
                    user_agent = "xxxx")
    print ("Logged into Reddit!")

    return reply

def run_bot(reply):
    print ("Obtaining 100 comments...")
    for comment in reply.subreddit('testingground4bots').comments(limit=100):
        if "zim" in comment.body:
            print ("Mention of Zimbabwe found!")
            comment.reply("Did you know that Zimbabwe was named after the [Great Zimbabwe](https://i.imgur.com/Q8zam4n.jpg) ruins?")
            print ("Replied to comment " + comment.id) 

 
reply = bot_login()

run_bot(reply)