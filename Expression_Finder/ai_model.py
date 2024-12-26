from transformers import pipeline

sentiment_analysis = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    return sentiment_analysis(text)
