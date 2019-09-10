import praw
import pandas as pd

data=pd.read_csv('../precog_reddit/reddit-50k.csv')
posts = []
count=0
for url in data['url']:
    print(count)
    count+=1
    reddit = praw.Reddit(client_id='KDMo4mS_QD1eqw', client_secret='RPKj_1mVLobhY7IBbFhHiu0nY4o', user_agent='WebScrapper') # Using credentials to use Reddit API
    Info = reddit.submission(url="https://www.reddit.com"+url)

    Info.comments.replace_more(limit=0)
    comments=''
    for comment in Info.comments.list():
      comments = ' '+comments + comment.body
    posts.extend([comments, Info.selftext])
x = pd.DataFrame.from_records(posts)
