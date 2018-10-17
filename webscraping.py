import os
import urllib
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

path_to_driver = '/Users/yuhanxie/Desktop/chromedriver'
gpo=webdriver.Chrome(path_to_driver)

for i in range(2000,2018):
    gpo.get("https://www.supremecourt.gov/oral_arguments/argument_transcript/" + str(i) + "")
    expansion = gpo.find_element_by_partial_link_text("Expand All")
    expansion.click()

    elements = gpo.find_elements_by_xpath(".//tr/td[1]/span[1]/a")
    for element in elements:
        link = element.get_attribute("href")
        name = element.text + ".pdf"
        print(name)
        file_name="/Users/yuhanxie/Desktop/LA/web scraping" + name
        r = requests.get(link)
        with open(file_name, 'wb') as outfile:
            outfile.write(r.content)
