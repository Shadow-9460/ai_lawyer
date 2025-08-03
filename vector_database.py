from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

pdfs_directory = 'pdfs/'

# Step 1: Upload and Load Raw pdf 
# Step 2 : Create a chunks 
# Steps 3 : Setup a embedding models 
# Step 4: Index Documents ** Store in Faiss (Vector Store )



def upload_pdf(file):
    with open(pdfs_directory+file.name,'wb') as f:
        f.write(file.getbuffer())

def load_pdf(file_path):
    loader = PDFPlumberLoader(file_path)
    documents = loader.load()
    return documents

file_path = 'pdfs/United Nations Universal Declaration of Human Rights 1948.pdf'
documents = load_pdf(file_path)

def create_chunks(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size =  1000,
        chunk_overlap = 200,
        add_start_index = True
    )
    text_chunks = text_splitter.split_documents(documents)
    return text_chunks
text_chunks = create_chunks(documents)
print("Chunks count: ",len(text_chunks))

# Step 3 :Setup Embedding Model (USe Deepseek R1 with Ollama)
ollama_model_name = "deepseek-r1:1.5b"
def get_embedding_model(ollama_model_name):
    embeddings = OllamaEmbeddings(model=ollama_model_name)
    return embeddings

#Step 4 : Index Documents **Store Embedding in Faiss (Vector Store)
Faiss_DB_Path= "vectorstore/db_faiss"
faiss_db = FAISS.from_documents(text_chunks,get_embedding_model(ollama_model_name))
faiss_db.save_local(Faiss_DB_Path)



# print(len(documents))