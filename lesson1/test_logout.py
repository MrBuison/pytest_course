import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def test_logout():
    driver.get("https://www.saucedemo.com/")

    url_before = "https://www.saucedemo.com/"

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    burger_menu = driver.find_element(By.ID, "react-burger-menu-btn")
    burger_menu.click()
    time.sleep(1)

    logout = driver.find_element(By.ID, "logout_sidebar_link")
    logout.click()

    url_after = driver.current_url
    assert url_before == url_after

    driver.quit()

