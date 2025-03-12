import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_add_to_basket_button(browser):
    # Открываем страницу товара
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(15)

    # Проверяем, что кнопка добавления в корзину присутствует на странице
    add_to_basket_button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(add_to_basket_button) > 0, "Кнопка добавления в корзину не найдена"

    print("Кнопка добавления в корзину найдена!")

    # запуск происходит pytest --language=es --browser_name=chrome -s -v test_items.py