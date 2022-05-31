# pip install selenium
from selenium import webdriver
# pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager
# pip install beautifulsoup4
from bs4 import BeautifulSoup

import datetime

#https://www.simply-hentai.com/tags/page-1

def main():
    time = "Tags\t" + str(datetime.date.today())
    print(time)
    name = "Tags " + str(datetime.date.today()) + ".txt"
    data = open(name, "w", encoding="utf-8")
    data.write(time)

    for n in range(1, 16):
        b = str(n)

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.simply-hentai.com/tags/page-" + b)
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, 'lxml')

        titles = soup.findAll("a", class_="is-trigger ism-trigger")

        data.write("\npage " + b)
        tit = 0
        for title in titles[:24]:
            res = str('\nTitle: {}'.format(titles[tit + 1].text))
            data.write(res)
            print(res)
            tit += 2


    data.close()

if __name__ == '__main__':
    main()
