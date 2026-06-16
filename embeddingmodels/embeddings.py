from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name = 'sentence-transformers/all-MiniLM-L6-v2'

)
texts = [
    "Hello this is Ansh Bhardwaj",
    "Hello your name is Coder",
    "And you are all very beautiful"
]
vector = embeddings.embed_documents(texts)
print(vector)