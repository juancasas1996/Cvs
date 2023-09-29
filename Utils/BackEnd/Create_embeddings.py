from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import pinecone

# # Api keys from pinecone and openai
# PINECONE_API_KEY ="dabe371f-52da-49c6-ba8e-cdcbdc664b5c"
# OPEN_AI_KEY ="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"

def create_embeddings(OPEN_AI_KEY):

    # Initialize OpenAI embeddings using the provided API key from environment variables
    embeddings = OpenAIEmbeddings(openai_api_key=OPEN_AI_KEY)
    
    return embeddings

def save_embeddings(embeddings, texts, PINECONE_API_KEY):
    # initialize pinecone
    pinecone.init(
        api_key=PINECONE_API_KEY,  
        environment='gcp-starter' 
    )
    index_name = "langchaintest"
    if index_name not in pinecone.list_indexes():
        # Create the index if it does not exist
        pinecone.create_index(index_name, dimension=1536)
    # Connect to abstractive-question-answering index we created
    index = pinecone.Index(index_name)

    # Generate and save embeddings in pinecone
    docsearch = Pinecone.from_texts([t.page_content for t in texts], embeddings, index_name=index_name)

    return docsearch