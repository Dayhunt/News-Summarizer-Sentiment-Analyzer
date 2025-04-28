import streamlit as st
from news_scraper import scrape_news
from summarizer import summarize_text
from translation import detect_language, translate_to_english
from sentiment import analyze_sentiment

# Streamlit App UI
st.set_page_config(page_title="News Summarizer & Sentiment Analyzer", page_icon="📰")

st.title("📰 News Summarizer & Sentiment Analyzer")

# Section for entering a news URL
url = st.text_input("Enter a news article URL:")

if st.button("Process URL"):
    if url.strip() == "":
        st.warning("⚠️ Please enter a valid news article URL!")
    else:
        with st.spinner("🔎 Scraping news..."):
            article_text = scrape_news(url)

        if article_text == "Article content not found.":
            st.warning("⚠️ Unable to extract article content.")
        else:
            # Detect language & translate if needed
            with st.spinner("🌐 Detecting language..."):
                lang = detect_language(article_text)

            if lang != "en":
                with st.spinner(f"🌐 Detected '{lang}'. Translating to English..."):
                    article_text = translate_to_english(article_text)

            # Summarize the article
            with st.spinner("📝 Summarizing text..."):
                summary = summarize_text(article_text)

            # Perform sentiment analysis on the summary
            with st.spinner("💬 Analyzing sentiment..."):
                sentiment = analyze_sentiment(summary)

            # Display results
            st.subheader("Summary:")
            st.success(summary)

            st.subheader("Sentiment Analysis:")
            st.info(f"Label: {sentiment['label']}, Confidence: {sentiment['score']:.2f}")
