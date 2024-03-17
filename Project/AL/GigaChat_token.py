import requests
import uuid
import json

def get_token(auth_token,scope='GIGACHAT_API_PERS'):
    """
    Параметры:
        auth_token (str): Авторизационные данные из Client Secret
        scope (str, optional): Используемый тип API(Для юр. лиц и для физ. лиц). По умолчанию для физ. лиц - 'GIGACHAT_API_PERS'.

    Возврат:
        str: Токен, который можно использовать в течении 30 минут для запросов
    """
    #Создание идентификатора
    rq_uid=str(uuid.uuid4())
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

    payload={'scope':scope
             }
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'RqUID': rq_uid,
    'Authorization': f'Basic {auth_token}'
    }
    # Отправляем пост запрос для получения токена
    response = requests.request("POST", url, headers=headers, data=payload,verify=False)
    if response.status_code==200:
        return response.json()['access_token']
    else:
        return response.text

if __name__=="__main__":
    
    file=open("key.json").read()
    file=json.loads(file)
    auth_token=file["token"]
    print(get_token(auth_token))