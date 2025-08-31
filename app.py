# /app.py

import streamlit as st
import pandas as pd
from modules.web_search import search_web_for_context
from modules.news_analyzer import analyze_news_with_llm
from modules.dashboard import display_analysis_results

# --- Page Configuration ---
st.set_page_config(
    page_title="Fake News Detector Using LLM",
    page_icon="🔎",
    layout="wide"
)

# --- Application Title and Description ---
st.title("🔎 Fake News Detector & Social Engineering Prevention By Higher Authority")
st.markdown("""
Welcome to the Fake News Detector. This tool helps you analyze news articles to determine their authenticity. 
Upload a CSV file with news articles, and the system will use AI and web search to fact-check each one.
""")
st.info("This tool uses the `gemma3` LLM via Ollama and Google search via Serper. Make sure your Ollama application is running.")

# --- File Uploader ---
st.header("1. Upload Your News Dataset")
uploaded_file = st.file_uploader("Upload a CSV file containing news articles.", type="csv")

if uploaded_file is not None:
    try:
        # Load the uploaded CSV into a DataFrame
        df = pd.read_csv(uploaded_file)
        
        # Verify that the necessary columns exist
        required_columns = {'title', 'text'}
        if not required_columns.issubset(df.columns):
            st.error(f"Error: The uploaded CSV must contain 'title' and 'text' columns. Found columns: {list(df.columns)}")
        else:
            st.success("✅ CSV file loaded successfully!")
            st.write("Here's a preview of your data:")
            st.dataframe(df.head())

            # --- Analysis Section ---
            st.header("2. Analyze News Articles")
            st.write("Select an article from your dataset to analyze.")

            # Let the user select an article by its title
            selected_title = st.selectbox(
                "Choose an article to analyze:",
                options=df['title']
            )

            if selected_title:
                # Get the selected article's data
                article_to_analyze = df[df['title'] == selected_title].iloc[0].to_dict()

                # Display the selected article's text
                with st.expander("View selected article text"):
                    st.write(article_to_analyze.get('text', 'No text available.'))

                # Button to trigger the analysis
                if st.button("🚀 Analyze This Article", key=f"analyze_{article_to_analyze.get('id', selected_title)}"):
                    
                    # Step 1: Search the web for context
                    with st.spinner("Searching the web for related news..."):
                        web_context = search_web_for_context(article_to_analyze['title'])

                    # Step 2: Analyze the article with the LLM
                    if not web_context:
                        st.warning("Could not find any context online. Analysis will be less reliable.")
                    
                    with st.spinner("🧠 The AI is analyzing the article... This might take a moment."):
                        analysis_result = analyze_news_with_llm(article_to_analyze, web_context)
                    
                    st.success("✅ Analysis complete!")

                    # Step 3: Display the results
                    display_analysis_results(analysis_result, web_context)

    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")
else:
    st.info("👆 Upload a CSV file to get started.")