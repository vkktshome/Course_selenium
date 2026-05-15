import time
# завантажуємо матиматичний модуль обчислення формули дізнатися код
import math
cod = str(math.ceil(math.pow(math.pi, math.e)*10000))
print(cod)
# завантажуємо драйвер з Селеніум та локатори
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"
time.sleep(3)   # щоб все побачити

try:
    # відкриваємо пусту сторінку Хрома
    browser = webdriver.Chrome()
    time.sleep(3)
    # йдемо за посиланням змінної link на потрібну сторінку з невідомими кодами
    browser.get(link)
    time.sleep(2)
    # шукаємо потрібний код локатором (методом) порівнянням тексту кодів
    code_link = browser.find_element(By.LINK_TEXT, cod)
    code_link.click()   # клікаємо на нього для відкриття форми реєстрації
    
    # далі шукаємо локаторами як на попередньому кроці (lesson1_6_step_04.py)
    
    # буде взятий перший елемент (зі всіх) з іменем зазначеного тега (вікно)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Валерій") # конструкція введення тексту в знайдене поле 
    # пошук елементу з полем вводу по унікальному значенню атрибуту в ньому
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Ковальов") # конструкція введення тексту в знайдене поле
    # спроба застосувати селектори без досвіду - подвійний унікальний клас
    input3 = browser.find_element(By.CSS_SELECTOR, ".form-control.city")
    input3.send_keys("Київ")    # конструкція введення тексту в знайдене поле
    # О! Є ID в елементі, зазвичай вони унікальні і бажані
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Україна") # конструкція введення тексту в знайдене поле
    
    # пошук елементу з кнопкою локатором повного співпадіння тексту
    # не вийшло! LINK_TEXT виконуэться тыльки для посилань (лінків): <a>text<\a>
    # тому берем або-або, наприклад:
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button = browser.find_element(By.XPATH, "//button[@type='submit' and text()='Submit']")
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    print("ДОЇХАЛИ!!!")
    button.click() # натиснули кнопку

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    print("Згортаємось!")
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла!!!!!!!!!
