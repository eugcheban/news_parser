from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime

import time

from dolp import Dolphin

class Driver():
    def __init__(self, port):
        self.port = port
        self.driver = self._createDriver()

    def _createDriver(self):
        profile_port = self.port
        # Настройка WebDriver для работы с профилем Dolphin Anty
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{profile_port}")

        # Инициализация WebDriver с использованием ChromeDriverManager
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        return driver

    def goToPage(self, url):
        try:
            # Переход на сайт google.com
            self.driver.get(url)

            # Ожидание загрузки страницы
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            # Получение содержимого страницы
            page_content = self.driver.page_source
            #print(page_content)
            return str(page_content)
        except Exception as e:
            print(f"Ошибка в функции goToPage: {e}")

    def close_driver(self):
        try:
            self.driver.quit()
        except Exception as e:
            print(f"Error while closing driver {e}")

    def save_page(self):
        try:
            with open(f'result_34', 'wb') as f:
                f.write(self.driver.page_source.encode())
        except Exception as e:
            print(f"Error while saving source_page {e}")

def get_page(port):
    # Использование информации о запущенном профиле
    profile_port = port

    # Настройка WebDriver для работы с профилем Dolphin Anty
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{profile_port}")

    # Инициализация WebDriver с использованием ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Переход на сайт google.com
        driver.get('https://www.google.com')

        # Ожидание загрузки страницы
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )

        # Получение содержимого страницы
        page_content = driver.page_source
        print(page_content)
        return page_content
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        # Закрытие браузера
        driver.quit()

if __name__ == "__main__":
    # Запуск профиля и получение страницы
    dolp = Dolphin()
    dolp.run_profile()
    automation_params = dolp.automation
    #time.sleep(5)
    #get_page(automation_response['port'])

    dr = Driver(automation_params['port'])
    #dr.goToPage('https://www.google.com/search?q=Deutsche+Bank+AG&tbm=nws&hl=en&num=2')
    dr.goToPage('https://www.db.com/news/detail/20240731-deutsche-bank-launches-basf-s-first-sustainability-linked-payables-finance-program-in-asia?language_id=1')
    dr.save_page()
    dr.close_driver()
    dolp.stop_profile()