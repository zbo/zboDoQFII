import csv
import urllib3
import time
from selenium import webdriver

browser = webdriver.Chrome()


def contain_stock(all, title):
    for s in all:
        if str(title).find(s) != -1:
            return True
    return False

def yanbao_approach(link, s):
    try:
        browser.get(link)
        # button = browser.find_element_by_link_text('最新研报')
        button = browser.find_element_by_link_text('公司研究')
        # button = browser.find_element_by_link_text('行业研究')
        button.click()
        for i in range(100):
            yanbao_div = browser.find_element_by_class_name('yb_con')
            items = yanbao_div.find_elements_by_tag_name('li')
            for item in items:
                try:
                    title = item.find_element_by_tag_name('a').get_attribute('title')
                    time_span = item.find_element_by_tag_name('span').text
                    if contain_stock(s, title):
                        print('{0}     {1}'.format(title, time_span))
                except Exception as e:
                    print('---------------------------------------')
            button = browser.find_element_by_link_text('下一页')
            button.click()
            print('第' + str(i) + '页')
    except Exception as e:
        pass


def do(stocks):
    link = '''http://istock.jrj.com.cn/yanbao.html'''
    yanbao_approach(link, stocks)


if __name__ == '__main__':
    reader = csv.reader(open('11-18.csv', 'r', encoding='GBK'))
    all_stocks = []
    for sb in reader:
        all_stocks.append(sb[1])
    do(all_stocks)

