from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Driver():
    def __init__(self):
        self.driver = self._createDriver()

    def _createDriver(self):
        # Настройка WebDriver для работы с Chrome
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--headless")  # Уберите это, если хотите видеть браузер

        # Инициализация WebDriver с использованием ChromeDriverManager
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        return driver

    def goToPage(self, url):
        try:
            # Переход на указанный сайт
            self.driver.get(url)

            # Ожидание загрузки страницы
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            # Получение содержимого страницы
            page_content = self.driver.page_source
            return str(page_content)
        except Exception as e:
            print(f"Ошибка в функции goToPage({url}): {e}")

    def close_driver(self):
        try:
            self.driver.quit()
        except Exception as e:
            print(f"Error while closing driver {e}")

    def save_page(self, filename):
        try:
            with open(filename, 'wb') as f:
                f.write(self.driver.page_source.encode())
        except Exception as e:
            print(f"Error while saving source_page {e}")

def main():
    dr = Driver()
    url = 'https://www.db.com/news/detail/20240731-deutsche-bank-launches-basf-s-first-sustainability-linked-payables-finance-program-in-asia?language_id=1'
    content = dr.goToPage(url)
    if content:
        dr.save_page('result_34.html')
    dr.close_driver()

if __name__ == "__main__":
    main()
