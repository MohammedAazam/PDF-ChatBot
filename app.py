import streamlit as st
import os
import time
from modules.pdf_loader import extract_text_from_pdf
from modules.vector_store import create_vector_store
from modules.rag_chain import get_qa_chain
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit Page Config
st.set_page_config(page_title="PDF ChatBot", layout="wide", page_icon="📄")

# Style - Inject Custom CSS
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
            padding: 2rem;
        }
        .block-container {
            padding-top: 2rem;
        }
        .title {
            font-size: 2.5rem;
            font-weight: 700;
            color: #ffffff;
        }
        .subtitle {
            color: #7f8c8d;
            font-size: 1.2rem;
            margin-bottom: 1.5rem;
        }
        .stButton > button {
            border-radius: 8px;
            padding: 10px 20px;
            background-color: #3498db;
            color: white;
            font-weight: 600;
        }
        .stTextInput > div > input {
            border-radius: 8px;
        }
        .stTextArea > div > textarea {
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# API Check
if "GOOGLE_API_KEY" not in os.environ:
    st.error("⚠ GOOGLE_API_KEY not found. Please add it in your .env file.")
    st.stop()

# Header
st.markdown('<div class="title">📄 PDF ChatBot by XLabs</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload a PDF and ask anything about it!</div>', unsafe_allow_html=True)

# Layout
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📂 Upload PDF")
    uploaded_file = st.file_uploader("Drop your PDF here", type=["pdf"])

    debug_mode = st.toggle("🛠 Debug Mode", value=False)
    custom_prompt = st.text_area(
        "📝 Custom Prompt Template",
        value="""You are a helpful assistant. Answer the question based on the document below.\n\nContext:\n{context}\n\nQuestion: {question}""",
        height=180
    )

with col2:
    if uploaded_file:
        st.success("✅ File uploaded successfully!")
        with st.spinner("🧠 Processing your document..."):
            try:
                text = extract_text_from_pdf(uploaded_file)
                st.session_state.pdf_text = text

                if debug_mode:
                    st.info(f"🔍 Extracted {len(text)} characters")

                vector_store = create_vector_store(text)
                chain = get_qa_chain(vector_store)

                st.session_state.chain = chain
                st.success("✅ Document ready for Q&A!")

            except Exception as e:
                st.error(f"❌ Failed to process PDF: {str(e)}")
                if debug_mode:
                    st.exception(e)
                st.stop()

    # Ask Question
    if "chain" in st.session_state and st.session_state.chain:
        question = st.text_input("❓ Ask your question")
        if question:
            with st.spinner("🤔 Thinking..."):
                try:
                    start = time.time()
                    response = st.session_state.chain.invoke({"query": question})
                    end = time.time()

                    result = response.get("result", response)
                    st.success("✅ Answer:")
                    st.markdown(f"**{result}**")

                    if debug_mode:
                        st.caption(f"⏱️ Took {end - start:.2f} seconds")

                except Exception as e:
                    st.error("⚠️ Error generating response")
                    if debug_mode:
                        st.exception(e)

# Optional Debug
if debug_mode and "pdf_text" in st.session_state:
    with st.expander("📜 Raw PDF Text Sample"):
        st.code(st.session_state.pdf_text[:1000] + "...")
