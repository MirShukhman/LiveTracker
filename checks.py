
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Checks:
    def __init__(self):
        self.pegasus_url= 'http://20.246.179.188:5000'
        self.eventhub_url= 'http://52.154.67.55'
        self.resume_url= 'http://mirshukhman.com'
        
    def check_pegasus(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        try:
            driver.get(f'{self.pegasus_url}/redirect_to_searchforflightbyid')
            
            input_element = driver.find_element("id",'flight_id')
            submit_button = driver.find_element("id",'search_for_flight_by_id_button')

            input_element.send_keys('13')

            submit_button.click()
            # Wait until the "flight" div appears (with a timeout of 10 seconds)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'flight')))
            status=f"Action performed successfully"
        
        except TimeoutException:
            # If the "flight" div does not appear within the timeout, return False
            status=f"ERROR :Failed to perform action"
            
        except Exception as e:
            status=f"ERROR :Failed to perform action: {str(e)}"
            
        finally:
            driver.quit()
            return status


    def check_eventhub(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        try:
            driver.get(self.eventhub_url)

            menu_button = driver.find_element(By.CSS_SELECTOR,'#open-sidebar button')
            menu_button.click()
            
            sidebar_button = driver.find_element(By.CSS_SELECTOR,'.sidebar-buttons-wrapper button')
            sidebar_button.click()
            
            organiser_input = driver.find_element("id",'organiser')
            organiser_input.send_keys('Max Vol')

            submit_button = driver.find_element(By.CSS_SELECTOR, '.search-button button')
            submit_button.click()
            submit_button.click()
        
            # Wait until the "open-event" div appears 
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'open-event')))
            status=f"Action performed successfully"
        
        except TimeoutException:
            # If the "open-event" div does not appear within the timeout, return False
            status=f"ERROR :Failed to perform action"
            
        except Exception as e:
            status=f"ERROR :Failed to perform action: {str(e)}"
            
        finally:
            driver.quit()
            return status


    def check_resume(self):
            driver = webdriver.Chrome()
            driver.maximize_window()
            try:
                driver.get(self.resume_url)

                name_input = driver.find_element(By.CSS_SELECTOR,'#message-form #name')

                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#message-form #name')))
                name_input.send_keys('twice-a-day-test')

                eamil_input = driver.find_element("id",'eamil')
                eamil_input.send_keys('miriysha@gmail.com')

                message_input = driver.find_element(By.TAG_NAME, 'textarea')
                message_input.send_keys('hola :)')

                submit_button = driver.find_element(By.CSS_SELECTOR, '#message-form button')
                submit_button.click()

                # Wait until the "sucsess-msg" div appears 
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'sucsess-msg')))
                status=f"Action performed successfully"
            
            except TimeoutException:
                # If the "sucsess-msg" div does not appear within the timeout, return False
                status=f"ERROR :Failed to perform action"
                
            except Exception as e:
                status=f"ERROR :Failed to perform action: {str(e)}"
                
            finally:
                driver.quit()
                return status