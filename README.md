# Fake News Detection & Social Engineering Prevention Using LLM

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

This project is an intelligent system that detects fake news to help prevent social engineering attacks. It uses a Large Language Model (LLM) with real-time web fact-checking to provide transparent, accurate analysis of news articles.

---

## ✨ Key Features

* 🧠 **Intelligent Analysis**: Uses the **Gemma3** Large Language Model, run locally via **Ollama**, to analyze news content while ensuring data privacy.
* 🌐 **Real-Time Fact-Checking**: Implements **Retrieval-Augmented Generation (RAG)** by fetching current web articles via the **Serper.dev API** to ground the analysis in verifiable facts.
* 🔍 **Transparent Reasoning**: Employs **Chain-of-Thought (CoT)** prompting to force the LLM to explain its reasoning step-by-step, making the final verdict easy to understand.
* 🎯 **Confidence Scoring**: Outputs a classification ("Real" or "Fake") along with a numerical confidence score, giving users insight into the model's certainty.
* 🖥️ **User-Friendly Interface**: A simple and interactive UI built with **Streamlit** allows for easy CSV file uploads, article selection, and clear visualization of the results.

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **AI & Backend**: Python, LangChain, Ollama
* **Core Model**: Gemma3
* **Services & APIs**: Serper.dev, newspaper3k
* **Data Handling**: Pandas

---

## 🚀 Getting Started

### Prerequisites
* ✅ Python 3.9+
* ✅ [Ollama](https://ollama.ai/) installed and running.
* ✅ Gemma3 model pulled via `ollama pull gemma3`
* ✅ A free API key from [Serper.dev](https://serper.dev)

### Installation
1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/fake-news-detector-llm-rag.git](https://github.com/your-username/fake-news-detector-llm-rag.git)
    cd fake-news-detector-llm-rag
    ```
2.  **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
3.  **Set Environment Variable:**
    Create a `.env` file in the root directory and add your API key:
    ```
    SERPER_API_KEY="your_serper_api_key_here"
    ```

---

## ▶️ Usage

1.  **Start the app:**
    Make sure Ollama is running, then launch the Streamlit interface.
    ```sh
    streamlit run app.py
    ```
2.  **Upload a CSV file** containing news articles. It must have `title` and `text` columns.
3.  **Select an article** from the dropdown menu.
4.  **Click "Analyze"** and view the verdict, confidence score, detailed reasoning, and the web sources used for fact-checking.

---

## 🔮 Future Work

* **Quantitative Evaluation:** Integrate labeled datasets to measure accuracy, precision, recall, and F1-score.
* **Ablation Studies:** Quantify the performance impact of RAG and CoT components.
* **Social Engineering Detection:** Add modules to specifically identify phishing indicators and persuasion techniques.
* **Model Exploration:** Test and benchmark other LLMs (e.g., GPT-4, Llama-3).
* **Real-Time Integration:** Connect to live data streams like social media feeds to detect emerging campaigns.
* **Source Credibility:** Develop mechanisms to assess the reliability of retrieved web sources.

---

## 👨‍💻 Authors

This project was developed by:
* **Oahed Noor Forhad** (C213056)
* **Md. Tohedul Islam Nirzon** (C213060)
* **Saiful Islam Rumi** (C211080)

Under the supervision of **Md. Ziaul Hoque**, Adjunct Faculty, Dept. of CSE, IIUC.

## 📜 License

This project is licensed under the MIT License.
