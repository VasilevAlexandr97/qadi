from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Es
from os import path
import time

@given('website "{url}"')
def step(context, url):
    context.browser = webdriver.Chrome(
        executable_path=path.abspath('chromedriver')
    )
    context.browser.get(url)

# переходим по ссылке с текстом
@then('click link with text "{text}"')
def step(context, text):
    link = context.browser.find_element_by_link_text(text)
    link.click()

# Проверяем правильность адреса в контактах
@then('page include text in contacts "{text}"')
def step(context, text):
    elements = context.browser.find_elements_by_css_selector('span.font-full-black')

    for element in elements:
        if element.location['x'] != 0 and element.location['y'] != 0:
            text = element.text.replace('\n', '').replace('оф.', ', офис ')
            assert 'ул. Малышева, 51, офис 1619' in text

# Проверяем правильность адресса в подвале страницы
@then('page include text in footer address "{text}"')
def step(context, text):
    el = context.browser.find_element_by_xpath("//a[@href='/contacts?ekaterinburg']")
    text_link = el.get_attribute('innerHTML').replace('\n', '').lstrip()
    assert text in text_link

# Проверяем скачивается ли файл о политике безопасности на странице О компании
@then('download file')
def step(context):
    link = context.browser.find_element_by_link_text('Политика в отношении обработки персональных данных ООО "ДартИТ"')
    link.click()
    time.sleep(5)
    assert path.isfile(path.abspath('Politika_v_otnoshenii_obrabotki_personalnyih_dannyih_OOO__DartIT.docx'))