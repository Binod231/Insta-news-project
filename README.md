﻿# Insta-news-project
This is a simple Flask-based web application that fetches and displays the latest news articles using the NewsAPI. Users can search for news on any topic, and the app returns relevant articles filtered for quality.

🔧 Features
🔍 Search for real-time news based on keywords.

🧠 Filters out articles from "Yahoo" and titles with "removed".

🎨 Responsive and clean UI styled using Bootstrap SCSS.

🌐 Fetches data dynamically from NewsAPI using requests.

💡 Uses render_template() to display articles in an HTML template.

🛠️ Tech Stack
Backend: Python, Flask

Frontend: HTML (Jinja2 Templates), Bootstrap SCSS

Styling Tools: SCSS (Bootstrap Custom)

API: NewsAPI.org

Others: requests, .gitignore, Flask routing

🚀 How to Run
1.Clone the repo.

2.Install dependencies: pip install Flask requests

3.Add your NewsAPI key to config.py:
NEWS_API_KEY = "your_api_key_here"

4.Run the app:
python app.py

## 🌄 Website Preview

Main UI of project
![Screenshot (267)](https://github.com/user-attachments/assets/8bf85ad3-0566-455a-a6b6-eda69a709e41)

News card 
![Screenshot (269)](https://github.com/user-attachments/assets/7e4af287-5c72-42e6-8c2b-bc36194e6b9d)

After clicking on news article card
![Screenshot (270)](https://github.com/user-attachments/assets/49eb6a5b-e9c8-4a7a-b2e9-5cf64af127c1)

You can search particular news
![Screenshot (298)](https://github.com/user-attachments/assets/56251e37-f005-4739-9f50-1fe9260733ca)
