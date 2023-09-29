from Utils.FrontEnd.Front import *
from Utils.BackEnd.Create_embeddings import *
from Utils.BackEnd.Extract_info import *
from Utils.BackEnd.QnA import *
import streamlit as st


st.set_page_config(layout="wide", page_icon="🧾", page_title="CV Intelligent Search")


with st.sidebar:
    fmarkdown(1, "White", "OpenAI Key")

    OpenAI_Key = st.text_input('Put your OpenAI key with some credits',)

    fmarkdown(1, "White", "Pinecone Key")

    Pinecone_Key = st.text_input('Put your Pinecone key with some credits',)


fmarkdown(1, "White", "CV Intelligent Search")

fmarkdown(2, "#6495ED", "Write a query to search in the saved CV")

fmarkdown(5, "#6495ED", "For example: what are the skills of (any candidate of the saved cv)")

query = st.text_input('','what are the skills of Sebastian Casas')

docs = extract_info_pdf()
texts = chunk_data(docs=docs)

