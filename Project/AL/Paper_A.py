from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings


def get_chunks(database):
    doc_list = []
    splitter = CharacterTextSplitter(separator="\n", chunk_size=500, chunk_overlap=0)
    for chunk in splitter.split_text(database):
        doc_list.append(chunk)

    chunk_num = len(doc_list)

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
def get_answer(topic,knowledge_base,k=1):
    # Модель для embeddings
    model='intfloat/multilingual-e5-large'
    # Основной цикл
    embeddings_hf = get_embeddings(model)
    doc_list = get_chunks(knowledge_base)

    embeddings_hf = get_embeddings(model)
    faiss_vectorstore = FAISS.from_texts(doc_list, embeddings_hf)
    faiss_retriever = faiss_vectorstore.as_retriever(search_kwargs={"k": k})

    embeddings_res = get_message_content(topic, faiss_retriever)
    return embeddings_res
if __name__=="__main__":
    topic="Блок Seize"
    knowledge_base="""
    Блок Generate предназначен для внесения в модель транзактов которые соответствует некоторым заявкам на обслуживание в моделируемой системе. Например запросы к серверу.
    Имеются параметры 
    A -  среднее значение интервала времени
    B – разброс или модификатор среднего значения(по умолчанию ноль)
    C – время появления первого транзакта (по умолчанию определяется законом распределения)
    D – общее число генерируемых транзактов (для ограничения заявок, по умолчанию бесконечность)
    E – уровень приоритета каждого транзакта( заявки на обслуживание могут иметь разный приоритет 0-127, значение по умолчанию 0)
    F – Число параметров (по умолчанию 12 к каждому транзакту приписываются параметры)
    G – тип параметра( F – полнослованый, H – полусловный по умолчанию)
    Модель начинается с блока Generate
        Блок Terminate
    Формат Termi[nate] A
    A – величина, вычитаемая из содержимого счетчика завершений( поле А карты start)
    Предназначен для удаления транзактов из модели. Когда счетчик старт окажется равен 0, то происходит завершение работы модели. 
    Система массового обслуживания - некоторая система из которого вытекают требования и должны быть обслужены.
    Блоки ограничивающие прибор. Как только транзакт движущийся по модели дойдет до блока seize он захватывает устройтсво
    Seize A
    A – имя устройства занимаемого транзактом
    Release A
    A – имя устройства освобождаемого транзактом
    Если устройство быо захвачено транзактом, то все следующие транзакты подходящие к блоку seize задерживаются в очереди перед устройством, ожидая, когда оно освободится. Устройство освобождается когда транзакт проходит чере з release.
    Advance – задержка перемещения транзакта. Предполагется что транзакт через любой блок за 0 время в gpss.
    Advance A,[B]
    B может быть опущено
    A – среднее время задержки транзакта в блоке , значение – число, СЧА
    B – модификатор задающий разброс времени задержки. Два типа модификаторов – модификатор интервал задающий закон распредения времени задержки. При вычисении разности значений, заданных в А и В получается нижняя граница, а при сложении верхняя. При использовании модификатор функции время задержки определяется как прозведение операнда занчения A и значения функции в парамтре B,
    Составим модель
    Имеется магазин куда приходят покупатели
    1 Приход [2, 10](единицы времени)
    2 Продавец [2, 8]
    Generate 6,4
    Seize
    Advance 5,3
    Release
    Terminate
    1 Приход [2, 10](единицы времени)
    2 Продавец [2, 8]
    3 Кассир [1,3]
    4 Выдача товара [1, 3]
    Generate 6,4
    Seize pok \\ Покупатель идет к продавцу
    Advance 5,3
    Release pok
    Seize kass \\Покупатель идет к кассиру
    Advance 2 1
    Release kass
    Seize prod \\Покупатель на выдачу
    Advance 2 1
    Release prod
    Terminate
    Лекция 2
    Queue – очередь, блок для сбора статистики, ограничивает участок модели, где собирается статистика,
    Queue A,B
    A – номер очереди (числовое или символьное имя очереди)
    B – Число добавляемых в очередь элементов (по умолчанию 1)
    Depart – блок для сбора статистики, ограничивает участок модели, где собирается статистика
    A – номер очереди
    B – Число удаляемых из очереди элементов
    Использование различных 3РСВ
    Стандартные функции 24шт
    EXPONENTIAL(A,B,C),POISSON(A,B),…
    GENERATE (EXPONENTIAL(1,10,0))
    ADVANCE(POISSON(1,12))
    A-датчик
    С помощью B задаются параметры распределения
    POISSON – закон распределения Пуассона
    Создание пользовательских функций
    Name FUNCTION A,B
    Name – имя функции
    A- аргумент функции RN(1-8)(какой датчик используется для генерации случайных величин)
    B – состоит из данной буквы, определяющий тип функции0 и целого положительного числа, задающего количество пар возможных значений аргумента т функции
    С- непрерывная числовая
    D – дискретная величина
    Создание пользовательских функций 
    Rasp FUNCTIO RN6,5
    .15,2/.35,5/.6,8/.82,9/1,12
    Fun FUNCTION R1,C10
    0,a/y1,x1/…/1,xn
    Генерируется случайное значение от 0 1 ищется значение и определяется значение, которое выдается (происходит линейная интерполяции функции распределения)
    """
    print(get_answer(topic,knowledge_base))