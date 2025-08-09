from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import os
from dotenv import load_dotenv
load_dotenv()

documents = []

for file in os.listdir("docs"):
    if file.endswith(".pdf"):
        documents.extend(PyPDFLoader(f"docs/{file}").load())
    elif file.endswith(".txt"):
        documents.extend(TextLoader(f"docs/{file}").load())


splitter = CharacterTextSplitter(chunk_size=700, chunk_overlap=100)
chunks = splitter.split_documents(documents)
embedding_model = OpenAIEmbeddings()

db = FAISS.from_documents(chunks, embedding_model)
db.save_local("search_index")
