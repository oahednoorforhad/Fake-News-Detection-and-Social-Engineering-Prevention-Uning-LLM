# Fake News Detector & Social Engineering Prevention

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

[cite_start]An intelligent system designed to detect fake news and mitigate social engineering attacks by leveraging a Large Language Model (LLM) enhanced with real-time web context[cite: 35, 41]. [cite_start]This project was submitted in fulfillment of the Computer Security course at the International Islamic University Chittagong (IIUC)[cite: 5, 7].

## 📝 Overview

[cite_start]The proliferation of fake news serves as a potent vector for social engineering attacks, manipulating human behavior to compromise security[cite: 33, 48]. [cite_start]This project introduces a detection system that counters this threat by providing real-time, explainable analysis of news articles[cite: 35].

[cite_start]The framework integrates a Large Language Model (**Gemma3**) with **Retrieval-Augmented Generation (RAG)** and **Chain-of-Thought (CoT)** prompting[cite: 36, 99].
* [cite_start]**RAG** fetches up-to-date web articles to ground the LLM's analysis in verifiable facts, reducing hallucinations[cite: 37, 64].
* [cite_start]**CoT** guides the model to reason in a transparent, step-by-step manner, making its final verdict interpretable[cite: 38, 65].
* [cite_start]The system outputs a clear classification ("Real" or "Fake"), a confidence score, and a detailed explanation of its reasoning[cite: 39].

## ✨ Key Features

* [cite_start]**LLM-Powered Analysis:** Utilizes the Gemma3 large language model, run locally via Ollama for data privacy and control[cite: 120].
* [cite_start]**Real-Time Fact-Checking:** Employs the Serper.dev API to retrieve relevant web context, ensuring analysis is based on current information[cite: 109, 131].
* [cite_start]**Transparent Reasoning:** Leverages Chain-of-Thought (CoT) prompting to generate clear, step-by-step explanations for each verdict[cite: 115, 117].
* [cite_start]**Confidence Scoring:** Provides a quantitative confidence score (0.0 to 1.0) for each classification, indicating the model's certainty[cite: 39, 66, 126].
* [cite_start]**Interactive UI:** A user-friendly interface built with Streamlit allows for easy CSV upload, article selection, and visualization of results[cite: 40, 138, 139].

## 🛠️ Technology Stack

* [cite_start]**Frontend:** Streamlit [cite: 138]
* [cite_start]**LLM Orchestration:** LangChain [cite: 128]
* [cite_start]**LLM Serving:** Ollama [cite: 120]
* [cite_start]**Core Model:** Gemma3 [cite: 120]
* [cite_start]**Web Retrieval:** Serper.dev Google Search API [cite: 131][cite_start], `requests` [cite: 206]
* [cite_start]**Article Parsing:** `newspaper3k` [cite: 110, 132]
* [cite_start]**Data Handling:** Pandas [cite: 185, 195]

## 🚀 Setup and Installation

### Prerequisites
1.  **Python:** Ensure you have Python 3.9 or newer installed.
2.  **Ollama:** Install [Ollama](https://ollama.ai/) on your machine.
3.  **Gemma3 Model:** Pull the Gemma3 model by running:
    ```sh
    ollama pull gemma3
    ```
4.  **Serper API Key:** Get a free API key from [Serper.dev](https://serper.dev).

### Installation Steps
1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/fake-news-detector-llm-rag.git](https://github.com/your-username/fake-news-detector-llm-rag.git)
    cd fake-news-detector-llm-rag
    ```

2.  **Create a virtual environment (recommended):**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
    *Note: A `requirements.txt` file should be created containing packages like `streamlit`, `pandas`, `requests`, `newspaper3k`, `langchain-community`, `langchain`, and `ollama`.*

4.  **Set up environment variables:**
    [cite_start]Create a file named `.env` in the root directory and add your Serper API key as shown in the project's code[cite: 209]:
    ```
    SERPER_API_KEY="your_serper_api_key_here"
    ```

## ▶️ How to Run

1.  [cite_start]Ensure your Ollama application is running in the background[cite: 282].

2.  Launch the Streamlit web application:
    ```sh
    streamlit run app.py
    ```
    *(Assuming your main script is named `app.py`)*

3.  Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

##  E- Usage

1.  [cite_start]**Upload Data:** Use the file uploader to select a CSV file containing news articles[cite: 102, 191]. [cite_start]The CSV must have `title` and `text` columns[cite: 103].
2.  [cite_start]**Select Article:** Choose an article from the dropdown menu[cite: 196].
3.  [cite_start]**Analyze:** Click the "Analyze" button to start the process[cite: 198].
4.  **View Results:** The system will display:
    * [cite_start]A final **verdict** ("Real" or "Fake")[cite: 262, 264].
    * [cite_start]A **confidence score** percentage[cite: 265].
    * [cite_start]A detailed **reasoning** for the verdict[cite: 267].
    * [cite_start]The **web context** (sources) used for the analysis[cite: 268].

## 🔮 Future Work

Based on the project report, future enhancements include:
* [cite_start][ ] **Quantitative Evaluation:** Integrate labeled datasets to measure accuracy, precision, recall, and F1-score[cite: 422].
* [cite_start][ ] **Ablation Studies:** Quantify the performance impact of RAG and CoT components[cite: 423].
* [cite_start][ ] **Social Engineering Detection:** Add modules to specifically identify phishing indicators and persuasion techniques[cite: 425].
* [cite_start][ ] **Model Exploration:** Test and benchmark other LLMs (e.g., GPT-4, Llama-3)[cite: 426].
* [cite_start][ ] **Real-Time Integration:** Connect to live data streams like social media feeds to detect emerging campaigns[cite: 427].
* [cite_start][ ] **Source Credibility:** Develop mechanisms to assess the reliability of retrieved web sources[cite: 428].

## 👨‍💻 Authors

This project was developed by:
* [cite_start]**Oahed Noor Forhad** (C213056) [cite: 2, 11]
* **Md. [cite_start]Tohedul Islam Nirzon** (C213060) [cite: 3, 12]
* [cite_start]**Saiful Islam Rumi** (C211080) [cite: 4, 13]

Under the supervision of **Md. [cite_start]Ziaul Hoque**, Adjunct Faculty, Dept. of CSE, IIUC[cite: 18].

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
