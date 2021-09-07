# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait, Select
# from selenium.webdriver.support import expected_conditions as EC
# import os
#
# import os
# import re
#
# regex = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
#                     "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
#                     "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))
#
# url ="http://www.publicdial.com/free-indian-email-database-list595to600K.aspx"
#
# path = r"C:\Users\user\Documents\email_marketing"
# fileName = "B.Tech, MTEch, MBA, BBA-"+url.split('/')[-1].split('.')[0].split("-")[-1]+".txt"
#
# def get_emails(s):
#     # mistakenly matches patterns like 'http://foo@bar.com' as '//foo@bar.com'.
#     return (email[0] for email in re.findall(regex, s) if not email[0].startswith('//'))
#
#
# class ColabDriver(unittest.TestCase):
#
#     def setUp(self):
#         #self.driver = webdriver.Chrome(driverpath)
#         self.driver = webdriver.Firefox(executable_path=r"C:\colab driver\geckodriver _v0.24.0-win64\geckodriver.exe")
#         # self.driver = webdriver.Firefox()
#
#     def test_search_in_python_org(self):
#         driver = self.driver
#
#         '''open gmail page'''
#         driver.get(url)
#         f = open(os.path.join(path, fileName), "w")
#
#         #  paginationm click
#         for i in range(1, 50):
#             try:
#                 driver.find_element_by_xpath('//*[@id="ctl00_MainContent_dlPagingtop_ctl{0:0=2d}_lnkbtnPagingtop"]'.format(i)).click()
#             except Exception as e:
#                 print(e)
#                 continue
#             try:
#                 element = WebDriverWait(driver, 5).until(
#                     EC.presence_of_element_located((By.XPATH, '/html/body/form/div[3]/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table[2]/tbody'))
#                 )
#             except ConnectionError as e:
#                 print("Network connectivity error.", e)
#
#             elem = driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table[2]/tbody').get_attribute("innerHTML")
#             if elem is not None:
#                 elem = str(elem).lower()
#                 for email in get_emails(elem):
#                     pass
#                     f.write(email+",\n")
#
#
#             print(i)
#         f.close()
#
#     def tearDown(self):
#         print(fileName)
#         self.driver.close()
#         return
#
# if __name__ == "__main__":
#     unittest.main()