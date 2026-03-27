import os
import streamlit as st
from rag_utility import process_document_to_chroma_db, answer_question

#set working dir
working_dir = os.getcwd()

st.title("🦙 InsightRAG ")

#file uploader widget
uploaded_file = st.file_uploader("Upload a pdf file", type=["pdf"])

if uploaded_file is not None:
    #define save path
    save_path = os.path.join(working_dir, uploaded_file.name)
    #save file
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    process_document = process_document_to_chroma_db(uploaded_file.name)
    st.info("document Processed Successfully")

#text widget to get user inpput
user_question = st.text_area("Ask your question about the document")

if st.button("Answer"):
    answer = answer_question(user_question)

    st.markdown("### Here is your answer: ")
    st.markdown(answer)




