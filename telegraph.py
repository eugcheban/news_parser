import os
from typing import Optional
import requests

class Telegraph:
    def __init__(self, access_token: Optional[str] = os.environ.get('TELEGRA_API', None)):
        self.access_token = access_token
        self.api_url = 'https://api.telegra.ph'

    def create_page(self, title, author_name, content):
        url = f'{self.api_url}/createPage'
        data = {
            'access_token': self.access_token,
            'title': title,
            'author_name': author_name,
            'content': content,
            'return_content': True
        }
        response = requests.post(url, json=data)
        return response.json()

def generate_content():
    return [
        {"tag": "h3", "children": ["Заголовок статьи"]},
        {"tag": "p", "children": ["Это примерный абзац текста."]},
        {"tag": "b", "children": ["Жирный текст"]},
        {"tag": "i", "children": ["Курсивный текст"]},
        {"tag": "a", "attrs": {"href": "https://example.com"}, "children": ["Ссылка"]},
        {"tag": "img", "attrs": {"src": "https://example.com/image.jpg"}},
        {"tag": "ul", "children": [
            {"tag": "li", "children": ["Элемент списка 1"]},
            {"tag": "li", "children": ["Элемент списка 2"]}
        ]}
    ]

if __name__ == "__main__":
    
    telegraph = Telegraph()

    title = "Пример статьи"
    author_name = "Автор"

    content = generate_content()

    response = telegraph.create_page(title, author_name, content)
    print(response)
