from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Data import data
from Locators import locators


class IMDbNameSearch:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 10)
        

    def access_imdb_advanced_search(self):
        try:
            self.driver.maximize_window()
            self.driver.get(data.Imdb_data().url)

            # Access the Name & fill data
            Name =self.wait.until(EC.element_to_be_clickable((By.NAME, locators.Imdb_locators().name_ip)))
            Name.send_keys(data.Imdb_data().name)

            # Access the birth date & fill data
            birth_min =self.wait.until(EC.visibility_of_element_located((By.NAME, locators.Imdb_locators().bd_min_ip)))
            birth_min.send_keys(data.Imdb_data().bd_min_ip)

            birth_max = self.wait.until(EC.visibility_of_element_located((By.NAME, locators.Imdb_locators().bd_max_ip)))
            birth_max.send_keys(data.Imdb_data().bd_max_ip)

            # Access & fill birthday
            birth = self.wait.until(EC.visibility_of_element_located((By.NAME, locators.Imdb_locators().bd_day_ip)))
            birth.send_keys(data.Imdb_data().bd_day)

            self.driver.find_element(By.ID, locators.Imdb_locators().na_ch_id).click()
            
             # Access & give birthplace
            birth_place = self.wait.until(EC.visibility_of_element_located((By.NAME, locators.Imdb_locators().bd_place_name)))
            birth_place.send_keys(data.Imdb_data().bd_pl_data)

             # Access & fill death date 
            death_min = self.wait.until(EC.visibility_of_element_located((By.NAME, locators.Imdb_locators().dd_min_name)))
            death_min.send_keys(data.Imdb_data().dd_min)


            death_max = self.wait.until(EC.visibility_of_element_located((By.NAME, locators.Imdb_locators().dd_max_name)))
            death_max.send_keys(data.Imdb_data().dd_max)

            death_place = self.wait.until(EC.visibility_of_element_located((By.NAME, locators.Imdb_locators().dd_pla_name)))
            death_place.send_keys(data.Imdb_data().dd_pla)

             # Access the gender data
            gen = self.driver.find_element(By.ID, locators.Imdb_locators().gen_id).click()

            # Access the Award & recogination
            aw = self.driver.find_element(By.XPATH, locators.Imdb_locators().aw_reg_path)
            dropdown = Select(aw)
            dropdown.select_by_value(locators.Imdb_locators().aw_opt_value)

             # Access the dropdown
            od = self.driver.find_element(By.NAME, locators.Imdb_locators().dis_name)
            dropdown = Select(od)
            dropdown.select_by_value(locators.Imdb_locators().dis_drop_val)

            # Click the "Search" button
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Imdb_locators().search_path))).click()
            print("search completed succesfully")

        except Exception as e:
            print(e)

        finally:
            self.driver.quit()
            
im = IMDbNameSearch()
im.access_imdb_advanced_search()