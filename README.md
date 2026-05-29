# 🤖 RAG Chatbot with PDF Question Answering

A Retrieval-Augmented Generation (RAG) chatbot built using Streamlit, Groq, and Scikit-Learn. The application allows users to upload PDF documents and ask questions based on their contents. When no PDF is uploaded, the chatbot functions as a general-purpose AI assistant.

---

## 🚀 Features

* 💬 General AI Chat
* 📄 PDF Upload and Processing
* 🔍 Retrieval-Augmented Generation (RAG)
* 🧠 Context-Aware Question Answering
* ⚡ Powered by Groq LLMs
* 🖥️ Streamlit Web Interface
* 📚 TF-IDF Based Document Retrieval

---

## 🏗️ Project Architecture

User Query
↓
Document Loading
↓
Text Chunking
↓
TF-IDF Embeddings
↓
Similarity Retrieval
↓
Relevant Context
↓
Groq LLM
↓
Generated Response

---

## 📁 Folder Structure

```text
chatbot-project
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── sample_document.pdf
├── utils/
│   ├── loader.py
│   ├── embedder.py
│   └── retriever.py
└── screenshots/
    └── demo.png
```

---

## 📄 What Document Did You Use and Why?

For demonstration purposes, a PDF containing academic notes/technical documentation was used.

The document was chosen because it contains structured information suitable for retrieval-based question answering. This allows the chatbot to demonstrate how relevant information can be extracted and provided to the language model for accurate responses.

---

## ✂️ How Does Chunking Work?

The extracted PDF text is divided into fixed-size chunks of approximately 1000 characters.

Chunking helps:

* Process large documents efficiently
* Reduce prompt size
* Improve retrieval performance
* Provide only relevant information to the language model

Each user query retrieves the most relevant chunks using similarity search.

---

## 🧠 Which Embedding Model Did You Use?

This project uses **TF-IDF (Term Frequency – Inverse Document Frequency)** vectorization from Scikit-Learn.

The workflow is:

1. Convert document chunks into vector representations.
2. Convert user query into a vector.
3. Compute cosine similarity between query and chunks.
4. Retrieve the most relevant chunks.
5. Pass retrieved context to the LLM.

This provides a lightweight and efficient retrieval system suitable for educational RAG applications.

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### Language Model

* Groq API
* Llama 3.1 Instant

### Retrieval

* Scikit-Learn
* TF-IDF Vectorizer
* Cosine Similarity

### Document Processing

* PyPDF

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git https://github.com/Gowtham270807/ChatBot
cd Chatbot
```

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

The application will launch locally at:

```text
http://localhost:8501
```

---

## 🔑 Obtaining a Groq API Key

1. Create an account on Groq Console.
2. Generate an API key.
3. Enter the API key in the application's sidebar.
4. Start chatting or upload a PDF.

---

## 📄 Using PDF Question Answering

1. Upload a PDF document.
2. Ask questions related to the document.
3. The retriever identifies relevant chunks.
4. Retrieved context is passed to the LLM.
5. The chatbot generates an informed response.

Example questions:

* Summarize the document.
* How many minors are there?
* What is suitable to me?

---

## 📸 Screenshot

A working screenshot of the application can be found in:

```text
screenshots/demo.png
```

---

## 🔮 Future Improvements

Given more development time, the following enhancements could be implemented:

* Semantic embeddings using Sentence Transformers
* FAISS or ChromaDB vector database integration
* Multi-document support
* Source citations and page references
* Conversational memory
* Hybrid retrieval techniques
* Public deployment using Streamlit Community Cloud
* Advanced RAG pipelines with reranking

---

## 🎯 Learning Outcomes

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* PDF document processing
* Text chunking strategies
* Information retrieval techniques
* Vector representations using TF-IDF
* Similarity search with cosine similarity
* LLM integration using Groq
* Streamlit application development

---

## 👨‍💻 Author

Gowtham Sai M

Electronics and Communication Engineering
BITS Pilani, Hyderabad Campus

---

## 📜 License

This project was developed for educational and learning purposes.
