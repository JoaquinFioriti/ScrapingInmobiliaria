from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd



class Scrape:


    def __init__(self, urlBase):
        self.urlBase = urlBase


    def scrape(self, url):
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.get(url)
        driver.find_element(By.ID, "information").click()

        container = driver.find_element(By.CSS_SELECTOR,"div.pmodal-body")
        #Getting info

        information = {
            "address" : '',
            'price' : '',
            'listingNumber':'',
            'Bedrooms' : '',
            'Bathrooms' : '',
            'Full Bathrooms' : '',
            'Square Feet' : '',
            'School District' : '',
            'Half Bathrooms' : '',
            'urlImages':[]
        }

        infos = container.find_elements(By.XPATH,"//div[@class='form-group informationblockheight col-md-4 col-sm-12 ng-binding']")
        information["address"] = infos[0].text
        information["price"] = infos[1].text.split('$')[1].replace(',','')
        information["listingNumber"] = container.find_element(By.XPATH, "//div[@class='informationblockheight form-group col-md-4 col-sm-12 ng-binding']").text
        infos = container.find_elements(By.XPATH, "//span[@ng-repeat='metadata in house.extra_meta_col1']")

        for f in infos:
            text = f.text.split("\n")
            index = text[0].replace(':','')
            value = text[1]
            information[index] = value


        #Getting Images
        containerImg = driver.find_element(By.CSS_SELECTOR, "div.galleria-thumbnails-container")

        images = containerImg.find_elements(By.CSS_SELECTOR, "div.galleria-image")
        urlsImgs = []
        for im in images:
            im = im.find_element(By.TAG_NAME, "img").get_attribute("src")
            urlsImgs.append(im)

        information["urlImages"] = ' '.join([str(item) for item in urlsImgs])

        driver.close()
        print(information)


        lista = []
        lista.append(information)

        dataFrame = pd.DataFrame(lista)
        dataFrame.to_excel("output.xlsx")













