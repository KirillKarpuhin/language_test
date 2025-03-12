import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_add_to_basket_button(browser):
    # Открываем страницу товара
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")

    # Проверяем, что кнопка добавления в корзину присутствует на странице
    add_to_basket = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    add_to_basket.click()