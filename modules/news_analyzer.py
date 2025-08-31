# /modules/news_analyzer.py

import json
import re
from langchain_community.chat_models import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# --- LLM Configuration ---
# Ensure the Ollama application is running and the gemma3 model is pulled.
# Command: ollama pull gemma3
try:
    llm = ChatOllama(model="gemma3:latest", temperature=0.2, format="json", model_kwargs={'num_predict': 4096})
except Exception as e:
    print(f"Error initializing Ollama: {e}")
    llm = None

# --- Prompt Template ---
# This prompt guides the LLM to perform a step-by-step analysis and return a structured JSON output.
prompt_template = PromptTemplate.from_template(
    """
    You are a professional fact-checker. Your task is to analyze a news article based on the context from other web sources and determine if it is "Real" or "Fake".

    **Analyze the following news article:**
    - **Title:** "{news_title}"
    - **Text:** "{news_text}"

    **Use the provided web context from multiple sources to verify the claims:**
    --- WEB CONTEXT START ---
    {web_context}
    --- WEB CONTEXT END ---

    **Perform the following reasoning steps:**
    1.  **Identify the Core Claim:** What is the main assertion or claim made in the news article?
    2.  **Cross-Reference with Context:** Do the provided web context articles support or contradict the core claim? Mention specific sources from the context.
    3.  **Analyze Language and Tone:** Examine the original article for signs of bias, sensationalism, emotional language, or other characteristics of fake news.
    4.  **Synthesize Findings:** Based on the evidence, what is your conclusion? Is the information consistent and verified across multiple reliable sources, or is it an outlier?

    **Provide your final verdict and a detailed explanation in a JSON format.** The `label` must be either "Real" or "Fake".

    {{
      "label": "...",
      "confidence": <a float between 0.0 and 1.0>,
      "reasoning": "..."
    }}
    """
)

def format_web_context(context_articles: list) -> str:
    """Formats the list of context articles into a single string for the prompt."""
    formatted_context = []
    for i, article in enumerate(context_articles):
        formatted_context.append(
            f"**Source {i+1}: {article['title']}**\n"
            f"URL: {article['link']}\n"
            f"Snippet: {article['snippet']}\n"
            f"Full Text (truncated): {article.get('full_text', 'Not available')}\n"
            f"---"
        )
    return "\n".join(formatted_context)

def analyze_news_with_llm(news_article: dict, context_articles: list) -> dict:
    """
    Analyzes a news article for authenticity using an LLM with web context.
    
    Args:
        news_article: A dictionary representing the news article to be analyzed.
                      Expected keys: 'title', 'text'.
        context_articles: A list of dictionaries with context from web search.
        
    Returns:
        A dictionary containing the analysis result (label, confidence, reasoning).
    """
    if not llm:
        return {
            "label": "Error",
            "confidence": 0.0,
            "reasoning": "LLM is not available. Make sure Ollama is running."
        }
        
    chain = LLMChain(llm=llm, prompt=prompt_template)
    
    formatted_context = format_web_context(context_articles)
    
    if not formatted_context.strip():
        formatted_context = "No web context was found. Analysis is based solely on the provided article text."

    try:
        response_text = chain.run(
            news_title=news_article.get('title', ''),
            news_text=news_article.get('text', ''),
            web_context=formatted_context
        )
        
        # The 'format="json"' parameter in ChatOllama should handle this automatically
        # but a fallback is good practice.
        result = json.loads(response_text)
        return result
        
    except json.JSONDecodeError:
        return {
            "label": "Error",
            "confidence": 0.0,
            "reasoning": f"Failed to parse JSON response from the LLM. Response: {response_text}"
        }
    except Exception as e:
        return {
            "label": "Error",
            "confidence": 0.0,
            "reasoning": f"An unexpected error occurred during LLM analysis: {e}"
        }