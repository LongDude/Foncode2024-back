import requests
import json

def query(filename):
    """_summary_

    Args:
        filename (String): Путь к файлу или его имя

    Returns:
        String: Текст распознанный с помощью модели
    """
    
    #Храним токен в json файле
    file=open("key.json").read()
    file=json.loads(file)
    auth_token=file["hugging_face"]
    
    headers = {"Authorization": f"Bearer {auth_token}"}
    API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()["text"]
if __name__=="__main__":
    print(query(""))