import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import selenium

print("seleniumのバージョン",selenium.__version__)
from selenium.webdriver.firefox.options import Options as FirefoxOptions
options = FirefoxOptions()
cloud_options = {}
cloud_options['build'] = "build_1"
cloud_options['name'] = "test_abc"
options.set_capability('cloud:options', cloud_options)


driver = webdriver.Remote(
    command_executor=os.environ["SELENIUM_URL"],
    options=options
)
driver.implicitly_wait(5)

# ここからコーディング

driver.get("https://www.time-j.net/worldtime/country/jp")

print(driver.find_element(By.XPATH, "/html/body/div/div[6]/div[1]/div/p[5]").text)
driver.quit()
