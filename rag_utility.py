import os
from dotenv import load_dotenv
from langchain_unstructured import UnstructuredLoader
#from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQA

#load environment variables
load_dotenv()

working_dir = os.path.dirname(os.path.abspath(__file__))

#Load embedding model
embedding = HuggingFaceEmbeddings()

#Load LLM
llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    temperature = 0.0
)

def process_document_to_chroma_db(file_name):
    #load pdf using UnstructuredPDFLoader
    loader = UnstructuredLoader(f"{working_dir}/{file_name}")
    documents = loader.load()
    #split text into chunks for embedding
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200
    )
    texts = text_splitter.split_documents(documents)
    #Store document chunks in Chroma vector db
    vectordb = Chroma.from_documents(
        documents=texts,
        embedding=embedding,
        persist_directory=f"{working_dir}/doc_vectorstore"
    )
    return 0

def answer_question(user_question):
    #Load persistent Chroma vector db
    vectordb = Chroma(
        persist_directory=f"{working_dir}/doc_vectorstore",
        embedding_function=embedding
    )
    #Create retriever for doc search
    retriever = vectordb.as_retriever()

    #Create a Retriever chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever
    )
    response = qa_chain.invoke({"query": user_question})
    answer = response["result"]

    return answer