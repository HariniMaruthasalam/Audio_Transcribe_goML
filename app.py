import assemblyai as ai
import streamlit as st
from transformers import pipeline
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

ai.settings.api_key = "fcc1790480634364a797423218cd6285"
audio_url = r"D:/ML/neuralgo/MLTask/CallDataSample/sample_call_1.mp3"

config = ai.TranscriptionConfig(sentiment_analysis=True, auto_highlights=True)

transcript = ai.Transcriber().transcribe(audio_url, config)

highlights = []
for result in transcript.auto_highlights.results:
    highlights.append(result.text)


# Initialize the sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

# Function to transcribe audio and perform sentiment analysis
def transcribe_and_analyze_sentiment(file_path):
    # Perform audio transcription
    # Replace this with your actual transcription code
    transcript_text = "Transcription of audio file goes here"

    # Split the input text into smaller segments that fit within the maximum sequence length
    max_seq_length = classifier.model.config.max_position_embeddings
    segments = [transcript_text[i:i + max_seq_length] for i in range(0, len(transcript_text), max_seq_length)]

    # Perform sentiment analysis on each segment and aggregate the results
    sentiments = {'positive': 0.5, 'negative': 0.6}
    for segment in segments:
        result = classifier(segment)
        for res in result:
            if res['label'] == 'POSITIVE':
                sentiments['positive'] += res['score']
            if res['label'] == 'NEGATIVE':
                sentiments['negative'] += res['score']

    return sentiments

# Function to generate word cloud from highlighted words
def generate_word_cloud(highlights):
    # Convert the list of highlighted words into a single string
    highlighted_text = " ".join(highlights)

    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(highlighted_text)

    return wordcloud

def calculate_AHT(highlights):
    # Calculate Average Handle Time (AHT) based on the duration of highlights
    total_highlight_duration = sum(len(highlight.split()) for highlight in highlights)
    total_highlights = len(highlights)
    
    if total_highlights != 0:
        aht = total_highlight_duration / total_highlights
    else:
        aht = 0
    
    return aht

def calculate_FCR(highlights):
    # Calculate First Call Resolution (FCR) based on the presence of keywords indicating resolution
    resolution_keywords = ['resolved', 'solved', 'fixed']  # Add more resolution keywords if needed
    
    resolved_calls = 0
    total_calls = len(highlights)
    
    for highlight in highlights:
        for keyword in resolution_keywords:
            if keyword in highlight.lower():
                resolved_calls += 1
                break
    
    if total_calls != 0:
        fcr = (resolved_calls / total_calls) * 100
    else:
        fcr = 80
    
    return fcr

def calculate_CSAT(highlights):
    # Calculate Customer Satisfaction Score (CSAT) based on the sentiment analysis
    positive_sentiment = 0
    negative_sentiment = 0
    total_sentiments = len(highlights)
    
    for highlight in highlights:
        sentiments = transcribe_and_analyze_sentiment(highlight)
        positive_sentiment += sentiments['positive']
        negative_sentiment += sentiments['negative']
    
    if total_sentiments != 0:
        csat = (positive_sentiment / total_sentiments) * 100
    else:
        csat = 0
    
    return csat

# Define function to plot KPIs
def plot_KPIs(aht, fcr, csat):
    # Plotting KPIs using matplotlib
    fig, ax = plt.subplots()
    ax.barh(['AHT', 'FCR', 'CSAT'], [aht, fcr, csat])
    ax.set_xlabel('Score')
    ax.set_title('Key Performance Indicators')
    st.pyplot(fig)

def main():
    # Streamlit app title
    st.title("Audio Transcription and Sentiment Analysis App")

    # File upload section
    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3"])
    if uploaded_file is not None:
        st.write("File Uploaded Successfully!")
        file_path = "./temp_audio.mp3"  # Temporary file path, replace with actual path
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        # Perform transcription and sentiment analysis
        sentiments = transcribe_and_analyze_sentiment(file_path)

        # Display sentiment scores
        st.write("Sentiment Scores:")
        st.write(f"Positive Score: {sentiments['positive']}")
        st.write(f"Negative Score: {sentiments['negative']}")

        # Word cloud generation
        
        wordcloud = generate_word_cloud(highlights)

        # Display word cloud
        st.write("Word Cloud of Highlighted Words:")
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot()
        
        aht = calculate_AHT(highlights)
        fcr = calculate_FCR(highlights)
        csat = calculate_CSAT(highlights)

        # Display KPIs and plot
        st.write("Key Performance Indicators:")
        st.write(f"Average Handle Time (AHT): {aht}")
        st.write(f"First Call Resolution (FCR): {fcr}")
        st.write(f"Customer Satisfaction Score (CSAT): {csat}")

        # Plotting KPIs
        plot_KPIs(aht, fcr, csat)

if _name_ == "_main_":
    main()
