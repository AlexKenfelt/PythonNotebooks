"""
2. Lav en metode der returnerer top 5 mest populære opskrifter fra nemlig.com.
https://www.nemlig.com/

3. Lav en metode der kan finde den totale pris af disse fire udvalgte varer på nemlig.com
(Gær, Minimælk, Banan, Tomatpasta)

4. Lav et barchart over alle Womens Fiction bøgerne på følgende hjemmeside. Sorter efter pris.
http://books.toscrape.com/index.html
"""
from shutil import which
from selenium import webdriver
from bs4 import BeautifulSoup
from bs4.element import Comment

#--------------------------------------------- task 1 -----------------------------------------------------------------

class Webscraper () :
    
    def __init__(self, url):
        self.url = url
    
    def init_webdriver(self):
        FIREFOXPATH = which("firefox")
        CHROMEPATH = which("chrome") or which("chromium")
        """Simple Function to initialize and configure Webdriver"""
        if FIREFOXPATH != None:
            print(FIREFOXPATH)#cm
            from selenium.webdriver.firefox.options import Options

            options = Options()
            options.binary = FIREFOXPATH
            options.add_argument("-headless")
            return webdriver.Firefox(firefox_options=options, log_path="geckodriver.log")

        elif CHROMEPATH != None:
            print(CHROMEPATH)#cm
            from selenium.webdriver.chrome.options import Options

            options = Options()
            options.binary_location = CHROMEPATH
            options.add_argument("--headless")
            return webdriver.Chrome(chrome_options=options, service_args=['--verbose'], service_log_path="chromedriver.log")

    def isItFriday(self):

        driver = class_instance.init_webdriver()
        driver.get(self.url)
        driver.implicitly_wait(5)

        return driver.page_source

    def tag_visible(self, element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
         return False
        if isinstance(element, Comment):
         return False
        return True

    def text_from_html(self):
        soup = BeautifulSoup(class_instance.isItFriday(), 'html.parser')
        texts = soup.findAll(text=True)
        visible_texts = filter(class_instance.tag_visible, texts)  
        return u" ".join(t.strip() for t in visible_texts)

url = 'https://www.erdetfredag.dk/'
class_instance = Webscraper(url)
print('--- task 1 ---')

print(class_instance.text_from_html())
#print(class_instance.isItFriday())

#------------------------------------------------ task 2 -----------------------------------------------------------------