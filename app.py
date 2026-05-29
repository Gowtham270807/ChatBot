import streamlit as st
from openai import OpenAI

from utils.loader import load_pdf, chunk_text
from utils.embedder import create_embeddings
from utils.retriever import retrieve

st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖"
)

st.title("🤖 RAG Chatbot")

api_key = st.sidebar.text_input(
    "Groq API Key",
    type="password"
)

uploaded_file = st.sidebar.file_uploader(
    "Upload PDF",
    type="pdf"
)

MODEL = "llama-3.1-8b-instant"

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask something...")

if prompt:

    if not api_key:
        st.error("Please enter your Groq API key.")
        st.stop()

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )

    # NORMAL CHAT MODE
    final_prompt = prompt

    # PDF RAG MODE
    if uploaded_file:

        text = load_pdf(uploaded_file)

        chunks = chunk_text(text)

        vectorizer, vectors = create_embeddings(chunks)

        relevant_chunks = retrieve(
            prompt,
            vectorizer,
            vectors,
            chunks
        )

        context = "\n\n".join(relevant_chunks)

        final_prompt = f"""
Answer the question using the document context below.

DOCUMENT:

{context}

QUESTION:

{prompt}
"""

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": final_prompt
                    }
                ]
            )

            reply = response.choices[0].message.content

            st.markdown(reply)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )