# _*_ coding:utf-8 _*_
"""
作者: LiXX
日期: 2024年06月17日
"""
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#url = "http://www.baidu.com"
url = "https://www.google.com.mx/"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_UItesting(driver):
    driver.get(url)
    time.sleep(5)
    search = driver.find_element(By.NAME, "q")
    search.send_keys("如何学习测试")
    search.send_keys(Keys.RETURN)
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.g h3"))
    )

    first_result_title = driver.find_element(By.CSS_SELECTOR, "div.g h3")
    assert "如何学习测试" in first_result_title.text, "搜索词未出现在第一个搜索目录标题中"