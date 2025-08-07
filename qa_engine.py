from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma  # or FAISS

def get_text_chunks(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.split_text(text)

def create_vector_store(chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_texts(chunks, embedding=embeddings)  # or use FAISS
    return vectorstore

def get_qa_chain(vectorstore):
    from langchain.chains import RetrievalQA
    from langchain.chat_models import ChatOpenAI
    llm = ChatOpenAI(model="gpt-4")
    return RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())
