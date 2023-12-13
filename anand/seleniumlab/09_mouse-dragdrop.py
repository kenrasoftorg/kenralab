from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time


# Specify the path to the downloaded chromedriver.exe
driver_path = "C:\\Users\\anand\\Selenium\\chromedriver.exe"

driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path))

driver.get("https://jqueryui.com/droppable/")

# Switch to the frame where the draggable and droppable elements are present
driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))

# Find the draggable and droppable elements
draggable = driver.find_element(By.ID, "draggable")
droppable = driver.find_element(By.ID, "droppable")

# Perform the drag-and-drop action
actions = ActionChains(driver)
actions.drag_and_drop(draggable, droppable)
actions.perform()

# Switch back to the main content (out of the frame)
driver.switch_to.default_content()

time.sleep(5)
# Close the browser
driver.quit()

