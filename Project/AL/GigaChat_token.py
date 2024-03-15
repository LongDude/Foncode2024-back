import requests
import uuid



def get_token(auth_token,scope='GIGACHAT_API_PERS'):
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

    response = requests.request("POST", url, headers=headers, data=payload,verify=False)
    return response.json()['access_token']