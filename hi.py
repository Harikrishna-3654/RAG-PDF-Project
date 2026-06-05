from dotenv import load_dotenv
from langchain_mistralai import MistralAIEmbeddings
import os

load_dotenv()

embedding_model = MistralAIEmbeddings(
    model="mistral-embed",
    api_key=os.getenv("MISTRAL_API_KEY")
)