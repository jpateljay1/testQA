import unittest
from selenium import webdriver
from PageObject.Login_screen import LoginPage
from BaseTest import logger

class Welcomescreentestcase(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://stage-nlearn.nspira.in/')
        logger.info('*****Browser launched and navigated to the login page.*****')


    def test_UIelementsonWelcomescreen(self):
        logger.info('Starting test: Verifying UIelements on Welcomescreen')
        UIelements = LoginPage(self.driver)
        UIelements.narayanalogoisdisplayed()

    def test_UIelementsonWelcomescreen(self):
        logger.info('Starting test: Verifying UIelements on Welcomescreen')
        UIelements = LoginPage(self.driver)
        UIelements.narayanalogoisdisplayed()

    def test_demo(self):
        print("Demo commit")

    def test_demo1(self):
        print("Demo commit1")

    def tearDown(self):
        self.driver.quit()
        logger.info('*****Browser closed.*****')

if __name__ == "__main__":
    unittest.main()


