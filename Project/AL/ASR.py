import requests

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    """_summary_

    Args:
        filename (String): Путь к файлу или его имя

    Returns:
        String: Текст распознанный с помощью модели
    """
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()["text"]