import praw
import pandas as pd

reddit = praw.Reddit(client_id='3', client_secret='#', user_agent='#') # Using credentials to use Reddit API
Indian_reddit =reddit.subreddit('India') # Subreddit in reddit



get_flairs = Indian_reddit.search("AskIndia", limit=1000)
posts = []
flair="AskIndia"
for submission in get_flairs:
    submission.comments.replace_more(limit=0)
    comments=''
    for comment in submission.comments.list():
        comments = ' '+comments + comment.body
    posts.append([submission.title, submission.score, submission.id, submission.permalink, submission.num_comments, submission.selftext, submission.over_18,submission.author,comments,flair])
data = pd.DataFrame(posts,columns=['title', 'score', 'id', 'url', 'num_comments', 'body', 'over_18','author','comments','flair'])

flairs_except_1 = ["Non-Political", "[R]eddiquette", "Scheduled", "Photography", "Science/Technology", "Politics", "Business/Finance", "Policy/Economy", "Sports", "Food", "AMA"]

for flair in flairs_except_1:
    get_flairs = Indian_reddit.search(flair, limit=1000)
    posts = []
    for submission in get_flairs:
        submission.comments.replace_more(limit=0)
        comments=''
        for comment in submission.comments.list():
            comments = ' '+comments + comment.body
        posts.append([submission.title, submission.score, submission.id, submission.permalink, submission.num_comments, submission.selftext, submission.over_18,submission.author,comments,flair])
    data_temp = pd.DataFrame(posts,columns=['title', 'score', 'id', 'url', 'num_comments', 'body', 'over_18','author','comments','flair'])
    data=pd.concat([data,data_temp], sort =False)
    print(flair)
data.to_csv('./Reddit-ML-model(4).csv', index=False)
