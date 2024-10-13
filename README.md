# Docs-QA

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

## Installation

Follow these steps to set up and run the system on your local machine.

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Create a Virtual Environment

Create a virtual environment using Python 3.10:

```bash
python3.10 -m venv venv
```
Activate the virtual environment:

On Windows:
```bash
.\venv\Scripts\activate
```
On macOS and Linux:
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
