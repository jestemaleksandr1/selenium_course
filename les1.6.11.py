from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import tkinter as tk
from tkinter import messagebox

def show_error_message(message):
    root = tk.Tk()
    root.withdraw()  # Скрыть главное окно
    messagebox.showerror("Опять кодеры сделали что-то не то!", message)
    root.destroy()

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Проверяем наличие плейсхолдера Имени
    try:
        first_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
        first_name.send_keys("Jon")
    except NoSuchElementException:
        try:
            first_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your name']")
            first_name.send_keys("Jon")
        except NoSuchElementException:
            error_message = "NoSuchElementException: Поле 'First name' не найдено"
            print(error_message)
            show_error_message(error_message)
            raise

    # Проверяем наличие плейсхолдера Фамилии
    try:
        last_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
        last_name.send_keys("Snow")
    except NoSuchElementException:
        error_message = "NoSuchElementException: Поле 'Last name' не найдено"
        print(error_message)
        show_error_message(error_message)
        raise

    # Проверяем наличие плейсхолдера электронной почты
    try:
        email = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
        email.send_keys("jon.snow@castleblack.westeros")
    except NoSuchElementException:
        error_message = "NoSuchElementException: Поле 'Email' не найдено"
        print(error_message)
        show_error_message(error_message)
        raise

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
