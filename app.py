import os
from flask import Flask, render_template
import praw
from textblob import TextBlob
import pandas as pd

app = Flask(__name__)

def scrape_reddit(keyword, limit):
    reddit = praw.Reddit(
        client_id=os.getenv('REDDIT_CLIENT_ID'),
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
        user_agent=os.getenv('REDDIT_USER_AGENT')
    )
    posts = []
    for submission in reddit.subreddit("all").search(keyword, limit=limit):
        posts.append(submission.title + " " + submission.selftext)
    return posts

def analyze_sentiment(texts):
    sentiment_data = []
    for text in texts:
        score = TextBlob(text).sentiment.polarity
        sentiment = 'Positive' if score > 0.1 else 'Negative' if score < -0.1 else 'Neutral'
        sentiment_data.append((text, round(score, 2), sentiment))
    return pd.DataFrame(sentiment_data, columns=['text', 'polarity', 'sentiment'])

@app.route('/')
def dashboard():
    keyword = "OpenAI"
    reddit = scrape_reddit(keyword, 30)
    df = analyze_sentiment(reddit)
    sentiment_counts = df['sentiment'].value_counts().to_dict()
    mentions = df.to_dict(orient='records')
    return render_template("dashboard.html", sentiment_counts=sentiment_counts, mentions=mentions, keyword=keyword)

if __name__ == "__main__":
    app.run(debug=True)
