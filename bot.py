from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.maximize_window()
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

spam_link = driver.find_element(By.CLASS_NAME, 'rtlI_dz_sSg ')
action = ActionChains(driver)
action.move_to_element(spam_link)
action.click(spam_link)
action.perform()

# driver.close()
