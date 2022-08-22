from selenium import webdriver
import pyautogui
import time
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
# path = "SesliAsist\chromedriver.exe"

def playyoutube(data):
    data = data.split()
    parcaismi = ""
    for i in data[1:-1]:
        parcaismi = parcaismi + i
    #driver adresine size verdiğim linkten indirdiğiniz
    #driver'ı çıkarttığınız yolun adresini koymalısınız..
    # driver = webdriver.Chrome(path)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.youtube.com/results?search_query=" + parcaismi);
    time.sleep(2)
    pyautogui.click(x=675, y=320, button='left')
    input('harf girin')
    # select_element = driver.find_elements_by_xpath('//*[@id="video-title"]')
    # for option in select_element:
    #     option.find_element_by_xpath('//*[@id="video-title"]').click()
    #     break
    return driver

def aramayap(data):
    data = data.split()
    aranacak = ""
    for i in data[1:-2]:
        aranacak = aranacak + i
    #driver adresine size verdiğim linkten indirdiğiniz
    #driver'ı çıkarttığınız yolun adresini koymalısınız..
    # driver = webdriver.Chrome(path)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://google.com/search?q=" + aranacak)
    time.sleep(2)
    pyautogui.click(x=325, y=400, button='left')
    input('harf girin')

    
if __name__ == "__main__":
    print("hoşgeldiniz.")
    data = input("şarkı ismi gir: ")
    playyoutube(data)