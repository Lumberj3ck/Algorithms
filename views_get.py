import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument('--incognito')
# chrome_options.add_argument('--headless')
print('asdf')
driver = webdriver.Chrome(options=chrome_options)
# url = 'https://public.tableau.com/app/profile/abdullah.alsudani/viz/ExecutiveOverview_17038932314610/ExecutiveOverview'
url = 'https://learning.oreilly.com/library/view/python-testing-with/9781680509427/f_0053.xhtml#d24e9526'


print('asdf')
def wait_for_element():
    # driver.implicitly_wait(5)
    time.sleep(3)
    while True:
        try:
            cookie_accept_button = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        except:
            continue
        else:
            break
    cookie_accept_button.click()

print('asdf')
driver.get(url)
print('asdf')
# wait_for_element()

reload_count = 1000
for _ in range(reload_count):
    time.sleep(3)
    driver.refresh()
    print('Reloaded +1 ')
    # wait_for_element()

input("Press Enter to quit")

driver.quit()

