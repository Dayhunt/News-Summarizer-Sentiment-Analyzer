from transformers import pipeline

# Load sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    """Analyzes the sentiment of the given text."""
    result = sentiment_analyzer(text)[0]
    return result
 
 