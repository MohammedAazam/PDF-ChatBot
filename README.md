# 📄 PDF Q&A ChatBot

Upload a PDF and ask questions about its content using **Gemini AI**!  
Built with **Streamlit**, this app uses **LangChain**, **FAISS**, and **Google Generative AI** to provide accurate answers based on your document.

---

## 🚀 Features

- 📚 Upload any PDF and ask context-aware questions
- 🧠 Powered by Google Gemini-Pro (via LangChain)
- 🧾 Custom prompt template support
- ⚡ Fast text extraction and vector search with FAISS
- 🐞 Debug Mode to view internal operations
- 🌐 Clean and responsive Streamlit UI

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **AI Model:** Gemini-Pro (Google Generative AI)
- **Text Extraction:** PyPDF2
- **Vector Store:** FAISS
- **RAG Chain:** LangChain
- **Environment:** Python, dotenv

---

## 🔧 Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pdf-chatbot.git
cd pdf-chatbot
```

### 2. Create a Virtual Environment

```bash
# Linux/macOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧪 Run the App

Make sure your `.env` is configured (see below), then run:

```bash
streamlit run app.py
```

## 🔐 .env Configuration

Create a `.env` file in the root directory:

```bash
GOOGLE_API_KEY=your-google-api-key-here
```
> ✅ To get your API key, enable the [Google Generative AI API](https://makersuite.google.com/app) and generate one in Google Cloud Console.


## 📁 Project Structure

``` bash
pdf-chatbot/
├── app.py                 # Main Streamlit app
├── requirements.txt       # Python dependencies
├── .env.example           # Sample environment file
├── modules/
│   ├── pdf_loader.py      # Extracts text from PDF
│   ├── vector_store.py    # Embedding + FAISS index
│   └── rag_chain.py       # LangChain QA logic
```

## 📦 requirements.txt

```
streamlit 
langchain 
faiss-cpu
PyMuPDF
langchain-google-genai
langchain-huggingface
langchain-community 
langchain-text-splitters
tf-keras
```


## 💡 Usage

1. Upload a PDF via the interface.
2. Ask questions in natural language.
3. Get context-aware answers based on your document.
4. Use Debug Mode (sidebar) to view extracted text, vector store status, and response time.

---

## 🐞 Troubleshooting

- **GOOGLE_API_KEY not set**  
  Make sure `.env` exists and contains your key.

- **No response or timeouts**  
  Gemini may take a few seconds. Use Debug Mode to trace errors.

- **FAISS import issues**  
  Run `pip install faiss-cpu` (Windows/Linux/macOS supported).

---

## 🧠 Example Custom Prompt

Customize your prompt in the sidebar:

```
You are a helpful assistant. Answer the question based on the following document context.

Context:
{context}

Question: {question}
```

---

## 🖼️ Screenshot

![image](https://github.com/user-attachments/assets/0b69fe1d-5502-412b-8681-8abbb8fb1670)

---

## 📜 License

MIT License. Use freely and contribute back if you like it! 🤝

---

## 💬 Feedback or Contributions

Open issues, suggest ideas, or submit pull requests! Let's build better AI tools together.

---
