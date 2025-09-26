import praw
import pandas as pd

#URL to access the app needed to scrape the data off the Berkeley subreddit
# https://www.reddit.com/prefs/apps


#PLAN
#Scrape the data off the Berkeley subreddit about consulting clubs
#Organize that data using the pandas library
#Create chatbot that utilizes natural language processing that will give users feedback
#about each consulting club here at Berkeley. 

reddit_read_only = praw.Reddit(client_id = "QlBfNfxQ3e_MGP9RkaOQig",
                               client_secret = "SpLjOwYdQPU4z1wqcXBjVl_7DnUIZg",
                               user_agent = "Berkeley_Consulting")

subreddit = reddit_read_only.subreddit("berkeley")

# This is test code if nothing is working
# #Display the name of the subreddit
# print("Display Name:", subreddit.display_name)

# #Display the title of the subreddit
# print("Title:", subreddit.title)

# #Display the description of the subreddit
# print("Description:", subreddit.description)


posts = subreddit.hot()
for post in posts:
    lowerCaseTitle = post.title.lower()
    if "consulting" in lowerCaseTitle and "club" in lowerCaseTitle:
        print(post.title+ "\n")
    else:
        continue

# subreddit._fetch()

# print(sorted(vars(subreddit).keys()))

# print("Display Name:", subreddit.display_name)

# try:
#     print("Title:", subreddit.unsubscribe)
# except Exception as e:
#     print("Error:", e)

# print("Title:", subreddit.title)

# print("Description:", subreddit.description)
