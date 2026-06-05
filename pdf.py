from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter =RecursiveCharacterTextSplitter (
    chunk_size=1000,
    chunk_overlap=1
)
    
loader = PyPDFLoader(r"C:\Users\Harik\Downloads\Trysol_Global_Services_Report.pdf")
documents = loader.load()

chunks= splitter.split_documents(documents)

print(chunks)
