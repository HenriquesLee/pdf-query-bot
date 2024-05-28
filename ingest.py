from langchain.document_loaders import PyPDFLoader, DirectoryLoader, PDFMinerLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
import os

persist_directory = "db"

def main():
    # List of PDF files
    pdf_files = [
        "/content/OSIT_SOP.pdf"
        # Add more PDF files as needed
    ]

    # Initialize an empty list to store all documents
    all_documents = []

    # Iterate over each PDF file
    for pdf_file in pdf_files:
        print(pdf_file)
        loader = PyPDFLoader(pdf_file)
        documents = loader.load()
        all_documents.extend(documents)

    print("splitting into chunks")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    texts = text_splitter.split_documents(all_documents)

    print("Loading sentence transformers model")
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    print(f"Creating embeddings. May take some minutes...")
    db = Chroma.from_documents(texts, embeddings, persist_directory=persist_directory)
    db.persist()
    db = None

    print("Ingestion complete! You can now run privateGPT.py to query your documents")

if __name__ == "__main__":
    main()
