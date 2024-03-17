import torch
import GigaChat_MarkDown
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

def query(filename,GigaChat_model="GigaChat:latest"):
    """
    Возвращает текст из аудио
    
    Args:
        filename (str): Путь к файлу или его имя, файлы любой длинны
        GigaChat_model (str): Возможные значения поля model:
        GigaChat — базовая модель для решения более простых задач;
        GigaChat:latest — последняя версия базовой модели;
        GigaChat-Plus — модель с увеличенным контекстом. Подходит, например, для суммаризации больших документов;
        GigaChat-Pro — модель лучше следует сложным инструкциям и может выполнять более комплексные задачи.
        Значение по умолчанию GigaChat:latest
        
    Returns:
        str: Текст распознанный с помощью модели
    """
    # Используем видеокарту, если поддерживается, иначе процессор
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    # Используемая модель для распознавания
    model_id = "openai/whisper-large-v3"

    # Инициализируем параметры модели
    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
    )
    model.to(device)

    processor = AutoProcessor.from_pretrained(model_id)

    # Инициализируем параметры распознавания
    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        max_new_tokens=10000,
        chunk_length_s=30,
        batch_size=16, 
        return_timestamps=True,
        torch_dtype=torch_dtype,
        device=device,
    )
    # Делаем запрос на рапознавание
    response = pipe(filename,generate_kwargs={"language": "Russian"})
    # Форматируем текст при помощи нейросети
    formated_text=GigaChat_MarkDown.get_formated_text(response["text"],GigaChat_model=GigaChat_model)
    return formated_text
if __name__ =="__main__":
    print(query("test.mp3"))