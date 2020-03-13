import random
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException


fp = webdriver.FirefoxProfile(r'C:\Users\VIASYS\AppData\Roaming\Mozilla\Firefox\Profiles\4awq77ne.amabellaracine50')
driver = webdriver.Firefox(fp)
driver.implicitly_wait(2)
driver.get('https://mail.yahoo.com')
print(driver.title)

# driver.get("https://login.yahoo.com/?.src=ym&.lang=en-BE&.intl=be&.done=https%3A%2F%2Fmail.yahoo.com%2Fd")
# driver.maximize_window()
# assert "Python" in driver.title
# email = driver.find_element_by_id("login-username")
# email.clear()
# email.send_keys("eleonoreguernon13@yahoo.com")
# email.send_keys(Keys.RETURN)

# # switch to password window.
# driver.implicitly_wait(2)
# print(driver.window_handles)
# pass_window = driver.window_handles.pop()
# driver.switch_to.window(pass_window)
# print(pass_window)

# password = driver.find_element_by_id('login-passwd')
# password.clear()
# password.send_keys('HJxUXq5S')
# password.send_keys(Keys.ENTER)

# switch to inbox window.
# driver.switch_to.frame(0)

driver.implicitly_wait(3)
# Spam section
driver.get('https://mail.yahoo.com/d/folders/6')
# spam_link = driver.find_elements_by_css_selector('a.W_6D6F')
# spam_link[6].send_keys(Keys.RETURN)
driver.implicitly_wait(10)

# action = ActionChains(driver)
# action.move_to_element(spam_link)
# action.click(spam_link)
# action.perform()

# emails = driver.find_elements(By.CLASS_NAME, 'c27KHO0_n')

# print(driver.window_handles)
# spam messages.
messages = driver.find_elements_by_css_selector('button[data-test-id=icon-btn-checkbox]')

# for message in messages:
# 	if random.random() <= 0.5:
# 		message.send_keys(Keys.RETURN)
# 		# message.click()
driver.implicitly_wait(2)
# print(messages)
# https://readthedocs.org/projects/selenium-python/downloads/pdf/latest/
# https://www.programcreek.com/python/example/100026/selenium.webdriver.FirefoxProfile

driver.execute_script("""
	console.log(arguments[0]);
	arguments[0].map(b => {
			if (Math.random() < 0.5)
				b.click();
		});

		setTimeout(() => {
			document.querySelector("button[data-test-id=toolbar-not-spam]").click();
		}, 2000)
""", messages)

try:
	WebDriverWait(driver, 6).until(EC.presence_of_element_located(driver.find_elements_by_css_selector("div[role=status] div#notifications")))
except (NoAlertPresentException, TimeoutException) as py_ex:
	pass

driver.implicitly_wait(2)
driver.get("https://mail.yahoo.com/d/folders/1")
driver.implicitly_wait(10)


# Mark as read in messages inbox.
messages = driver.find_elements_by_css_selector('button[data-test-id=icon-btn-checkbox]')

driver.execute_script("""
	arguments[0].map(b => {
			if (Math.random() < 0.5)
				b.click();
		});

""", messages)
ActionChains(driver).key_down(Keys.SHIFT).send_keys('K').key_up(Keys.SHIFT).perform()
driver.implicitly_wait(20)


# adding stars to the inbox messages.
messages = driver.find_elements_by_css_selector('button[data-test-id=icon-btn-checkbox]')
driver.execute_script("""
	console.log('ADDING STARS...')
	document.querySelector("button[data-test-id=checkbox]").click();
	arguments[0].map(b => {
			if (Math.random() < 0.2)
				b.click();
		});
""", messages)
ActionChains(driver).send_keys('l').perform()

# driver.close()
