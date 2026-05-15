import time
# завантажуємо драйвер з Селеніум та локатори
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/huge_form.html"
print(link)
time.sleep(3)   # щоб все побачити

try:
    # відкриваємо Chrome
    browser = webdriver.Chrome()
    time.sleep(3)
    # йдемо за посиланням на потрібну сторінку зі 100 полями
    browser.get(link)
    # шукаємо ВСІ елементи в HTML (find_elements - на кінці "..s")
    # elements = browser.find_elements(By.CSS_SELECTOR, "input[type="text"]")
    elements = browser.find_elements(By.CSS_SELECTOR, "input")
    
    # перебираємо в циклі всі елементи, записуємо в змінну та заповнюємо поля
    # додатково фіксуємо номер ітерації в index ч\з функцію enumerate
    # send_keys: Працює лише з елементами, які можуть приймати 
    # введення (наприклад, <input>, <textarea>). Якщо ні може виникнути помилка.
    for index, element in enumerate(elements, start=1):
        element.send_keys("Моя відповідь: " + str(index))
    
    
    
    # пошук елементу з кнопкою локатором повного співпадіння тексту
    # не вийшло! LINK_TEXT виконується тільки для посилань (лінків): <a>text<\a>
    # тому берем або-або, наприклад:
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button = browser.find_element(By.XPATH, "//button[@type='submit' and text()='Submit']")
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit'].btn.btn-default")
    print("ДОЇХАЛИ!!!")
    button.click() # натиснули кнопку

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    print("Згортаємось!")
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла!!!!!!!!!
