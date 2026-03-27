import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA

class RAGClient:
    def __init__(self, pdf_folder="app/model/data"):
        self.pdf_folder = pdf_folder
        self.loader = PyPDFLoader(os.path.join(pdf_folder, "your_documents.pdf"))
        self.docs = self.loader.load()
        
        self.embeddings = OpenAIEmbeddings()  # or any embedding provider
        self.vectorstore = FAISS.from_documents(self.docs, self.embeddings)
        self.retriever = self.vectorstore.as_retriever()
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=None,  # You can pass OpenAI or Groq LLM here later
            retriever=self.retriever
        )

    def ask(self, question):
        try:
            return self.qa_chain.run(question)
        except Exception as e:
            return f"RAG error: {e}"