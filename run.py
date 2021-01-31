import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=options)

df = pd.read_csv("data.csv")
di = {"title": [], "cited_list_url": [], "cited": [], "cited_url": []}
for i in df.index:
    title, cited_list_url = df.loc[i, ["title", "cited_list_url"]]
    driver.get(cited_list_url)
    for paper in driver.find_elements_by_xpath("//h3[@class='gs_rt']/a"):
        di["title"].append(title)
        di["cited_list_url"].append(cited_list_url)
        di["cited"].append(paper.text.lower())
        di["cited_url"].append(paper.get_attribute("href"))

driver.save_screenshot("screenshot.png")
result = pd.DataFrame(di)
result.to_csv("result.csv", index=False)
