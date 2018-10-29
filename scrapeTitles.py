import os
import urllib
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import re


path_to_driver = '/Users/pratibha/Downloads/chromedriver'
gpo=webdriver.Chrome(path_to_driver)


outputPath = "/Users/pratibha/Desktop/LA/test/"

for i in range(2000,2019):
    gpo.get("https://www.supremecourt.gov/oral_arguments/argument_transcript/" + str(i) + "")
    expansion = gpo.find_element_by_partial_link_text("Expand All")
    expansion.click()

    # //*[@id="cell01-10-2018"]/div/table/tbody/tr[2]/td[1]/span[2]
    # //*[@id="cell01-10-2018"]/div/table/tbody/tr[2]/td[1]/span[1]/a


    links = gpo.find_elements_by_xpath(".//tr/td[1]/span[1]/a")
    names = gpo.find_elements_by_xpath(".//tr/td[1]/span[2]")
    for i in range(len(links)):

        link = links[i]
        name = names[i + 1]
        linkpath = link.get_attribute("href")
        name = name.text + ".pdf"
        name = name.replace("/", "")
        print(name)
        file_name= outputPath + name
        r = requests.get(linkpath)
        with open(file_name, 'wb') as outfile:
             outfile.write(r.content)