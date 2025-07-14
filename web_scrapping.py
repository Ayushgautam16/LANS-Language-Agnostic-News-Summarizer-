import requests
from bs4 import BeautifulSoup

def get_content_from(url):
    try:
        # Making a GET request to the URL
        r = requests.get(url)

        # Checking if the request was successful (status code 200)
        if r.status_code == 200:

            soup = BeautifulSoup(r.content, 'html.parser')

            # Finding all paragraphs in the HTML content
            paragraphs = soup.find_all('p')

            # Joining paragraphs into a single string
            content_text = ' '.join([p.get_text() for p in paragraphs])

            return content_text

        else:
            return f"Failed to retrieve content. Status code: {r.status_code}"

    except Exception as e:
        return f"An error occurred: {str(e)}"
