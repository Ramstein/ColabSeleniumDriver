import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time, datetime, copy

from keyboard import press
import pyautogui, pyperclip

user = 'makrovh@gmail.com'
pwd  = 'nadiufgbua'
scriptPath = r'C:\Users\Ramstein\PycharmProjects\ColabDriver\Checking.py'
file_name = scriptPath.split("\\")[-1].split('.')[0]
colabInstanceName = f"{datetime.datetime.now():%m-%d-%Hh%Mm%Ss}"+file_name

class ColabDriver(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome(driverpath)
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver

        '''open gmail page'''
        driver.get("https://www.gmail.com")

        '''Enter username and password'''
        element = driver.find_element_by_id('identifierId')
        element.send_keys(user)

        driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()
        time.sleep(2)

        '''Enter password'''
        element = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        element.send_keys(pwd)

        '''press submit button for login'''
        driver.find_element_by_xpath('//*[@id="passwordNext"]/span').click()
        try:
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id=":2a"]'))
            )
            print("Logged in.")
        except ConnectionError as e:
            print("Network connectivity error.", e)
        except:
            print("Additional authentication required.")

        '''initialising colab notebook'''
        driver.get("https://colab.research.google.com")
        try:
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/colab-dialog/paper-dialog/div/a/paper-button'))
            )
            driver.find_element_by_xpath('/html/body/colab-dialog/paper-dialog/div/a/paper-button').click()
        except ConnectionError as e:
            print("New python3 notebook: ", e)

        try:
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="doc-name"]'))
            )
        except ConnectionError as e:    # This is the correct syntax
            print(e)
        '''renaming the colab instance'''
        element = driver.find_element_by_xpath('//*[@id="doc-name"]')
        element.click()
        element.clear()  #renaming the colab instance
        time.sleep(0.5)
        element.send_keys(colabInstanceName+".ipynb")
        time.sleep(0.5)
        pyautogui.press('enter')
        print("colab instance name: "+colabInstanceName+'.ipynb')
        time.sleep(0.5)
        '''initiliasing gpu runtime'''
        element = driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[5]/div/div/div[1]').click()
        element = driver.find_element_by_xpath('/html/body/div[12]/div[12]/div').click()
        element = driver.find_element_by_xpath('/html/body/colab-dialog/paper-dialog/paper-dialog-scrollable/div/div/p[2]'
                                                '/paper-dropdown-menu/paper-menu-button/div/div/paper-input/paper-input-container/div[2]/div/iron-input/input').click()
        time.sleep(0.5)
        pyautogui.press('down')
        time.sleep(1.5)
        pyautogui.press('enter')
        time.sleep(1)

        element = driver.find_element_by_xpath('//*[@id="ok"]').click()
        element = driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[2]/'
                                               'colab-connect-button/colab-toolbar-button[1]/paper-button').click()

        print("GPU runtime initialised.")

        # ColabDriver.pasteData(self, driver=driver)
        ColabDriver.runScript(self, driver=driver)

        # elem.send_keys(Keys.RETURN)
        # assert "No results found." not in driver.page_source
    def pasteData(self, driver):
        element = driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[1]/colab-shaded-scroller/div/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div[6]/div[1]/div/div/div/div[5]/div/pre')

        element.click()
        with open(scriptPath) as f:

            lines = f.readlines()
            for line in lines:
                pyperclip.copy(line)
                pyautogui.hotkey('ctrl', 'v')

    def runScript(self, driver):
        CtrlEnter = '/html/body/div[7]/div[2]/div[1]/colab-shaded-scroller/div/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div/div[2]/paper-icon-button'

        element = driver.find_element_by_xpath(CtrlEnter).click()
        #clicking on the google drive authentication link
        following_link_xpath = '/html/body/div/span[2]/pre'


        # try:
        #     element = WebDriverWait(driver, 50).until(
        #         EC.presence_of_element_located((By.XPATH, following_link_xpath))
        #     )
        # except ConnectionError as e:    # This is the correct syntax
        #     print(e)
        # link = str(driver.find_element_by_xpath(following_link_xpath).get_attribute('outerHTML')).split('<')[1].split(' ')[-1].split('"')[0]
        # print(link)



        # window_0 = driver.window_handles[0]
        # window_1 = driver.window_handles[1]
        #
        # driver.switch_to.window(window_1)
        # '''open google authentication page'''
        # driver.get(link)
        # element = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div/form/span/section/div/span/div/div/ul/li[1]/div/div[1]/div/div[2]').click()
        # element = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span').click()
        # element = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div/form/span/section/div/span/div/div/div/div/div/span/span/svg').click()
        # driver.switch_to.window(window_0)
        # element = driver.find_element_by_xpath('/html/body/div/span[2]/pre/input').send_keys(pyautogui.hotkey('ctrl', 'v').pyautogui.press('enter')











        driver.find_element_by_css_selector()
        '#output-footer > pre:nth-child(1) > a:nth-child(1)'





    # def tearDown(self):
    #     self.driver.close()
    #     return




if __name__ == "__main__":
    unittest.main()