# 📊 Reddit Sentiment Dashboard (ReputationMonitorApp)

A powerful Flask-based web application that scrapes Reddit posts for a given keyword, performs sentiment analysis using **TextBlob**, and visualizes public sentiment in an interactive dashboard.

---

## 🔥 Features

- 🔍 **Live Reddit Search**: Searches Reddit in real-time using the PRAW API.
- 🧠 **Sentiment Analysis**: Categorizes posts as Positive, Neutral, or Negative.
- 📈 **Data Visualization**: Displays sentiment statistics in a clean dashboard.
- 🚀 **Deploy-Ready**: Easily deployable on platforms like Render.

---

## 🛠️ Tech Stack

- **Python 3.11**
- **Flask** – Web framework  
- **PRAW** – Python Reddit API Wrapper  
- **TextBlob** – Sentiment analysis  
- **Pandas** – Data handling  
- **Gunicorn** – Production WSGI server

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Someshsw1109/ReputationMonitorApp.git
cd reddit-sentiment-dashboard


### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate

### 3. Install dependencies

```bash
pip install -r requirements.txt

### 4. Create a .env file (for local development)

```REDDIT_CLIENT_ID=your_client_id
   REDDIT_CLIENT_SECRET=your_client_secret
   REDDIT_USER_AGENT=ReputationMonitorApp by /u/your_reddit_username

### 5. Run the app

```bash
python app.py

```Visit: http://127.0.0.1:5000/ in your browser.


👨‍💻 Author
[Somesh Raj]
GitHub: @Someshsw1109
Reddit: /u/Lonely-Discount-6781