from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def extract_info_pdf():

    loader = PyPDFDirectoryLoader("./CVs/")
    docs = loader.load()
    
    return docs

def chunk_data(docs):

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
    texts = text_splitter.split_documents(docs)

    return texts