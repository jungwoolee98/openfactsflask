from flaskstuff import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

terms = ['mitochondria', 'homeostasis', 'cell membrane']

for term in terms:
	print term
	d=webdriver.Chrome()
	d.get('https://google.com')
	d.find_element_by_name("q").send_keys(term + " education site:youtube.com\n")
	d.implicitly_wait(2)
	link = d.find_element_by_css_selector("._Rm").get_attribute('innerHTML')
	print link, type(link)
	embedded_link = link.encode('utf-8')[-11:]
	embedded_link = "https://youtube.com/embed/" + embedded_link
	print embedded_link
	d.quit()
