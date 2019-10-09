#importing libraries
import flask
import pickle
from flask import Flask, render_template,request
import praw
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import make_pipeline
from nltk.corpus import stopwords
import re
import contractions


wnl = WordNetLemmatizer()
remove =set(stopwords.words('english'))
def edit(words):
    words =str(words)
    words=re.sub('([.,////])',' ',words)
    words=re.sub('\[.*?\]', '', words)
    words = words.replace('\n', ' ')
    words = contractions.fix(words)
    word_list = nltk.word_tokenize(re.sub(r'([^a-z A-Z])', '', words.lower()))
    comment = ' '.join([wnl.lemmatize(w) for w in word_list if w not in remove])
    return comment


def edit2(words):
    words=str(words)
    if 'https://www.reddit.com/r/india/comments/' in words:
        count =0
        s=''
        for i in range(len(words)):
            if words[i]=='/':
                count+=1
            elif count==7:
                s+=words[i]
        lis = s.split('_')
        t=' '.join(word for word in lis )
        return str(t)
    else:
        return words

def Praw_data(URL):
    reddit = praw.Reddit(client_id='%', client_secret='%', user_agent='WebScrapper') # Using credentials to use Reddit API
    Info = reddit.submission(url=URL)
    posts = []
    Info.comments.replace_more(limit=0)
    comments=''
    for comment in Info.comments.list():
        comments = ' '+comments + comment.body
    posts.extend([Info.title, comments, Info.selftext, Info.url,Info.link_flair_text])
    posts[0]=edit(posts[0])
    posts[1]=edit(posts[1])
    posts[2]=edit(posts[2])
    posts[3]=edit2(posts[3])
    s=''
    s=posts[0]+' '+posts[1]+' '+posts[2]+' '+posts[3]
    print(s)
    return (s,posts[4])






app=Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/flair',methods=['POST'])
def flair():
    URL=request.form['GetURL']
    combined_str, flair = Praw_data(URL)
    loaded_model = pickle.load(open("model(3).pkl","rb"))
    result=loaded_model.predict([combined_str])
    result=result[0]
    return render_template('flair.html',result = str(result),flair=flair)


@app.route('/statistics')
def stats():
    return render_template('statistics.html')

if __name__ == '__main__':
    app.run(debug=True)
