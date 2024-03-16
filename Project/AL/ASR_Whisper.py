import requests
import json
import GigaChat_MarkDown

def query(filename):
    """
    Args:
        filename (Str): Путь к файлу или его имя, файлы длинной около 30 секунд

    Returns:
        String: Текст распознанный с помощью модели
    """
    
    #Храним токен в json файле
    file=open("key.json").read()
    file=json.loads(file)
    auth_token=file["hugging_face"]
    
    headers = {"Authorization": f"Bearer {auth_token}"}
    API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
    #Считываем аудио файл и отправляем его на распознаванием с помощью пост запроса
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    #Форматируем текст при помощи нейросети
    formated_text=GigaChat_MarkDown.get_formated_text(response.json()["text"])
    return formated_text

if __name__=="__main__":
    print(query("test.mp3"))