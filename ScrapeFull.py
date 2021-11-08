import pandas as pd
from selenium import webdriver

from Scrape import Scrape


class ScrapeFull:

    def scrapeAllLinks(self, linkList):
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        for link in linkList:
            Scrape.scrape(link, driver)

    def scrapeAllLinksTest(self, link):
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        s = Scrape("asd")
        list = []
        for i in range(0,9):
            for j in range(0, 9):
                link = link[:-2]
                link += f'{i}'
                link += f'{j}'
                info = s.scrape(link, driver)
                if info is not None:
                    print("APPENDED")
                    list.append(info)

        dataFrame = pd.DataFrame(list)
        dataFrame.to_excel("output.xlsx")

        driver.close()
