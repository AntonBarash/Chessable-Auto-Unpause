from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
action = ActionChains(driver)
driver.get("https://www.chessable.com/login")
time.sleep(1)
inputemail = driver.find_element(By.NAME, "email")
inputemail.send_keys("youremailhere") #replace youremailhere with your chessable email
inputpass = driver.find_element(By.NAME, "password")
inputpass.send_keys("yourpasswordhere") #replace yourpasswordhere with your chessable password
login = driver.find_element(By.ID, "doLoginButton")
login.click()
time.sleep(1)
driver.get("chessablecourselink") # replace chessablecourselink with the link for the chessable course and variation where you would like to unpause
time.sleep(5)
containing = "containstring" #replace containstring with the text that all the variations that you would like to unpause contain
#elem=driver.find_element_by_xpath("//a[@title='Sicilian: 2...d5']")
allvarelems = driver.find_elements_by_xpath("//*[contains(text(), '" + containing + "')]")
for elem in allvarelems:
    href = elem.get_attribute("href")
    varid = "v" + href[36:]
    varid = varid[:-1]
    elem=driver.find_element_by_xpath("//li[@id='" + varid + "']/div[1]/div/div/span/i")
    elem.click()
driver.close()
driver.quit()
