import unittest
import time, sys, win32clipboard, glob, os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

aws_singin_url = "https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3Fstate%3DhashArgs%2523%26isauthcode%3Dtrue&client_id=arn%3Aaws%3Aiam%3A%3A015428540659%3Auser%2Fhomepage&forceMobileApp=0&code_challenge=92u2ia_abJumIAE7LmKqqHW7o3mN9IJXH_BRDbYzfm4&code_challenge_method=SHA-256"
aws_ec2_instances_url = "https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Instances:"
ACCESS_KEY_ID = 'hiaudfhgkuadhfluihg'
SECRET_ACCESS_KEY = 'iafuhgiuahdfu'
user = "gerialworld@gmail.com"
password = "ufadnguiadnfiu"

instanceID = 'i-0e8bef829c4d81924'
region = 'ap-south-1'
instanceUrl = ''
instaceRDPClientUrl = ''
PublicIPv4DNS = ''






class ColabDriver(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(executable_path="C:\colab driver\chromedriver_ver86.exe")
        self.driver = webdriver.Firefox(executable_path="C:\colab driver\Firefox_geckodriver.exe")
        # self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        # driver.maximize_window()
        '''open aws signin page'''
        driver.get(aws_singin_url)

        # passing emailID
        try:
            element = driver.find_element_by_xpath('//*[@id="resolving_input"]')
            element.send_keys(user)
            driver.find_element_by_xpath('//*[@id="next_button_text"]').click()
        except Exception as e:
            print(e)

        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="next_button"]')))
        except ConnectionError as e:
            print("Network connectivity error.", e)
        driver.find_element_by_xpath('//*[@id="next_button"]').click()

        # passing the password
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((
                By.XPATH,'// *[ @ id = "password"]')))
        except ConnectionError as e:
            print("Network connectivity error.", e)
        element = driver.find_element_by_xpath('//*[@id="password"]')
        element.send_keys(password)
        driver.find_element_by_xpath('//*[@id="signin_button"]').click()

        '''opening instance Url'''
        time.sleep(2)
        # driver.get(instanceUrl)
        driver.get(instaceRDPClientUrl)

        # # copying the Public IPv4 DNS Address to clipboard
        # try:
        #     WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,
        #                                                                     "/html/body/div/div/awsui-app-layout/div/main/div/div[2]/div[2]/span/div/div[1]/div[2]/awsui-column-layout/div/span/div/div[5]/div[2]/span/awsui-popover/div/span/span/span/awsui-button/button/awsui-icon/span")))
        # except ConnectionError as e:
        #     print("Network connectivity error.", e)
        # driver.find_element_by_xpath("/html/body/div/div/awsui-app-layout/div/main/div/div[2]/div[2]/span/div/div[1]/div[2]/awsui-column-layout/div/span/div/div[5]/div[2]/span/awsui-popover/div/span/span/span/awsui-button/button/awsui-icon/span").click()
        #
        # win32clipboard.OpenClipboard()
        # PublicIPv4DNS = str(win32clipboard.GetClipboardData())
        # print(PublicIPv4DNS)
        # win32clipboard.CloseClipboard()

        # # Clicking on connect button
        # try:
        #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
        #                                                                     "/html/body/div/div/awsui-app-layout/div/main/div/div[2]/div[2]/span/div/div[1]/div[1]/div/div[2]/awsui-button[2]/button/span")))
        # except ConnectionError as e:
        #     print("Network connectivity error.", e)
        # driver.find_element_by_xpath("/html/body/div/div/awsui-app-layout/div/main/div/div[2]/div[2]/span/div/div[1]/div[1]/div/div[2]/awsui-button[2]/button/span").click()

        # Clicking on RDP Client tab
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                            "/html/body/div/div/awsui-app-layout/div/main/div/div[2]/div[2]/span/div/awsui-form/div/div[2]/span/awsui-form-section/div/div[2]/span/awsui-column-layout/div/span/div/awsui-tabs/div/ul/li[2]/a/span/span/span")))
        except ConnectionError as e:
            print("Network connectivity error.", e)
        driver.find_element_by_xpath("/html/body/div/div/awsui-app-layout/div/main/div/div[2]/div[2]/span/div/awsui-form/div/div[2]/span/awsui-form-section/div/div[2]/span/awsui-column-layout/div/span/div/awsui-tabs/div/ul/li[2]/a/span/span/span").click()

        # Clicking on Download remote desktop file (RDP)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                            "/html/body/div/div/awsui-app-layout/div/main/div/div[2]/div[2]/span/div/awsui-form/div/div[2]/span/awsui-form-section/div/div[2]/span/awsui-column-layout/div/span/div/awsui-tabs/div/div/div[2]/span/awsui-column-layout/div/span/div/div[2]/awsui-button/button/span")))
        except ConnectionError as e:
            print("Network connectivity error.", e)
        driver.find_element_by_xpath("/html/body/div/div/awsui-app-layout/div/main/div/div[2]/div[2]/span/div/awsui-form/div/div[2]/span/awsui-form-section/div/div[2]/span/awsui-column-layout/div/span/div/awsui-tabs/div/div/div[2]/span/awsui-column-layout/div/span/div/div[2]/awsui-button/button/span").click()

        list_of_files = glob.glob(r'C:\Users\user\Downloads\*')  # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        print(latest_file)


# "blob:https://ap-south-1.console.aws.amazon.com/4c31e13b-4b24-429c-a380-37f77e484766"

        for i in range(10000):
            print(i)


    # def tearDown(self):
    #     self.driver.close()
    #     return


if __name__ == "__main__":

    # region = str(sys.argv[0])
    # instanceID = str(sys.argv[1])

    # instanceUrl = "https://" + region + ".console.aws.amazon.com/ec2/v2/home?region=" + region + "#InstanceDetails:instanceId=" + instanceID

    instaceRDPClientUrl = "https://" + region + ".console.aws.amazon.com/ec2/v2/home?" + region + "=ap-south-1#ConnectToInstance:instanceId=" + instanceID


    unittest.main()
