from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service = Service('/usr/bin/geckodriver')
firefox_options = firefoxOptions()
firefox_options.add_argument('--headless')
driver = webdriver.Firefox(service=service, options=firefox_options)

driver.get('https://www.jwst.nasa.gov/content/webbLaunch/whereIsWebb.html?units=english')
milesAway = driver.find_element(By.ID, 'milesEarth')
l2 = driver.find_element(By.ID, 'milesToL2')
percentage = driver.find_element(By.ID, 'percentageCompleted')
speed = driver.find_element(By.ID, 'speedMi')
tempWarm = driver.find_element(By.ID, 'tempWarmSide2F')
tempCold = driver.find_element(By.ID, 'tempCoolSide2F')

print(f'The James Webb Space Telescope...\n\n-is {milesAway.text} miles away from earth\n\
-is {l2.text} miles away from the L2 point\n-has completed {percentage.text}% of its journey\n-is travelling at \
{speed.text} miles per second\n-is at {tempWarm.text}°F on its warm side\n-is at {tempCold.text}°F on its cold side')

driver.quit()
