import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud, Image
from nltk.corpus import stopwords

# Exclude common words
stopwords = set(stopwords.words('english') + ['by', 'the', 'and', 'is'])

def process_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    return text.lower()

def filter_words(text):
    words = text.split()
    filtered = [word for word in words if len(word) >=4 and word not in stopwords]
    return ' '.join(filtered)

# Fetch webpage content
url = "https://ww.gettingstarted.ai/autogen-studio-overview"
response = requests.get(url, timeout=10)
html_content = response.text

try:
    # Process the content
    clean_text = process_content(html_content)
    filtered_text = filter_words(clean_text)

    # Create wordcloud
    wordcloud = WordCloud(max_words=200, background_color="black", 
                          width=800, height=400, margin=20,
                          stopwords=stopwords).generate(filtered_text)

    # Save the image
    image = Image(wordcloud)
    image.save("wordcloud.png")
except Exception as e:
    print(f"An error occurred: {str(e)}")