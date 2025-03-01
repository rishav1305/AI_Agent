import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_word_cloud(url):
    try:
        # Fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        
        # Parse HTML and extract text
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        
        # Clean the text (remove special characters, numbers, etc.)
        cleaned_text = ''.join([c.lower() if c.isalpha() else ' ' for c in text])
        
        # Generate word cloud
        wordcloud = WordCloud(
            width=800,
            height=400,
            max_words=100,
            stopwords={'the', 'is', 'and', 'in', 'that', 'of', 'to', 'a', 'it'},
            background_color='white',
            min_font_size=10
        ).generate(cleaned_text)
        
        # Display the word cloud
        plt.figure(figsize=(16, 8))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.savefig('word_cloud.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_url_here' with the actual URL you want to process
generate_word_cloud('https://www.gettingstarted.ai/autogen-studio-overview')