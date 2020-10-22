from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from time import sleep


class MercadoLibreTest(object):

    def __init__(self,driver):

        self._driver = driver
        self._url = 'http://www.mercadolibre.com/'

    @property
    def keyword(self):
        pass
    
    def open(self):

        self._driver.get(self._url) # 'llama' a la pagina de la variable
        self._driver.maximize_window()
        self._driver.implicitly_wait(30)
        self._driver.find_element_by_id('AR').click() # cliquea en el mercado de Argentina
        


    def search(self):
        
        self.search_locator = self._driver.find_element_by_name('as_word') # encuentra la barra de busqueda
        self.search_locator.click() # cliquea en la barra de busqueda
        self.search_locator.clear() # limpia la barra de busqueada
        sleep(1.5)
     
        item = 'iPhone XS' # Aca va el item que deseas buscar, aca usamos un iPhone XS como ejemplo

        self.find_item(item)


    def find_item(self,keyword):

        self.search_locator.send_keys(keyword)
        self.search_locator.submit()
        sleep(2)