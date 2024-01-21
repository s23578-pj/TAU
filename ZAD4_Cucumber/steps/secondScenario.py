from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

import logging

logger = logging.getLogger('mySecondlogger')
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)

driver = None

@given('I open the website "{url}" using "{browser}" browser')
def open_website(context, url, browser):
    print(browser)
    global driver
    options = ChromeOptions() if 'chrome' in browser.lower() else EdgeOptions()
    context.driver = webdriver.Chrome(options=options) if 'chrome' in browser.lower() else webdriver.Edge(options=options)
    context.driver.get(url)

@when('I click on accept cookies button')
def click_accept_cookies_button(context):
    context.driver.find_element(By.CSS_SELECTOR, '.btn.btn-red.js__accept-all-consents').click()

@when('I hover specific product dropdown menu')
def hover_dropdown_menu(context):
    element_to_hover_over = context.driver.find_elements(By.ID, 'headlink23')
    actions = ActionChains(context.driver)
    actions.move_to_element(element_to_hover_over[2]).perform()

@when('I click specific pannel')
def click_anime_subpage(context):
    context.driver.find_element(By.CLASS_NAME, 'productname')

@then('I should be on the correct subpage')
def check_current_page(context):
    current_url = context.driver.current_url
    expected_url = 'https://wkdzik.pl/'

    if current_url == expected_url:
        logger.info(f'Correct transfer to subpage = {current_url}')
    else:
        logger.info(f'Incorrect transfer to subpage. You should be on {expected_url}')
