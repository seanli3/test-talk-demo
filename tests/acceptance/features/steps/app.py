from behave import given, when, then, step
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from redis import StrictRedis

r = StrictRedis(host='localhost', port=6379, db=0)
r.delete('bmi')

driver = webdriver.Chrome()

@given('open App index page')
def _(context):
    driver.get("http://localhost:5000")

@when('user type in weight: {weight} and height: {height}')
def _(context, weight, height):
    weightEl = driver.find_element_by_name("weight")
    weightEl.clear()
    weightEl.send_keys(weight)
    heightEl = driver.find_element_by_name("height")
    heightEl.clear()
    heightEl.send_keys(height)

@when('select the {btn_text} button')
def _(context, btn_text):
    button = driver.find_element_by_xpath("//button[contains(text(), '" + btn_text +"')]")
    button.click()


@then('BMI is displayed as {bmi}')
def _(context, bmi):
    driver.implicitly_wait(3)
    text = driver.find_element_by_xpath("//p[contains(text(), '" +bmi +"')]")
    assert text

@then('life expectancy is displayed as {age}')
def _(context, age):
    driver.implicitly_wait(3)
    text = driver.find_element_by_xpath("//p[contains(text(), '" + age +"')]")
    assert text

