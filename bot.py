#reddit bot to post to imgae of Great Zimababwe
#zimbot1 04/01/2019

import praw
import re
import time

reddit = praw.Reddit(username = "user_name",
                    password = "password",
                    client_id = "xxxXXXxxx",
                    client_secret = "XXXxxxXXX",
                    user_agent = "xxxx")

subreddits = ['testingground4bots', 'reddit_bot_test']
pos = 0
errors = 0
title = "Test GZ"
url="https://i.imgur.com/Q8zam4n.jpg"

def post():
        global subreddits
        global pos
        global errors
        
        try:
            subreddit = reddit.subreddit(subreddits[pos])
            subreddit.submit(title, url=url)
            print("Bot has successfully posted to " +  subreddits)

            pos = pos + 1

            if (pos <= len(subreddits) - 1):
                post()
            else:
                print ("done")
        except praw.exceptions.APIException as e:
            if (e.error_type == "RATELIMIT"):
                delay = re.search("(\d+) minutes?", e.message)

                if delay:
                    delay_seconds = float(int(delay.group(1)) * 60)
                    time.sleep(delay_seconds)
                    post()
                else:
                    delay = re.search("(\d+) seconds", e.message)
                    delay_seconds = float(delay.group(1))
                    time.sleep(delay_seconds)
                    post()
        except:
            errors = errors + 1
            if(errors>5):
                print("Bot Crashed!")
                exit(1)

post()