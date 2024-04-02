# Audio_Transcribe_goML
![istockphoto-1350635646-612x612](https://github.com/HariniMaruthasalam/Audio_Transcribe_goML/assets/114240304/29bbcbef-ee8e-4e8a-81cb-3e4f990f92bb)

# Audio Transcription and Sentiment Analysis Project Report

## Introduction
The Audio Transcription and Sentiment Analysis project focus on analyzing audio content to extract meaningful insights and assess sentiment using advanced AI techniques. The project utilizes the AssemblyAI API for audio transcription, sentiment analysis models from the Transformers library, and Streamlit for creating a user-friendly web application.

## Methodology
### Transcription
- The audio file undergoes transcription using the AssemblyAI API.
- Spoken content is converted into textual format for further analysis.
### Sentiment Analysis
- Transcribed text undergoes sentiment analysis using pre-trained models from the Transformers library.
- Positive and negative sentiment scores are calculated based on confidence levels.
### Word Cloud Generation
- Key segments of the transcribed text are collected for generating a word cloud.
- The word cloud visually represents the most frequently occurring words in the transcribed content.
### KPI Calculation
- Key Performance Indicators (KPIs) such as AHT, FCR, and CSAT are calculated based on the transcribed and analyzed content.
### Visualization
- KPIs and sentiment scores are presented in a Streamlit web application.
- Matplotlib is used for data visualization, including plotting KPIs and generating word clouds.

## Technologies Used
- AssemblyAI API for audio transcription with sentiment analysis and auto-highlighting features.
- Transformers library for sentiment analysis using pre-trained models.
- Streamlit for building the interactive web application.
- Matplotlib for data visualization, including plotting KPIs and generating word clouds.

## Key Findings
### Sentiment Analysis
- Positive sentiment is predominant in the transcribed content.
- Some segments show negative sentiment, suggesting areas for improvement.
### KPIs
- AHT falls within an acceptable range, indicating efficient handling of queries.
- FCR rate is high, indicating strong issue resolution during initial interactions.
- CSAT score is generally positive, reflecting high customer satisfaction.
### Word Cloud
- Word cloud highlights key themes or topics discussed in the audio content.
- Commonly occurring words align with positive sentiment and high CSAT scores.

## Interactive Dashboard
- Streamlit web application provides an intuitive interface for exploring and analyzing results.
- Users can interact with visualizations to gain deeper insights into the audio content and performance metrics.

## Actionable Insights
- Insights can be used to optimize operations, train agents, and enhance customer experience.

## Challenges
- Faced challenges with the Lyzr API and calculating/plotting APIs, requiring extra time and effort.

