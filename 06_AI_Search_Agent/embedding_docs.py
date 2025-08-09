from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

documents = []

# Load documents
for file in os.listdir("docs"):
    path = os.path.join("docs", file)
    if file.endswith(".pdf"):
        documents.extend(PyPDFLoader(path).load())
    elif file.endswith(".txt"):
        documents.extend(TextLoader(path, encoding="utf-8").load())

# Split text into chunks
splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(documents)

# Create embeddings
embedding_model = OpenAIEmbeddings()

# Create FAISS DB
db = FAISS.from_documents(chunks, embedding_model)

# Save index
db.save_local("search_index")
