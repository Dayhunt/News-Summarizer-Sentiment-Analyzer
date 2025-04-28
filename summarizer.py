from transformers import pipeline

# Load pre-trained summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    try:
        # Make sure the text length is within the acceptable model input range
        max_input_length = 1024  # BART has a max token input of 1024
        if len(text.split()) > max_input_length:
            text = ' '.join(text.split()[:max_input_length])  # Truncate if it's too long

        # Use summarizer pipeline
        summary = summarizer(text, max_length=250, min_length=90, do_sample=False)
        return summary[0]['summary_text']
    
    except Exception as e:
        return f"⚠️ Error during summarization: {str(e)}"
