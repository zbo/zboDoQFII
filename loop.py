import csv
import urllib3
from selenium import webdriver

browser = webdriver.Chrome()

def web_call(link, instance):
    try:
        browser.get(link)
        qfii_table = browser.find_element_by_id('tb_cgtj')
        qfii_body = qfii_table.find_element_by_tag_name('tbody')
        qfii_row = qfii_body.find_elements_by_tag_name('tr')
        if len(qfii_row) == 1:  # QUID 为空
            return False
        row = qfii_row[0]
        cells = row.find_elements_by_tag_name('td')
        one = cells[7]
        five = cells[8]
        ten = cells[9]
        if color(one) == 'green':
            return False

        # 单日转折
        if color(one) == 'red' and color(five) == 'green':
            print('单日转折'+'-'+instance[1])
            print(link)

        # 五日转折
        if color(five) == 'red' and color(ten) == 'green':
            print('五日转折'+'-'+instance[1])
            print(link)

        # 十日转折
        if color(one) == 'red' and color(five) == 'red' and color(ten) == 'red':
            print('十日转折'+'-'+instance[1])
            print(link)

        return True

    except Exception:
        print(link)


def color(td):
    return td.find_element_by_tag_name('span').get_attribute('class')


def http_call(link):
    http = urllib3.PoolManager()
    r = http.request('GET', link)
    print(r)


def do(one):
    pair = one[0].split('.')
    link = '''http://data.eastmoney.com/hsgtcg/StockHdStatistics.aspx?stock={0}'''.format(pair[0])
    # http_call(link)
    web_call(link, one)


if __name__ == '__main__':

    reader = csv.reader(open('11-18.csv', 'r', encoding='GBK'))
    for sb in reader:
        if sb[0] == '股票代码':
            continue
        do(sb)

