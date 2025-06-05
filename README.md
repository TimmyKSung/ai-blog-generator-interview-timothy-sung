# ai-blog-generator-interview-timothy-sung – Flask App
This is a simplified Flask application that, given a keyword, performs a bit of “SEO research” and then calls OpenAI to generate a draft blog post (with basic structure and placeholder affiliate links). Additionally, it sets up a scheduler so the app automatically generates a new post for a predefined keyword, 'wireless earbuds' once per day.

## Features

- Accepts a user-provided keyword via web form or directly in the URL
- Fetches mock SEO metrics (CPC, difficulty, search volume) for the keyword
- Generates blog content using OpenAI based on the keyword and SEO metrics
- Displays a saved example blog post from file 
    - example_wireless_earbuds.md
- Automatically generates a blog post daily via APScheduler

## Tech Stack

- Python 3.13.3
- Flask
- OpenAI API
- APScheduler
- Markdown Parser
- Github

## Project Structure
- app.py                            # Main Flask app
- ai_generator.py                   # OpenAI blog post generation logic
- seo_fetcher.py                    # Mock SEO metric fetch logic
- example_wireless_earbuds.md       # Automatically generated daily example blog post
- .env                              # API key storage
- requirements.txt                  # Dependencies to pip install
- README.md

## Installation

1. **Clone the repository**
git clone https://github.com/TimmyKSung/ai-blog-generator-interview-timothy-sung.git

2. **Install dependencies**
pip install -r requirements.txt

3. **Set up environment variables**
Add OPEN_API_KEY or GITHUB_TOKEN to .env
If using OPEN_API_KEY, change ai_generator.py starting at line 7 to:

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv("OPEN_API_KEY"))

4. **Run the app**
python app.py

## Author
Timothy Sung