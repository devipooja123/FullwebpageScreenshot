from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.headless=True
driver = webdriver.Chrome(executable_path="C:/Users/Pooja Devi/Downloads/chromedriver_win32 (1)/chromedriver.exe",options=options)
driver.implicitly_wait(10)
driver.get("https://featurepreneur.com/")
S=lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height'))
driver.find_element_by_tag_name('body').screenshot('screenshot.png')
