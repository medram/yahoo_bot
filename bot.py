from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
# driver.maximize_window()
driver.get("https://login.yahoo.com/?.src=ym&.lang=en-BE&.intl=be&.done=https%3A%2F%2Fmail.yahoo.com%2Fd")
# assert "Python" in driver.title
print(driver.title)
email = driver.find_element_by_id("login-username")
email.clear()
email.send_keys("eleonoreguernon13@yahoo.com")
email.send_keys(Keys.RETURN)

# switch to password window.
driver.implicitly_wait(2)
# print(driver.window_handles)
# pass_window = driver.window_handles.pop()
# driver.switch_to.window(pass_window)
# print(pass_window)

password = driver.find_element_by_id('login-passwd')
password.clear()
password.send_keys('HJxUXq5S')
password.send_keys(Keys.ENTER)

# switch to inbox window.
driver.implicitly_wait(2)
# driver.switch_to.frame(0)

spam_link = driver.find_elements_by_css_selector('a.W_6D6F')
# Spam section
spam_link[6].send_keys(Keys.RETURN)

driver.implicitly_wait(2)




# action = ActionChains(driver)
# action.move_to_element(spam_link)
# action.click(spam_link)
# action.perform()

# emails = driver.find_elements(By.CLASS_NAME, 'c27KHO0_n')
driver.implicitly_wait(2)
print(driver.window_handles)
messages = driver.find_elements_by_css_selector('button.c27KHO0_n')
# messages = driver.find_elements_by_css_selector('button[data-test-id="icon-btn-checkbox"] span.D_F')

# for message in messages:
# 	message.click()
# print(messages)
# https://www.programcreek.com/python/example/100026/selenium.webdriver.FirefoxProfile
driver.execute_script("""
	console.log(arguments)
	arguments[0].click()
""", messages)

# driver.close()
