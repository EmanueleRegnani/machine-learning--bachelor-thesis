from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
from time import sleep
from selenium.webdriver.common.keys import Keys
# import pyperclip




athlete = input("Enter an athlete's name: ").title()
parsed_athlete_name = [*athlete]
discipline = input("Enter a discipline: ").title()
disciplines = {
    'Numbers': 'div.transition:nth-child(4) > div:nth-child(6)',
    'Cards': 'div.transition:nth-child(4) > div:nth-child(2)',
    'Words': 'div.transition:nth-child(4) > div:nth-child(7)',
    'Images': 'div.transition:nth-child(4) > div:nth-child(3)',
    'International Names': 'div.transition:nth-child(4) > div:nth-child(4)',
    'Names': 'div.transition:nth-child(4) > div:nth-child(5)',
    }
discipline_id = disciplines[discipline]

browser = webdriver.Firefox(executable_path=r'C:\Users\emanu\Programs\geckodriver-v0.31.0-win64\geckodriver.exe')
browser.get('https://memoryleague.com/#!/home')





sleep(0.5)

### Zoom out 5 times
sleep(1)
pyautogui.click(1581, 77)
sleep(0.25)
pyautogui.click(1449,640)
sleep(0.25)
pyautogui.click(1449,640)
sleep(0.25)
pyautogui.click(1449,640)
sleep(0.25)
pyautogui.click(1449,640)
sleep(0.25)
pyautogui.click(1449,640)
pyautogui.click(1581, 77)

# Search for athlete's games in the specified discipline
button = browser.find_element(By.CSS_SELECTOR, "#gameSearch")
button.click()
sleep(0.5)
button = browser.find_element(By.CSS_SELECTOR, ".eventName")
button.click()
sleep(0.5)
button = browser.find_element(By.CSS_SELECTOR, discipline_id) # previous id was "span.eventNameNumbers:nth-child(1)" if you need it
button.click()
sleep(0.5)
pyautogui.click(938,286)#893,326)
sleep(0.5)
parsed_athlete_name.append('Enter')
pyautogui.typewrite(parsed_athlete_name)
parsed_athlete_name.pop()
sleep(5)


with open('Project/Dataset/' + athlete + ' - ' + discipline + '.txt', 'w') as f:
        
    ranges, x = [(1, 7)], 7
    while x < 400:
        ranges.append((x, x+10))
        x += 10

    #ranges = [(1, 7), (7, 17), (17, 27), (27, 37), (37, 47), (47, 57), (57, 67), (67, 77), (77, 87), (87, 97), (97, 107), (107, 117), (117, 127), (127, 137), (137, 147), (147, 157), (157, 167), (167, 177), (177, 187), (187, 197), (197, 207)]
    for r in ranges:
            
        for i in range(r[0], r[1]):
            user_0 = 'a.publicMatchLink:nth-child(' + str(i) + ') > div:nth-child(2) > div:nth-child(1) > span:nth-child(2)'
            user_1 = 'a.publicMatchLink:nth-child(' + str(i) + ') > div:nth-child(2) > div:nth-child(1) > span:nth-child(6)'
            text = 'a.publicMatchLink:nth-child(' + str(i) + ') > div:nth-child(2) > div:nth-child(1) > span:nth-child(10)'
                    
            if browser.find_element(By.CSS_SELECTOR, user_0).get_attribute("innerHTML") == athlete:
                result = browser.find_element(By.CSS_SELECTOR, text).get_attribute("innerHTML")[20:32]
            else:
                result = browser.find_element(By.CSS_SELECTOR, text).get_attribute("innerHTML")[52:-20]
                
            if result[-1] == 's':
                result = result[:-1]
            
            f.write(result[:3].strip() + ',' + result[-6:].strip() + '\n')    
            print(result[:3].strip() + ',' + result[-6:].strip())
        
        # click "View more"
        button = browser.find_element(By.CSS_SELECTOR, 'div.message:nth-child(2) > p:nth-child(7) > a:nth-child(1)')#div.message:nth-child(2) > p:nth-child(7) > a:nth-child(1)')#div.message:nth-child(2) > p:nth-child(7) > a:nth-child(1)')#'div.eight:nth-child(2) > div:nth-child(3) > p:nth-child(7) > a:nth-child(1)')
        button.click()
        
        # Scroll down to the bottom
        sleep(1)
        htmlelement= browser.find_element(By.TAG_NAME, 'html')
        htmlelement.send_keys(Keys.END)



