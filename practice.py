import requests
import os


def translate_file(filename, save_to, language_from, language_to):
    """
    YANDEX file-translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20180215T145857Z.9922606d88c1938a.d1b8fcb18ef4343b2e8c4c1ca6ad754b06bcc14f'

    current_dir = os.path.dirname(os.path.abspath(__file__))
    filepath_from = os.path.join(current_dir, filename)

    with open(filepath_from, encoding='utf-8') as f:
        text = f.read()

    params = {
        'key': key,
        'lang': '{}-{}'.format(language_from, language_to),
        'text': text,
    }
    
    filepath_to = os.path.join(current_dir, save_to)
    response = requests.get(url, params=params).json()
    
    with open(filepath_to, encoding='utf-8', mode='w') as f:
        f.write(''.join(response['text']))


translate_file('FR.txt', 'FR-RU.txt', 'fr', 'ru')
translate_file('DE.txt', 'DE-RU.txt', 'de', 'ru')
translate_file('ES.txt', 'ES-RU.txt', 'es', 'ru')
