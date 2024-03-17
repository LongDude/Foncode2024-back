from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import filetotext


def get_chunks(database):
    doc_list = []
    splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=0)
    for chunk in splitter.split_text(database):
        doc_list.append(chunk)
    return doc_list

# Поиск релевантных отрезков с помощью faiss_retrieve
def get_message_content(topic, faiss_retriever):
    docs = faiss_retriever.get_relevant_documents(topic)
    message_content = [doc.page_content + '\n' for i, doc in enumerate(docs)]
    return message_content

# Получение embeddings
def get_embeddings(model):
    model_kwargs = {'device': 'cpu'}
    embeddings_hf = HuggingFaceEmbeddings(
        model_name=model,
        model_kwargs=model_kwargs
    )
    return embeddings_hf
def get_answer(topic,filenames,k=1):
    """
    Осуществляет поиск ответа на вопросы по лекциям

    Args:
        topic (str): Вопрос на который нужен ответ
        filenames (list(str)): Список путей до файлов с лекциями для поиска
        k (int, optional): Количество возвращаемых ответов. По умолчанию 1.

    Returns:
        list(str): Спискок полученных ответов зависит от параметра k
    """
    knowledge_base=filetotext.format_to_text(filenames)
    # Модель для embeddings
    model='intfloat/multilingual-e5-large'
    # Основной цикл
    embeddings_hf = get_embeddings(model)
    doc_list = get_chunks(knowledge_base)
    faiss_vectorstore = FAISS.from_texts(doc_list, embeddings_hf)
    faiss_retriever = faiss_vectorstore.as_retriever(search_kwargs={"k": k})

    embeddings_res = get_message_content(topic, faiss_retriever)
    return embeddings_res
if __name__=="__main__":
    topic="Блок Terminate"
    filenames=["1.md"]
    print(get_answer(topic,filenames))