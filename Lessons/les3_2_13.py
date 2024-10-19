import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)

        # Заполнение формы
        self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("Jon")
        self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']").send_keys("Snow")
        self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']").send_keys("jon.snow@castleblack.westeros")

        # Отправка формы
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Проверка успешной регистрации
        time.sleep(1)
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Текст не совпадает")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)

        # Заполнение формы
        self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']").send_keys("Jon")
        self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']").send_keys("Snow")
        self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']").send_keys("jon.snow@castleblack.westeros")

        # Отправка формы
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Проверка успешной регистрации
        time.sleep(1)
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Текст не совпадает")

if __name__ == "__main__":
    unittest.main()
