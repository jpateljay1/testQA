from selenium.webdriver.common.by import By
from Testcases.BaseTest import logger
import logging

class LoginPage:
    Narayana_logo_XPATH = "(//img[@alt='naryana-logo'])[2]"

    def __init__(self, driver):
        self.driver = driver

    def narayanalogoisdisplayed(self):
        Narayana_logo = self.driver.find_element(By.XPATH, self.Narayana_logo_XPATH)
        try:
            if Narayana_logo.is_displayed():
                print('Narayana logo is displayed on the Login page')
                logger.info('*****Narayana logo is displayed on the Login page.*****')
            else:
                print('Narayana logo is not displayed on the Login page')
                logger.error('*****Narayana logo is not displayed on the Login page.*****')
                assert False  # This should be assert False to indicate test failure

        except Exception as e:
            logger.error(f'An error occurred: {e}')
            assert False
