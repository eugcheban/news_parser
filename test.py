from pywebcopy import save_webpage

# URL страницы, которую вы хотите сохранить
url = 'https://www.google.com'

# Папка, куда будет сохранена страница
download_folder = '/'  # Замените на путь к вашей папке

# Настройки для сохранения веб-страницы
kwargs = {
    'project_name': 'google_page',
    'bypass_robots': True,  # Игнорировать правила robots.txt
    'open_in_browser': False,  # Не открывать в браузере после сохранения
}

# Сохранение страницы
save_webpage(url, download_folder, **kwargs)

print("Страница сохранена успешно!")
