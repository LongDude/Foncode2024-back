import speech_recognition as sr
 
# Создаем объект распознавателя речи
recognizer = sr.Recognizer()
 
# Загружаем аудио файл
audio_file = sr.AudioFile("test.wav")
 
# Распознаем речь из аудио файла
with audio_file as source:
    audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data,language="ru-RU",show_all=True)
 
# Выводим текст
print(text['alternative'][0]['transcript'])