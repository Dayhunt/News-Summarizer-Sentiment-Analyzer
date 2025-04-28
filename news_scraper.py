import requests
from bs4 import BeautifulSoup

def scrape_news(url):
    try:
        # Send a request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Check for successful response
        if response.status_code != 200:
            return "⚠️ Unable to fetch the article. Status Code: {}".format(response.status_code)

        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Try to find the article text
        paragraphs = soup.find_all('p')

        # If paragraphs are found, join them into a single string
        if paragraphs:
            article_text = ' '.join([para.get_text() for para in paragraphs])
            return article_text

        # If no paragraphs are found, check for other possible tags
        alternative_paragraphs = soup.find_all(['div', 'span', 'article'])
        if alternative_paragraphs:
            article_text = ' '.join([para.get_text() for para in alternative_paragraphs])
            return article_text

        return "⚠️ Unable to extract article content."

    except requests.exceptions.RequestException as e:
        return f"⚠️ Error during request: {str(e)}"
    except Exception as e:
        return f"⚠️ An unexpected error occurred: {str(e)}"
