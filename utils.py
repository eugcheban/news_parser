from urllib.parse import urlparse

def get_domain(url):
    # Парсинг URL
    parsed_url = urlparse(url)
    
    # Получение домена без префиксов www и т.д.
    domain = parsed_url.netloc
    
    # Удаление префикса "www." если он есть
    if domain.startswith('www.'):
        domain = domain[4:]
    
    return domain