# %%

import requests
import pandas as pd 
import time 
import datetime 
import pytz

today = datetime.datetime.today()
today = today.astimezone(pytz.timezone("Australia/Brisbane")).strftime('%Y%m%d')

from selenium import webdriver 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Firefox(options=chrome_options)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def dumper(path, name, frame):
    with open(f'{path}/{name}.csv', 'w') as f:
        frame.to_csv(f, index=False, header=True)



start_url = 'https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-processing-times/global-processing-times'

# %%

driver.get(start_url)

tabs = []

for i in range(0,5):

  time.sleep(1)

  tab = pd.read_html(driver.page_source)[0]


  dumper('input/raw', f'{today}-{i}', tab)

  tabs.append(tab)

  cat = pd.concat(tabs)

  dumper('input/out', f'{today}', cat)

  button = driver.find_element_by_link_text(f"Next").click()

  time.sleep(5)

# %%

# cat = pd.concat(tabs)

# with open()

# p = tab[0]

# print(p)
# print(p.columns.tolist())


# %%



