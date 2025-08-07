import streamlit as st
from utils import extract_text_from_pdf, extract_text_from_docx
from qa_engine import get_text_chunks, create_vector_store, get_qa_chain

st.title("📄 Document-based Q&A System")

uploaded_file = st.file_uploader("Upload a PDF or Word document", type=["pdf", "docx"])
if uploaded_file:
    if uploaded_file.name.endswith(".pdf"):
        text = extract_text_from_pdf(uploaded_file)
    else:
        text = extract_text_from_docx(uploaded_file)

    with st.spinner("Processing..."):
        chunks = get_text_chunks(text)
        vectorstore = create_vector_store(chunks)
        qa_chain = get_qa_chain(vectorstore)

    query = st.text_input("Ask a question based on the document:")
    if query:
        response = qa_chain.run(query)
        st.markdown("### 📌 Answer:")
        st.write(response)
        st.set_page_config(
    page_title="Doc Q&A System",
    page_icon="📄"
)

st.image("logo.png", width=120)  # Put logo.png in root of your GitHub repo
st.title("📄 Document-based Question Answering System")


