from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

def initialize_OpenAI(OPEN_AI_KEY):

    # Initialize the OpenAI language model and load the question-answering chain
    llm = OpenAI(temperature=0, openai_api_key=OPEN_AI_KEY)
    chain = load_qa_chain(llm, chain_type="stuff")

    return chain

def questions(docsearch, chain, query):
    
    #query = "Cuales son las habilidades de james bond?"
    docs = docsearch.similarity_search(query)
    answer = chain.run(input_documents=docs, question=query)

    return answer