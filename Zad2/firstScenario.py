import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options as chrom
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as edg

logger = logging.getLogger('myFirstLogger')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.info('Lets start of the test scenario')

DRIVER_NAMES = ['Chrome', 'Edge']
for driver_name in DRIVER_NAMES:
    if 'Chro' in driver_name:
        logger.info(f'Starting test with {driver_name} browser')
        chrome_options = chrom()
        driver = webdriver.Chrome(options=chrome_options)
    else:
        logger.info(f'Starting test with {driver_name} browser')
        edge_options = edg()
        driver = webdriver.Edge(options=edge_options)

    driver.get('https://pl.wikipedia.org/wiki/Wikipedia:Strona_g%C5%82%C3%B3wna')

    login_subpage_button = driver.find_element(By.ID, 'pt-login-2')
    login_subpage_button.click()

    sleep(2)

    login_input = driver.find_element(By.ID, 'wpName1')
    login_input.send_keys('krzychu@onet.pl')

    password_input = driver.find_element(By.ID, 'wpPassword1')
    password_input.send_keys('jtcnw')

    login_button = driver.find_element(By.ID, 'wpLoginAttempt')
    login_button.click()

    sleep(2)

    error_popup = driver.find_element(By.CLASS_NAME, 'cdx-message__content')
    logger.info('Site testing stopped at logging page with an error code:')
    logger.warning(error_popup.text)

    logger.info(f'End of the test firstScenario1 for {driver_name} browser')
    driver.close()