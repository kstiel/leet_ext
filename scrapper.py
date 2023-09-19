import requests, json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_argument('--headless=new')
driver = webdriver.Chrome(options=chrome_options)

start_url = "https://neetcode.io/practice"
driver.get(start_url)

neetcode_150_tab = driver.find_element(By.XPATH, "/html/body/app-root/app-pattern-table-list/div/div[2]/div[2]/ul/li[3]")
toogle_button = driver.find_element(By.XPATH, "/html/body/app-root/app-pattern-table-list/div/div[2]/div[1]/div/button[1]")

neetcode_150_tab.click()
if toogle_button.get_attribute("data-tooltip") == "Show List View":
    toogle_button.click()

neetcode_150_table = driver.find_element(By.XPATH, "/html/body/app-root/app-pattern-table-list/div/div[2]/div[4]/app-table/div/table/tbody")

responseObj = requests.get("https://leetcode.com/api/problems/algorithms/")
list_problems = json.loads(responseObj.content)['stat_status_pairs']


paid_problems_set = []

for problem in list_problems:
    if problem['paid_only']:
        paid_problems_set.append(problem['stat']['question__title'].lower())

paid_problems_set = set(paid_problems_set)


f = open("free_neetcode_150_list.txt", "w")
for row in neetcode_150_table.find_elements(By.XPATH, './tr'):
    if row.find_element(By.XPATH, "./td[3]/a").text.lower() not in paid_problems_set:
        f.write(row.find_element(By.XPATH, "./td[3]/a").get_attribute("href") + "\n")
        # print(row.find_element(By.XPATH, "./td[3]/a").get_attribute("href"))
f.close()
driver.quit()
