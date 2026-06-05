

\# RAG PDF Vector Database Builder



\## Introduction



This project implements the document ingestion and indexing stage of a Retrieval-Augmented Generation (RAG) pipeline using LangChain and FAISS.



The application loads PDF documents, splits the content into chunks, generates embeddings using Hugging Face Sentence Transformers, and stores the embeddings in a FAISS vector database for efficient semantic retrieval.



\---



\## Problem Statement



Large Language Models cannot directly search through custom PDF documents.



To enable document retrieval, PDF content must first be converted into vector embeddings and stored in a vector database.



This project automates that process.



\---



\## Technologies Used



\* Python

\* LangChain

\* FAISS

\* HuggingFace Embeddings

\* Sentence Transformers

\* Mistral AI

\* python-dotenv



\---



\## Workflow



1\. Load PDF document

2\. Extract text from PDF

3\. Split text into chunks

4\. Generate embeddings

5\. Store embeddings in FAISS

6\. Save vector database locally



\### Architecture



PDF File

↓

PyPDFLoader

↓

RecursiveCharacterTextSplitter

↓

HuggingFaceEmbeddings

↓

FAISS Vector Store

↓

Local Vector Database



\---



\## Embedding Model



Model:



sentence-transformers/all-MiniLM-L6-v2



This model converts text chunks into dense vector representations suitable for semantic search.



\---



\## Chunk Configuration



| Parameter     | Value |

| ------------- | ----- |

| Chunk Size    | 1000  |

| Chunk Overlap | 200   |



\---



\## Installation



Clone the repository:



git clone https://github.com/Harikrishna-3654/RAG-PDF-Project.git



Move into the project directory:



cd RAG-PDF-Project



Install dependencies:



pip install -r requirements.txt



\---



\## Running the Project



Update the PDF path in:



create\_database.py



Execute:



python create\_database.py



\---



\## Output



The project generates a FAISS vector database:



faiss\_db/



├── index.faiss



└── index.pkl



These files contain vector embeddings of the PDF content.



\---



\## Future Scope



\* Build document retrieval system

\* Implement semantic search

\* Integrate Mistral LLM

\* Create Question Answering pipeline

\* Develop complete RAG chatbot

\* Deploy using Streamlit



\---



\## Skills Demonstrated



\* LangChain

\* Vector Databases

\* FAISS

\* Embeddings

\* Document Processing

\* Retrieval-Augmented Generation (RAG)

\* Python Development



\---



\## Author



Harikrishna



GitHub: https://github.com/Harikrishna-3654



