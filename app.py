from flask import Flask, request, jsonify
from markdown import markdown
import os
from dotenv import load_dotenv
from seo_fetcher import get_seo_metrics
from ai_generator import generate_blog_post
from apscheduler.schedulers.background import BackgroundScheduler

load_dotenv()
app = Flask(__name__)

# Given a keyword, generate a draft blog post
@app.route('/generate', methods=['GET'])
def generate():
    keyword = request.args.get('keyword')

    # If keyword is missing
    if not keyword:
        return f'''
        <h2>ERROR: MISSING KEYWORD</h2>
        ''', 400

    # Get SEO data
    seo_metrics = get_seo_metrics(keyword)
    blog_post = generate_blog_post(keyword, seo_metrics)

    return jsonify({
        "keyword": keyword,
        "seo_metrics": seo_metrics,
        "blog_post": blog_post
        })

@app.route('/')
def home():
    # Read example blog post and display it under user input form
    with open("example_wireless_earbuds.md", "r", encoding="utf-8-sig", errors="replace") as file:
        md = file.read()
        md_blog = markdown(md)
    
    return f'''
        <h2>AI Blog Generator Interview Timothy Sung</h2>
        <form action="/generate" method="get">
            <label for="keyword">Enter keyword:</label><br>
            <input type="text" id="keyword" name="keyword" required><br><br>
            <input type="submit" value="GET AI Blog Post">
        </form>
        <hr>
        <h3>example_wireless_earbuds.md</h3>
        <div>{md_blog}</div>
    '''

# Logic to generate the daily blog with predefined keyword
def generate_daily():
    keyword = "wireless earbuds"
    seo_metrics = get_seo_metrics(keyword)
    blog_post = generate_blog_post(keyword, seo_metrics)
    
    # Write to md file
    filename = "example_wireless_earbuds.md"
    with open(filename, "w") as file:
        file.write(blog_post)
    print("Generating daily blog post...")

# APScheduler to create daily blog
scheduler = BackgroundScheduler()
scheduler.add_job(generate_daily, 'interval', days=1)
scheduler.start()

if __name__ == '__main__':
    app.run(debug=True)
