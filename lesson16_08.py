import time
# завантажуємо драйвер з Селеніум та локатори
from selenium import webdriver
from selenium.webdriver.common.by import By

# задаємо змінній значення посилання типу "рядок"
link = "http://suninjuly.github.io/find_xpath_form"
time.sleep(3)   # щоб все побачити

try:
    # відкриваємо браузер Хрома
    browser = webdriver.Chrome()
    # йдемо за посиланням змінної link на потрібну сторінку
    browser.get(link)

    # шукаємо потрібні поля локаторами та вводимо в них значення
    # використовуємо виключно ч/з XPATH (вибір всіх елем.і фільтрація [])
    # зверни увагу на лапки (" vs ')-не можна використовувати "" декілька разів
    input1 = browser.find_element(By.XPATH, '//input[@name="first_name"]')
    input1.send_keys("Валерій") # конструкція введення тексту в знайдене поле 
    input2 = browser.find_element(By.XPATH, '//input[@name="last_name"]')
    input2.send_keys("Ковальов") # конструкція введення тексту в знайдене поле
    # намагаємося шукати поле по подвійному класу
    # помилка 1:
    # input3 = browser.find_element(By.XPATH, "//.form-control.city")
    # помилка 2:
    # input3 = browser.find_element(By.XPATH, "//input[.form-control.city]")
    # вірно (потрібно беред фільтром вказувати імя тега!!)
    input3 = browser.find_element(By.XPATH, '//input[@class="form-control city"]')
    input3.send_keys("Київ")    # конструкція введення тексту в знайдене поле
    # О! Є ID, зазвичай вони унікальні і бажані (памятаємо про лапки і імя тега)
    input4 = browser.find_element(By.XPATH, "//input[@id='country']")
    input4.send_keys("Україна") # конструкція введення тексту в знайдене поле
    
    # пошук елементу з кнопкою Submit локатором повного співпадіння тексту
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click() # натиснули кнопку

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
