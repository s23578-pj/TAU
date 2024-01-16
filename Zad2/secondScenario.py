import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options as chrom
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as edg

logger = logging.getLogger('mySecondlogger')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.info('Lets Start of the test scenario')

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

    driver.get('https://wkdzik.pl/')
    sleep(1)
    accept_cookies= driver.find_element(By.CSS_SELECTOR, '.btn.btn-red.js__accept-all-consents')
    accept_cookies.click()

    element = driver.find_element(By.ID, 'headlink23')
    element.click()
    logger.info("Transfer to subpage for details")

    element = driver.find_element(By.CLASS_NAME, 'productname')
    element.click()

    current_url = driver.current_url
    expected_url = 'https://wkdzik.pl/suplementy-i-odzywianie'

    if current_url == expected_url:
        logger.info(f'Correct transfer to the appropriate subpage = {current_url}')
    else:
        logger.info(f'Incorrect transfer to the appropriate subpage. Correct URL = {expected_url}')

    logger.info(f'End of the test secondScenario for {driver_name} browser')
    driver.close()