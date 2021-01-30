import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=options)
driver.implicitly_wait(10)
driver.get(
    "https://scholar.google.com/scholar?cites=585713681430766553&as_sdt=2005&sciodt=0,5&hl=en"
)
driver.save_screenshot("screenshot.png")
