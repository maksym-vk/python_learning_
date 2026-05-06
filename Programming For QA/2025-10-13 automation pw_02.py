

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False) #запускаємо браузер у явному режимі
    page=browser.new_page() #відкриваємо нове вікно браузера
    page.goto("https://google.com")
    print("Title:", page.title()) #виводимо у консолі текст елемента <title>
    browser.close() #закриваємо браузер

