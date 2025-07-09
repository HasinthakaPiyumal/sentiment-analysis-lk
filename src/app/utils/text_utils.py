import re
import emoji

def emoji_to_text(text):
    return emoji.demojize(text, delimiters=(" ", " "))  # Convert emojis to text with spaces around them
    
def clean_comment(text):
    text = text.lower()
    text = re.sub(r"@[\w_-]+", '', text)  # remove mentions (allowing _ and - in username)
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)  # remove URLs
    # Remove punctuation except Sinhala/Unicode letters
    text = re.sub(r"[^\w\s\u0D80-\u0DFF]", '', text)  # keep Sinhala Unicode range
    text = re.sub(r"\d+", '', text)  # remove numbers
    text = re.sub(r"\s+", ' ', text).strip()  # remove extra spaces
    return text