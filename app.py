from flask import Flask, render_template, request
import requests
from config import NEWS_API_KEY

#create a Flask application
app = Flask(__name__)

# Define a route for the news page
@app.route('/')
def index():
    query = request.args.get('query', "latest")
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data.get('articles', [])
    filtered_articles = [article for article in articles if "Yahoo" not in article['source']['name'] and "removed" not in article['title'].lower()]

    if not articles:
        return render_template('index.html', error="No articles found")
    return render_template('index.html', articles=filtered_articles, query=query)



app.run(debug=True)