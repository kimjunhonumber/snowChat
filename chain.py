from langchain.vectorstores import Chroma
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain, ChatVectorDBChain
# from langchain.document_loaders import DirectoryLoader
# from langchain.vectorstores import FAISS
from langchain.prompts.prompt import PromptTemplate
# from langchain.chat_models import ChatOpenAI

TEMPLATE = """ You're name is snowchat, and you are a senior snowflake developer. You are currently working in a snowflake database. You have to write a sql code in snowflake database based on the following question. Also you have to ignore the sql keywords and the context and give a one or two sentences about how did you arrive at that sql code. Be a little bit creative and humorous.
If you don't know the answer, just say "Hmm, I'm not sure. I am trained only to answer sql related queries. Please try again." Don't try to make up an answer.
Use snowflake database documentation https://docs.snowflake.com/sql-reference-commands for writing sql code.

Question: {question}
{context}
Answer:"""
QA_PROMPT = PromptTemplate(template=TEMPLATE, input_variables=["question", "context"])


def get_chain(vectorstore):
    """
    Get a chain for chatting with a vector database.
    """
    llm = ChatOpenAI(model_name='gpt-4', temperature=0.2)
    chat_vector_db_chain = ChatVectorDBChain.from_llm(llm=llm, vectorstore=vectorstore, qa_prompt=QA_PROMPT, verbose=True)
    
    return chat_vector_db_chain
