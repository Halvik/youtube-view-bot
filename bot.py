import time;
from selenium import webdriver;


#time to refresh page
Timer = 3 #(3 seconds)

#youtube link
link = 'https://www.youtube.com/watch?v=6ZWNYZ_kTTw'

#number of views
views = 100


driver = webdriver.Chrome()
driver.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()
    print(i)