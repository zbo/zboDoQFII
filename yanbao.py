import csv
import urllib3
import time
from selenium import webdriver

browser = webdriver.Chrome()


def yanbao_approach(link):
    try:
        browser.get(link)
        button = browser.find_element_by_link_text('最新研报')
        button.click()
        for i in range(100):
            yanbao_div = browser.find_element_by_class_name('yb_con')
            items = yanbao_div.find_elements_by_tag_name('li')
            for item in items:
                try:
                    title = item.find_element_by_tag_name('a').get_attribute('title')
                    time = item.find_element_by_tag_name('span').text
                    print('{0}     {1}'.format(title, time))
                except Exception as e:
                    print('---------------------------------------')
            button = browser.find_element_by_link_text('下一页')
            button.click()
            print('第' + str(i) + '页')
    except Exception as e:
        pass


def do():
    link = '''http://istock.jrj.com.cn/yanbao.html'''
    yanbao_approach(link)


if __name__ == '__main__':
    do()

