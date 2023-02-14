from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

# driver = webdriver.Chrome(options=chrome_options)

driver.get("http://localhost:80/index.php")

# wait web driver 
delay = 5 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located(("id", 'username')))
    print("Page is ready!")
except TimeoutException:
    print ("Loading took too much time!")

# Scenario 1: Test successful login
username = driver.find_element("id","username")
password = driver.find_element("id","password")

username.send_keys("admin")
password.send_keys("admin123")

driver.find_element("xpath","//input[@type='submit']").click()
time.sleep(2)

if driver.current_url == "http://localhost/home.php":
    print("Scenario 1: Testing Successful")
else:
    print("Scenario 1: Testing Failed")

# Scenario 2: Test wrong username
driver.back()

username = driver.find_element("id","username")
password = driver.find_element("id","password")

username.clear()
password.clear()

username.send_keys("notadmin")
password.send_keys("admin123")

driver.find_element("xpath","//input[@type='submit']").click()
time.sleep(2)

notif = driver.find_element("xpath","//div[@class='notif']").text

if notif == "Wrong username or password!":
    print("Scenario 2: Testing Successful")
else:
    print("Scenario 2: Testing Failed")

# Scenario 3: Test wrong password
driver.back()

username = driver.find_element("id","username")
password = driver.find_element("id","password")

username.clear()
password.clear()

username.send_keys("admin")
password.send_keys("notadmin123")

driver.find_element("xpath","//input[@type='submit']").click()
time.sleep(2)

notif = driver.find_element("xpath","//div[@class='notif']").text

if notif == "Wrong username or password!":
    print("Scenario 3: Testing Successful")
else:
    print("Scenario 3: Testing Failed")

# Scenario 4: Test empty input
driver.back()

username = driver.find_element("id","username")
password = driver.find_element("id","password")

username.clear()
password.clear()

driver.find_element("xpath","//input[@type='submit']").click()
time.sleep(2)
if driver.current_url == "http://localhost/index.php":
    print("Scenario 4: Testing Successful")
else:
    print("Scenario 4: Testing Failed")

# Scenario 5 : Test Karakter tidak valid

time.sleep(10)
username = driver.find_element("xpath","//input[@id='username']")
password = driver.find_element("xpath","//input[@id='password']")
username.clear()
password.clear()

username.send_keys("\x01\x02")
password.send_keys("\x01")

driver.find_element("xpath","//input[@type='submit']").click()

time.sleep(2)
if driver.current_url == "http://localhost/index.php":
    print("Scenario 5: Testing Successful")
else:
    print("Scenario 5: Testing Failed")
