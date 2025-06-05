import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Define OpenAI client
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv("GITHUB_TOKEN"))

# Calls OpenAI with a structured prompt to generate a blog post draft (Markdown), replacing {{AFF_LINK_n}} placeholders with dummy URLs.
def generate_blog_post(keyword, seo_metrics):
    prompt = f"""
    Write a SEO blog post about '{keyword}'.
    Write sections like: Introduction, Key Features, Benefits, Challenges, and Conclusion.
    Use this SEO data: Search Volume: {seo_metrics['search_volume']}, Difficulty: {seo_metrics['keyword_difficulty']}, CPC: {seo_metrics['avg_cpc']}
    Add the affiliate placeholders {{AFF_LINK_1}} and {{AFF_LINK_2}}.

    Return content in Markdown format. Do not include extra comments outside of the markdown.
    Avoid using smart quotes, em dashes, or any non-ASCII characters. Use only standard ASCII characters like straight quotes (' and "), hyphens (-), and regular punctuation.
    """

    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=1,
        model="gpt-4o-mini",
        max_tokens=4096,
        top_p=1
    )

    content = response.choices[0].message.content
    content = content.replace("{AFF_LINK_1}", "https://dummyurl1.com")
    content = content.replace("{AFF_LINK_2}", "https://dummyurl2.com")
    return content
