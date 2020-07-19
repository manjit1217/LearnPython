from selenium import webdriver
from appium import webdriver
# "app":'C://Users/Manjit/Desktop/Amazon_shopping.apk',
desired_caps={
    "deviceName": "OnePlus5",
    "platformName": "Android",
    "platformVersion" : "10.0",
    "realDevice": True,
    "appPackage":"com.tvf.tvfplay",
    "appActivity":"com.tvf.tvfplay.MainActivity",
    "udid":"f521c294",
    "automationName ":"UiAutomator2"

}

driver=webdriver.Remote('http://127.0.0.1:5025/wd/hub',desired_caps)
driver.save_screenshot('manjit.png')

