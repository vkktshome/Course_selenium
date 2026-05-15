import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
time.sleep(3)

link = input("page for test: old/new...>")
if link == "old":
    link = link1
else:
    if link == "new":
        link = link2
    else:
        print("Input error")

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)
    
    # label_stars = browser.find_elements(By.XPATH, '//label[contains(normalize-space(), "*")]/parent::div/input')
    # for index, label_star in enumerate(label_stars, start=1):
    #     label_star.send_keys("Any text *: " + str(index))
        
    input1 = browser.find_element(By.XPATH, "//label[contains(normalize-space(), 'First name*')]/following-sibling::input")
    input1.send_keys("Ivan") 
    input2 = browser.find_element(By.XPATH, "//label[contains(normalize-space(), 'Last name*')]/following-sibling::input")
    input2.send_keys("Ivanov")
    input3 = browser.find_element(By.XPATH, "//label[contains(normalize-space(), 'Email*')]/following-sibling::input")
    input3.send_keys("ivan.ivanov@gmail.com")
    
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    time.sleep(3)
    button.click()
        
    result_lokator = browser.find_element(By.TAG_NAME, "h1")
    result_text = result_lokator.text 
    time.sleep(2)

    assert "Congratulations! You have successfully registered!" == result_text
    print(result_text)
    time.sleep(3)    
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
