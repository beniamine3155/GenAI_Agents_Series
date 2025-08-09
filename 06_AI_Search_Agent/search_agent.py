from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def query_documents(query):
    # Load FAISS index
    db = FAISS.load_local(
        "search_index",
        OpenAIEmbeddings(),
        allow_dangerous_deserialization=True
    )
    
    # Create retriever
    retriever = db.as_retriever(search_type="similarity", k=3)
    
    # Create LLM
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    
    # Create QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )
    
    return qa_chain.run(query)
