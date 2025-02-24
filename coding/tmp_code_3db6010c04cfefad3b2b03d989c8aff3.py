import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
from PIL import Image

# Fetch the webpage content
url = 'https://ww.gettingstarted.ai/autogen-studio-overview'
response = requests.get(url)

# Parse the HTML and extract text
soup = BeautifulSoup(response.text, 'html.parser')
text = soup.get_text()

# Preprocess the text: convert to lowercase, split into words, remove non-alphabetic characters
words = []
for word in text.split():
    # Convert to lowercase and strip any non-alphabetic characters
    clean_word = ''.join([char.lower() for char in word if char.isalpha()])
    if len(clean_word) >= 4:
        words.append(clean_word)

# Define stop words to exclude
stop_words = {'the', 'and', 'is', 'in', 'of', 'to', 'a', 'an', 'at', 'by', 
              'for', 'from', 'on', 'with', 'as', 'it', 'this', 'that'}

# Filter out stop words and short words (already handled in preprocessing)
filtered_words = [word for word in words if word not in stop_words]

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(filtered_words))

# Save the word cloud as an image
Image.open(wordcloud).save("wordcloud.png")