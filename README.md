Trysol RAG project
Overview

This project is a document retrieval application built using LangChain, Hugging Face Embeddings, and FAISS.

The application reads a PDF document, splits the content into chunks, converts the chunks into vector embeddings, stores them in a FAISS vector database, and retrieves the most relevant document sections based on user queries.

Features
Load PDF documents using PyPDFLoader
Split documents into manageable text chunks
Generate embeddings using Hugging Face models
Store vectors in a FAISS database
Perform semantic similarity search
Retrieve the top matching document chunks
Technologies Used
Python
LangChain
FAISS
Hugging Face Embeddings
PyPDF
Python Dotenv
Project Structure
trysol_rag_project/
│
├── create_database.py
├── query_data.py
├── requirements.txt
├── faiss_db/
└── README.md
Installation
1. Clone the Repository
git clone https://github.com/veerababu74/trysol_rag_project.git
cd trysol_rag_project
2. Create a Virtual Environment
python -m venv .venv
3. Activate the Virtual Environment

Windows:

.venv\Scripts\activate
4. Install Dependencies
pip install -r requirements.txt
Create the Vector Database

Update the PDF path in create_database.py.

Run:

python create_database.py

Output:

Database Created Successfully

This will:

Load the PDF document.
Split the document into chunks.
Create embeddings using the MiniLM model.
Store the vectors in a FAISS database.
Save the database locally in the faiss_db folder.
Query the Database

Run:

python query_data.py

Example:

Ask a question: What services does Trysol provide?

The application retrieves the top 5 most relevant chunks from the vector database and displays them.

Embedding Model
sentence-transformers/all-MiniLM-L6-v2
Vector Store
FAISS
Workflow
PDF Document
      │
      ▼
Document Loader
      │
      ▼
Text Splitter
      │
      ▼
Embeddings Model
      │
      ▼
FAISS Vector Database
      │
      ▼
User Query
      │
      ▼
Similarity Search
      │
      ▼
Relevant Results
Future Improvements
Integrate Mistral AI for answer generation
Convert into a complete RAG application
Add FastAPI backend
Create a Streamlit web interface
Support multiple PDF documents
Add conversational memory
Author

Harikrishna