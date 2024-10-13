import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import tempfile
import time

# Load environment variables (ensure .env file contains keys)
load_dotenv()

# Load API keys
groq_api_key = os.getenv('GROQ_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')
os.environ["GOOGLE_API_KEY"] = google_api_key

# Page title
st.set_page_config(page_title="Document Q&A", layout="wide")
st.title("PDF Document Q&A System")

# Layout: Sidebar for document uploading, center for chat
with st.sidebar:
    st.header("Upload Documents")
    uploaded_files = st.file_uploader("Upload PDF files", accept_multiple_files=True, type="pdf")

    # Button to load and process the documents
    if st.button("Load Documents"):
        if uploaded_files:
            with st.spinner('Processing documents and creating vector store...'):
                # Initialize embeddings for FAISS vector store using Google Gemini
                embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

                # Load and process PDFs
                if len(uploaded_files) > 100:
                    st.error("You can upload a maximum of 100 PDF documents.")
                else:
                    documents = []
                    for uploaded_file in uploaded_files:
                        # Save uploaded file to a temporary location
                        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                            temp_file.write(uploaded_file.read())
                            temp_file_path = temp_file.name

                        # Load PDF content
                        loader = PyPDFLoader(temp_file_path)
                        documents.extend(loader.load())

                    # Split documents into chunks for efficient processing
                    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
                    split_documents = text_splitter.split_documents(documents)

                    # Create FAISS vector store from document chunks
                    st.session_state.vector_store = FAISS.from_documents(split_documents, embeddings)

                    st.success('Vector Store created!')
        else:
            st.error("Please upload at least one PDF file.")

# Main chat interface layout
chat_container = st.container()

# Display chat history and input box
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Function to answer questions based on document context
def answer_question(question):
    if "vector_store" in st.session_state:
        retriever = st.session_state.vector_store.as_retriever()
        docs_with_context = retriever.get_relevant_documents(question)

        if docs_with_context:
            context = " ".join([doc.page_content for doc in docs_with_context])
        else:
            context = "No relevant information found."

        # Create a chain to use Llama (via ChatGroq) to answer the question
        chain = LLMChain(
            llm=ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192"),
            prompt=PromptTemplate(
                input_variables=["context", "question"],
                template="""
                You are an AI assistant. Answer the following question based on the given context from documents:
                Context: {context}
                Question: {question}
                Answer with as much relevant detail as possible, or say 'No relevant information found' if the context does not provide an answer.
                """
            )
        )
        answer = chain.run({"context": context, "question": question})
        return answer
    else:
        return "Documents are not loaded yet. Please upload and load the documents first."

# Chat Interface: Display conversation
with chat_container:
    st.header("Chat with the AI Assistant")
    
    # User input for chat
    user_question = st.text_input("Enter your question")

    # If the user enters a question and presses the button, answer it
    if st.button("Send", key="send_button"):
        if user_question:
            with st.spinner('Fetching response...'):
                start_time = time.process_time()
                response = answer_question(user_question)
                response_time = time.process_time() - start_time

                # Append to chat history
                st.session_state.chat_history.append((user_question, response, response_time))
                
                # Display the updated chat
                for i, (q, a, t) in enumerate(st.session_state.chat_history):
                    st.markdown(f"**You:** {q}")
                    st.markdown(f"**AI Assistant:** {a}")
                    st.markdown(f"*Response time: {t:.2f} seconds*")
                    st.write("---")
        else:
            st.error("Please enter a question.")
