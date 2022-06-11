import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


frazaTestowa = "Paczkord"
cyfra1 = "65"
cyfra2 = "45"

class APRegistration(unittest.TestCase):
    """Analogia: Przypadek/scenariusz testowy"""

    # Przygotowanie do każdego testu
    # (Warunki wstepne)
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://demo.seleniumeasy.com/')
        self.driver.maximize_window()
        sleep(1)
        self.driver.find_element(By.ID,"at-cv-lightbox-close").click()
        self.driver.implicitly_wait(2)

    # Sprzatanie po kazdym tescie
    def tearDown(self):
        self.driver.quit()

    def testSingleInputField(self):
        self.driver.find_element(By.ID, "basic_example").click()
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="basic"]/div/a[1]').click()
        sleep(1)
        wiadomosc = self.driver.find_element(By.ID,"user-message")
        wiadomosc.clear()
        wiadomosc.send_keys(frazaTestowa)
        self.driver.find_element(By.XPATH,'// *[ @ id = "get-input"] / button').click()
        SingleInputField = self.driver.find_element(By.ID,"display").text
        print(SingleInputField)
        assert SingleInputField == frazaTestowa
        sleep(2)

    def testTwoInputFields(self):
        self.driver.find_element(By.ID, "basic_example").click()
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="basic"]/div/a[1]').click()
        sleep(1)
        sum_1 = self.driver.find_element(By.ID,"sum1")
        sum_1.send_keys(cyfra1)
        sum_2 = self.driver.find_element(By.ID,"sum2")
        sum_2.send_keys(cyfra2)
        sumTestA = int(cyfra2) + int(cyfra1)
        self.driver.find_element(By.XPATH,'//*[@id="gettotal"]/button').click()
        sumTestB = self.driver.find_element(By.ID,"displayvalue").text
        print(str(sumTestA) +" vs "+ str(sumTestB))
        sleep(2)
        assert str(sumTestA) == str(sumTestB)

# Uruchom test jesli uruchamiamy
# ten plik
if __name__ == "__main__":
    unittest.main()