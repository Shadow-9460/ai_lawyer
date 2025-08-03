from langchain_groq import ChatGroq
from vector_database import faiss_db
from langchain_core.prompts import ChatPromptTemplate
import os
os.environ["GROQ_API_KEY"] = Groq_Api_Key

# llm_model = ChatGroq(model="deepseek-r1-distill-llama-70")
llm_model = ChatGroq(model="llama3-70b-8192")



def retrieve_docs(query):
    return faiss_db.similarity_search(query)

def get_context(documents):
    context = "\n\n".join(doc.page_content for doc in documents)
    return context

custom_prompt_template = """sumary_line

Question: {question}
Context: {context}
Answer:
"""
def answer_query(documents,model,query):
    context =  get_context(documents)
    prompt = ChatPromptTemplate.from_template(custom_prompt_template)
    chain =  prompt | model
    return chain.invoke({"question":query,"context":context})


question="If government forbid the right to assemble peacefully which article get violated"
retrieved_docs = retrieve_docs(question)
print("AI Lawyer:",answer_query(documents=retrieved_docs,model=llm_model,query=question))

