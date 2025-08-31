# /modules/dashboard.py

import streamlit as st

def display_analysis_results(analysis: dict, web_context: list):
    """
    Displays the fake news analysis results and the web context in the Streamlit UI.
    
    Args:
        analysis (dict): The dictionary containing the 'label', 'confidence', and 'reasoning'.
        web_context (list): The list of context articles from the web search.
    """
    if not analysis:
        st.error("Analysis could not be completed.")
        return

    label = analysis.get("label", "Unknown")
    confidence = analysis.get("confidence", 0.0)
    reasoning = analysis.get("reasoning", "No reasoning provided.")

    st.subheader("📊 Analysis Result")

    # Display the final verdict with a color-coded metric
    if label == "Real":
        st.metric(label="Verdict", value="REAL NEWS", delta=f"Confidence: {confidence:.2%}", delta_color="normal")
        st.success("This article appears to be credible based on the analysis.")
    elif label == "Fake":
        st.metric(label="Verdict", value="FAKE NEWS", delta=f"Confidence: {confidence:.2%}", delta_color="inverse")
        st.warning("This article shows signs of being unreliable or fake.")
    else:
        st.metric(label="Verdict", value="ANALYSIS ERROR", delta_color="off")
        st.error("An error occurred during the analysis.")

    # Display the detailed reasoning from the LLM
    st.subheader("🧠 Reasoning")
    st.markdown(reasoning)

    # Display the web context that was used for fact-checking
    st.subheader("🌐 Web Context Used for Analysis")
    if not web_context:
        st.info("No web context was found to cross-reference the article.")
        return
        
    for i, article in enumerate(web_context):
        with st.expander(f"**Source #{i+1}:** {article['title']}"):
            st.markdown(f"**Link:** [{article['link']}]({article['link']})")
            st.caption(f"**Snippet:** {article['snippet']}")