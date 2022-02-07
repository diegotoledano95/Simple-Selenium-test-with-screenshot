from time import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdrivermanager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome .app/Contents/MacOS/Google Chrome"
chrome_driver_binary = '/Applications/chromedriver'
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
driver.maximize_window()
driver.implicitly_wait(30)
driver.set_page_load_timeout(50)
driver.get("https://www.istqb.org/")
assert "ISTQB" in driver.title
driver.find_element_by_xpath('//*[@id="t3-mainnav"]/div/div[3]/div/ul/li[5]/a').click()
driver.save_screenshot('/Users/diegotoledano/Desktop/exams.png')
time.sleep(3)
driver.quit()




