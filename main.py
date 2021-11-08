from selenium import webdriver

from Scrape import Scrape

# Instanancing the Scrape Class
# scrape = Scrape("https://www.propertypanorama.com")
# # Open ChromeWebDriver
# driver = webdriver.Chrome(executable_path="chromedriver.exe")
# # Scrape all the links
#
#
# scrape.scrape("https://www.propertypanorama.com/instaview/mia/A11101026", driver)

# driver.close()
from ScrapeFull import ScrapeFull

s = ScrapeFull()
s.scrapeAllLinksTest("https://www.propertypanorama.com/instaview/mia/A11101026")