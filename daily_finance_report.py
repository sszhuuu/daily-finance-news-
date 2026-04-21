import requests
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import schedule
import time

# Email configuration
EMAIL_ADDRESS = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_password'
RECEIVER_EMAIL = 'cicizhuyanfei@gmail.com'

# Fetch news from multiple sources
def fetch_news():
    sources = [
        'https://newsapi.org/v2/everything?q=finance&apiKey=your_api_key',
        'https://another-news-api.com/latest?category=finance'
    ]
    news_articles = []
    for url in sources:
        response = requests.get(url)
        if response.status_code == 200:
            news_articles.extend(response.json().get('articles', []))
    return news_articles

# Analyze news articles
def analyze_news(articles):
    # Placeholder for analysis logic
    analysis = "Critical analysis based on sentiment or impact."
    return analysis

# Map stakeholders
def stakeholder_mapping():
    stakeholders = [
        'Investors',
        'Regulators',
        'Analysts',
        'Media'
    ]
    return stakeholders

# Generate report
def generate_report():
    news_articles = fetch_news()
    analysis = analyze_news(news_articles)
    stakeholders = stakeholder_mapping()
    report_content = f"Daily Financial Report - {datetime.now().strftime('%Y-%m-%d')}\n\n"
    report_content += "== News Articles ==\n"
    for article in news_articles:
        report_content += f"Title: {article['title']}\nURL: {article['url']}\n\n"
    report_content += "== Analysis ==\n"
    report_content += analysis + '\n\n'
    report_content += "== Stakeholders ==\n"
    report_content += ', '.join(stakeholders) + '\n'
    return report_content

# Send email
def send_email(report):
    msg = MIMEText(report)
    msg['Subject'] = 'Daily Financial News Report'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECEIVER_EMAIL

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

# Scheduler
def schedule_report():
    report = generate_report()
    send_email(report)

schedule.every().day.at('09:00').do(schedule_report)

while True:
    schedule.run_pending()
    time.sleep(1)