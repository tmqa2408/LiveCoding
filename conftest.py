import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Убери, если нужен UI
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--log-level=3")  # Для минимизации вывода

    # Принудительно указываем путь к chromedriver
    chromedriver_path = ChromeDriverManager().install()
    service = Service(chromedriver_path)

    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()