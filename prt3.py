from threading import Thread
from bs4 import BeautifulSoup as BS
import lxml
import time
import requests

def get_html(link):
    time.sleep(1)
    response = requests.get(link).text
    print(response)

links = ("https://github.com/dashboard", "https://pythontutor.ru/", "https://dzen.ru/?clid=2255080&from=dist_bookmark&win=480&yredirect=true", "https://relizua.com/", "https://travel.yandex.ru/avia/" )

threads = [Thread(target=get_html, args=(links[i],)) for i in range(5)]

start_1 = time.time()
for t in threads:
    t.start()
for t in threads:
    t.join()
end_1 = time.time()

start_2 = time.time()
for link in links:
    get_html(link)
end_2 = time.time()
print(f"Время выполнения параллельного запуска {end_1 - start_1} секунд")
print(f"Время выполнения последовательного запуска {end_2 - start_2} секунд")
