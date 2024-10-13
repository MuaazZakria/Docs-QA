# PDF Documents Q&A

This project is a PDF-based Question-Answering (Q&A) system built using Streamlit, FAISS, Google Gemini embeddings, and the Llama language model (via ChatGroq). Users can upload multiple PDF documents, and then ask questions about the content. The system processes the documents, retrieves relevant sections, and answers the questions using a powerful LLM.


## Overview

This system allows users to:
1. Upload PDF documents.
2. Ask questions about the uploaded documents.
3. Receive detailed answers based on the content of the PDFs.

The solution uses a combination of FAISS (for vector search) and Google Gemini embeddings to represent the document content, while the Llama language model answers the user's questions.

## Features

- **PDF Upload**: Users can upload up to 100 PDF files for processing.
- **Document Search**: The system uses FAISS to efficiently search for relevant document sections.
- **Chat Interface**: Users can interact with the system using a chat-like interface, where they can ask questions and receive answers.
- **Unanswerable Queries**: If no relevant content is found in the documents, the system informs the user that no relevant information was found.

## Technology Stack 

- **Streamlit**: Used to build the web interface.
- **LangChain**: Provides utilities for language models and chains.
- **FAISS**: For fast document vector search.
- **Google Gemini Embeddings**: Used for embedding document content into vectors.
- **ChatGroq (Llama Model)**: Used
- **PyPDFLoader**: For processing and extracting text from PDF files.
- **Tempfile**: For managing temporary file storage for PDF uploads.

## Limitations 
- The system is limited to processing a maximum of 100 PDFs at a time.
- Large PDFs with extensive content may take longer to process and return answers.
- The system currently handles only English-language documents and questions.

## Environment Variables 
Ensure that the following environment variables are set in your `.env` file:
- `GROQ_API_KEY`: The API key to access Llama models via ChatGroq.
- `GOOGLE_API_KEY`: The API key for Google Gemini embeddings.
- The API keys are required for the vector search and the LLM response generation

## Installation

Follow these steps to set up and run the system on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/MuaazZakria/Docs-QA.git
cd Docs-QA
```

### 2. Create a Virtual Environment

Create a virtual environment using Python 3.10:

```bash
python3.10 -m venv venv
```
Activate the virtual environment:

- On Windows:
```bash
.\venv\Scripts\activate
```
- On macOS and Linux:
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application
Run the Streamlit application:

```bash
streamlit run app.py
```

Open the provided URL in your web browser to interact with the application.

## Interacting with the Application

- The panel on the left side of the page will allow you to upload your documents.
- Once the documents are uploaded, you need to click on **Load Documents** button to generate their embeddings
- If you upload more than 100 documents and click on **Load Documents** button, then an error will be raised.
- Once the embeddings are generated, you can chat with the bot.
