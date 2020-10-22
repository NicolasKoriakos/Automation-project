import unittest
from selenium import webdriver
from mercadolibre_tests import MercadoLibreTest


class MercadoTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(executable_path=r'C:\Users\LENOVO\Desktop\Coding proyects\Drivers and other things\.\chromedriver.exe')


    def test_search(self): 

        mercado_libre = MercadoLibreTest(self.driver)
        mercado_libre.open()
        mercado_libre.search()



    @classmethod
    def tearDownClass(cls):

        cls.driver.close()



if __name__ == '__main__':

    unittest.main(verbosity=2)
