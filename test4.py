from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
import requests

def login():
    firfox_op=Options()
    firfox_op.add_argument("--headless")
    # firfox_op.add_argument("--disable-gpu")
    log_file = "geckodriver"
    service = Service(log_output=log_file)
    driver = webdriver.Firefox(service=service,options=firfox_op)

    print("no")
    driver.get("https://newmiind.com/psychology-test/test/neo-five-factor-test/")
    time.sleep(5)
    print("ok")

    buttum=driver.find_element(By.CLASS_NAME,"digits-login-modal")
    buttum.click()
    print("ook")
    time.sleep(2)

    buttum2=driver.find_element(By.NAME,"mobmail")
    buttum2.send_keys("9384245687")
    time.sleep(5)
    print("oook")
    imag=driver.find_element(By.CLASS_NAME,"dig_captcha")
    url_imag=imag.get_attribute("src")
    return url_imag

# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
    driver.close()
