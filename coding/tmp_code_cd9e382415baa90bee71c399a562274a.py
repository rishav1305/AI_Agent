import requests
from bs4 import BeautifulSoup
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Get the webpage content
url = "https://ww.gettingstarted.ai/autogen-studio-overview"
response = requests.get(url)
html_content = response.text

# Extract text from HTML
soup = BeautifulSoup(html_content, 'html.parser')
text = soup.get_text()

# Clean the text by removing unwanted characters and tags
cleaned_text = re.sub(r'<[^>]+>', '', text)  # Remove HTML tags
cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)  # Remove special characters

# Convert to lowercase and split into words
words = cleaned_text.lower().split()

# Define stop words and short words
stop_words = set(["the", "and", "is", "in", "that", "of", "to", "at", 
                 "for", "with", "on", "this", "there", "from", "it",
                 "which", "but", "not", "a", "an", "or", "as", "if"])
short_words = set(w for w in words if len(w) < 4)

# Filter words
filtered_words = [word for word in words 
                  if word not in stop_words and 
                  word not in short_words]

# Generate word cloud
wordcloud = WordCloud(
    width=800,
    height=600,
    max_words=100,
    prefer_horizontal=1.0,
).generate(' '.join(filtered_words))

# Plot the word cloud
plt.figure(figsize=(16, 9))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig("wordcloud.png", dpi=300, bbox_inches='tight', transparent=True)
plt.show()