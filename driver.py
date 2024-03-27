import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

path = "D:\CharRoomsTest\chromedriver-win64\chromedriver.exe"


class TestDriver():

    def __init__(self):
                    
        self.driver = webdriver.Chrome()
        self.home_url = "https://stane000.pythonanywhere.com/"


    def login(self, username, password):

        self.driver.get(self.home_url + "login_register/") 

        email_input = self.driver.find_element(By.ID, "username")
        password_input = self.driver.find_element(By.ID, "password")

        email_input.send_keys(username)
        password_input.send_keys(password)

        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()

    def is_user_logged(self) -> bool:

        self.driver.get(self.home_url)
        
        try:
            self.driver.find_element(By.CLASS_NAME, "header__user")
        except:
            return False
        return True

    def logout(self):
        
        dropdown = self.driver.find_element(By.CLASS_NAME, "dropdown-button")
        dropdown.click()

        logout = self.driver.find_elements(By.CLASS_NAME, "dropdown-link")[-1]
        logout.click()
        

    def create_room(self, topic, name, description):

        self.driver.get(self.home_url + "create-room/") 

        # Fill in the form fields
        topic_input = self.driver.find_element(By.NAME, "topic")
        topic_input.clear()  
        topic_input.send_keys(topic)

        name_input = self.driver.find_element(By.NAME, "name")
        name_input.clear()
        name_input.send_keys(name)

        description_input = self.driver.find_element(By.NAME, "description")
        description_input.clear()
        description_input.send_keys(description)

        # Submit the form
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

    def get_number_of_roooms_on_page(self):

        self.driver.get(self.home_url)  

        # Locate specific elements by class name
        return len(self.driver.find_elements(By.CLASS_NAME, "roomListRoom"))

    def send_message(self, room_id, room_meesage="hey"):

        self.driver.get(self.home_url + "room/" + str(room_id)) 

        message_input = self.driver.find_element(By.ID, "messageInput")
        message_input.clear()  
        message_input.send_keys(room_meesage)

        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

    def get_current_page(self) -> str:
        return self.driver.current_url
    
    def get_messages_info(self):

        #self.driver.get(self.home_url + "login_register/")

        return self.driver.find_element(By.CLASS_NAME, "messages")
    
    
    def get_all_room_meessges(self, room_id):

        self.driver.get(self.home_url + "room/" + str(room_id)) 

        return self.driver.find_elements(By.CLASS_NAME, "thread")
        


if __name__ == "__main__":
    driver = TestDriver()
    driver2 = TestDriver()
    for _ in range(5):

        driver.login("stankovicigor199737@gmail.com", "E11zje9de")
        driver.is_user_logged()
        driver2.login("anto199737@gmail.com", "E11zje9de")
        driver.send_message(6)
        driver.logout()