import time
# завантажуємо драйвер з Селеніум та локатори
from selenium import webdriver
from selenium.webdriver.common.by import By

# задаємо змінній значення посилання типу "рядок"
link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
time.sleep(3)   # щоб все побачити

#  визначаємось яку сторінку будемо тестувати: стару/нову
link = input("page for test: old/new...>")
if link == "old":
    link = link1
else:
    if link == "new":
        link = link2
    else:
        # перевірка
        print("Error! Invalid input!")


try:
    # відкриваємо браузер Хрома
    browser = webdriver.Chrome()
    # йдемо за посиланням змінної link на потрібну сторінку
    browser.get(link)

    # створюємо список із елементІВ (..s) з фільтром де є зірочка
    # знаходиш label, а потім переходиш до батька (div) і береш input:
    # конструкція normalize-space() -прибирає пробіли, 
    # конструкція contains(., "*") -знаходить елемент по контексту 
    label_stars = browser.find_elements(By.XPATH, '//label[contains(normalize-space(), "*")]/parent::div/input')
    # або беремо input,який йде відразу після label (не залеж.від div):
    label_stars = browser.find_elements(By.XPATH, "//label[contains(normalize-space(), '*')]/following-sibling::input")
     
    # перебираємо всі елементи списку з *, записуємо в змінну та заповнюємо поля
    # додатково фіксуємо номер ітерації в index ч/з функцію enumerate
    # send_keys: Працює лише з елементами, які можуть приймати 
    # введення (наприклад, <input>, <textarea>). Якщо ні може виникнути помилка.
    for index, label_star in enumerate(label_stars, start=1):
        label_star.send_keys("Any text *: " + str(index))
        print(index)
        
    # пошук елементу з кнопкою Submit локатором повного співпадіння тексту
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click() # натиснули кнопку
    time.sleep(3)  #чекаемо на завантаження сторінки
    
    # знаходимо елемент, який містить текст результату реєстрації
    result_lokator = browser.find_element(By.TAG_NAME, "h1")
    # заносимо значення знайденного в елементі тексту в змінну перевірки
    result_text = result_lokator.text 
    # перевіряємо (порівнюємо) результат за допомогою assert
    assert "Congratulations! You have successfully registered!" == result_text
    print(result_text)
    print("First test (*) - OK")  # Звіт про успішне закінчення тесту
    time.sleep(3)
    
    # тест без зірочки йдемо за посиланням змінної link на потрібну сторінку
    browser.get(link)
    time.sleep(3)
    # список із елементІВ де немає зірочки not(contains(., "*"))
    label_notsts = browser.find_elements(By.XPATH, '//label[not(contains(normalize-space(), "*"))]/parent::div/input')
    for index, label_notst in enumerate(label_notsts, start=1) :
        label_notst.send_keys("Any text -: " + str(index))
        print(index)
    time.sleep(3)    
    # пошук елементу з кнопкою Submit локатором повного співпадіння тексту
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click() # натиснули кнопку
    time.sleep(3)
    # знаходимо елемент, який містить текст результату реєстрації
    result_lokator = browser.find_element(By.TAG_NAME, "h1")
    # заносимо значення знайденного в елементі тексту в змінну перевірки
    result_text = result_lokator.text 
    # перевіряємо (порівнюємо) результат за допомогою assert
    assert "Congratulations! You have successfully registered!" == result_text
    print(result_text)
    time.sleep(3)
    print("First test (*) - OK")  # Звіт про успішне закінчення тесту
    time.sleep(3)
    
    
    # шукаємо потрібні поля локаторами та вводимо в них значення
    # використовуємо виключно ч/з XPATH (пошук всіх елемен.і фільтрація [])
    # зверни увагу на лапки (" vs ')-не можна використовувати "" декілька разів
    #input1 = browser.find_element(By.XPATH, '//input[@name="first_name"]')
    #input1.send_keys("Валерій") # конструкція введення тексту в знайдене поле 
    #input2 = browser.find_element(By.XPATH, '//input[@name="last_name"]')
    #input2.send_keys("Ковальов") # конструкція введення тексту в знайдене поле
    # намагаємося шукати поле по подвійному класу
    #input3 = browser.find_element(By.XPATH, '//input[@class="form-control city"]')
    #input3.send_keys("Київ")    # конструкція введення тексту в знайдене поле
    # О! Є ID, зазвичай вони унікальні і бажані (памятаємо про лапки і імя тега)
    #input4 = browser.find_element(By.XPATH, "//input[@id='country']")
    #input4.send_keys("Україна") # конструкція введення тексту в знайдене поле
    


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
