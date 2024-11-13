from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from langchain.chains import RetrievalQA

class RAGPipeline:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings("sentence-transformers/all-MiniLM-L6-v2")
        self.retriever = FAISS(self.embeddings)
        self.tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
        self.rag_chain = RetrievalQA(retriever=self.retriever, llm=self.model)

    def retrieve_and_generate(self, query):
        return self.rag_chain({"query": query})