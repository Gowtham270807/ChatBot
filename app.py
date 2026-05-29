import streamlit as st
from openai import OpenAI
from pypdf import PdfReader

# ---------------- PAGE SETUP ----------------

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Chatbot")
st.caption("Normal Chat + PDF Chat")

# ---------------- SIDEBAR ----------------

st.sidebar.header("Settings")

api_key = st.sidebar.text_input(
    "Enter your Groq API Key",
    type="password"
)

MODEL = st.sidebar.selectbox(
    "Choose Model",
    [
        "llama-3.1-8b-instant",
        "llama-3.3-70b-versatile"
    ]
)

uploaded_file = st.sidebar.file_uploader(
    "Upload PDF (Optional)",
    type="pdf"
)

# ---------------- CHAT HISTORY ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- PDF TEXT EXTRACTION ----------------

pdf_text = ""

if uploaded_file:

    pdf_reader = PdfReader(uploaded_file)

    for page in pdf_reader.pages:

        text = page.extract_text()

        if text:
            pdf_text += text

    st.sidebar.success("PDF Loaded Successfully!")

# ---------------- DISPLAY CHAT ----------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- CLEAR CHAT ----------------

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# ---------------- USER INPUT ----------------

prompt = st.chat_input("Ask anything...")

if prompt:

    # API key check
    if not api_key:
        st.error("Please enter your Groq API key.")
        st.stop()

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Create Groq client
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )

    # ---------------- WITH PDF ----------------

    if uploaded_file and pdf_text.strip():

        context = pdf_text[:12000]

        enhanced_prompt = f"""
You are a helpful AI assistant.

Use the PDF content below to answer the question whenever relevant.

PDF CONTENT:
{context}

QUESTION:
{prompt}

If the answer is not in the PDF,
you may still answer normally using your own knowledge.
"""

    # ---------------- NORMAL CHAT ----------------

    else:

        enhanced_prompt = prompt

    # ---------------- AI RESPONSE ----------------

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = client.chat.completions.create(
                    model=MODEL,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful AI assistant."
                        },
                        {
                            "role": "user",
                            "content": enhanced_prompt
                        }
                    ]
                )

                reply = response.choices[0].message.content

                st.markdown(reply)

                # Save assistant reply
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": reply
                    }
                )

            except Exception as e:
                st.error(f"Error: {e}")