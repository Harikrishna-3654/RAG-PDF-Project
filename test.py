from langchain_community.document_loaders import CSVLoader

from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(
    chunk_size=5000,
    chunk_overlap=1000
)

loader = CSVLoader(
    file_path="C:\\Users\\Harik\\Downloads\\Sales_Data.csv"
)
documents = loader.load()

chunks= splitter.split_documents(documents)

print(chunks)