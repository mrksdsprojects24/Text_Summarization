import streamlit as st
from transformers import pipeline

st.title("Krishna's Text Summarization App")

# Define the summarization pipeline
model_name = "Falconsai/text_summarization"  
summarizer = pipeline("summarization", model=model_name)

# User input field for text
user_text = st.text_input("Enter the text you want to summarize:")

# Button to trigger summarization
if st.button("Summarize"):
  if user_text:
    # Summarize the text using the pipeline
    summary = summarizer(user_text)[0]['summary_text']

    # Display the summary
    st.success("Summary:")
    st.write(summary)
  else:
    st.warning("Please enter some text to summarize.")
