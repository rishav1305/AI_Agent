# filename: generate_wordcloud.py
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Step 1: Fetch the content from the URL
url = "https://www.gettingstarted.ai/autogen-studio-overview"  # Corrected URL
response = requests.get(url)
content = response.text

# Step 2: Clean the content
soup = BeautifulSoup(content, 'html.parser')
text = soup.get_text()

# Remove common stop words and filter words
custom_stopwords = set(STOPWORDS).union({"the", "and", "is"})
words = [word for word in text.split() if len(word) >= 4 and word.lower() not in custom_stopwords]

cleaned_text = ' '.join(words)

# Step 3: Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(cleaned_text)

# Step 4: Save the image as "wordcloud.png"
wordcloud.to_file("wordcloud.png")
print("Word cloud saved as 'wordcloud.png'.")