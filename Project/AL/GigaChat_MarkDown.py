import requests
import json
import GigaChat_token


def get_formated_text(unformated_text, GigaChat_model="GigaChat:latest"):
    """
    Отправляет POST-запрос к API чата для получения ответа моделей GigaChat/GigaChat-Pro
    - unformated_text (str): Текст, который нужно привести отформатировать в соответствии с разметкой markdown
    - GigaChat_model (str): Возможные значения поля model:
        GigaChat — базовая модель для решения более простых задач;
        GigaChat:latest — последняя версия базовой модели;
        GigaChat-Plus — модель с увеличенным контекстом. Подходит, например, для суммаризации больших документов;
        GigaChat-Pro — модель лучше следует сложным инструкциям и может выполнять более комплексные задачи.
        Значение по умолчанию GigaChat:latest
        
    Возвращает:
    - srt: Форматированный текст в виде текстовой строки
    """
    
    #Храним токен в json файле
    file=open("key.json").read()
    file=json.loads(file)
    auth_token=file["token"]
    
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    payload = json.dumps({
    "model": GigaChat_model, #Используемая модель
    "messages": [
        {
            "role": "system",
            "content": "Перепиши текст используя язык разметки markdown. Выдели основные термины, заголовки, подпункты. Используй жирный шрифт для терминов и курсив для их определений."
        },
        {
        "role": "user",
        "content": unformated_text
        }
    ],
    "temperature": 1, # Температура генерации
    "top_p": 0.1, # Контроль разнообразия ответов
    "n": 1, # Количество возвращаемых ответов
    "stream": False, # Потоковая передача ответов
    "max_tokens": len(unformated_text)//2, # Максимальное кол-во токенов в ответе
    "repetition_penalty": 1 #Штраф за повторения
    })
    token=GigaChat_token.get_token(auth_token)
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json', # Принимаем ответ в формате JSON
    'Authorization': f'Bearer {token}' # Токен авторизации
    }
    # Запрос на получение форматированного текста
    response = requests.request("POST", url, headers=headers, data=payload,verify=False)
    if response.status_code==200:
        return response.json()['choices'][0]['message']['content']
    else:
        return response.text