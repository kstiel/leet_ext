from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless=new") # for Chrome >= 109
# chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works
driver = webdriver.Chrome(options=chrome_options)
start_url = "https://neetcode.io/practice"
driver.get(start_url)

neetcode_150_tab = driver.find_element(By.XPATH, "/html/body/app-root/app-pattern-table-list/div/div[2]/div[2]/ul/li[3]")
toogle_button = driver.find_element(By.XPATH, "/html/body/app-root/app-pattern-table-list/div/div[2]/div[1]/div/button[1]")

neetcode_150_tab.click()
if toogle_button.get_attribute("data-tooltip") == "Show List View":
    toogle_button.click()

neetcode_150_table = driver.find_element(By.XPATH, "/html/body/app-root/app-pattern-table-list/div/div[2]/div[4]/app-table/div/table/tbody")

count = 0
for row in neetcode_150_table.find_elements(By.XPATH, './tr'):
    
    count += 1
print(count)

# b'<!DOCTYPE html><html xmlns="http://www....
driver.quit()
