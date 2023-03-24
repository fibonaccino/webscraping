import requests
from bs4 import BeautifulSoup
import csv
import time

# def extract_table_data(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     csstab = soup.select_one('#spot-list > ul > li:nth-child(1) > div.spot-content > div.spot-text > dl > dt > a > span')
#     rows = csstab.select('tr')
#
# #spot-list > ul > li:nth-child(1) > div.spot-content > div.spot-text > dl > dt > a > span
# #__next > div > div.ThreeColumnsLayout-body-1V4am.ThreeColumnsLayout-keep-right-column-y4vud'
#                              '.
#     data = []
#     for row in rows:
#         cols = row.select('td')
#         cols = [col.text for col in cols]
#         data.append(cols)
#
#     return data

def main():
    print("=== Start Scraping ===")
    # cnt = 1
    # ken = str(cnt).zfill(2)
    # print(ken)
    for i in range(1,48):
        ken = str(i).zfill(2)
        sw = True
        num = 1
        jin = []
        pagewk = []
        while sw:
            res = requests.get(f"https://www.navitime.co.jp/category/0705002/{ken}/?page={num}")
            soup = BeautifulSoup(res.text, 'html.parser')

            title = soup.select_one('#main-title')          # 都道府県
            # print("==A==")
            if num == 1:
                # print("==B==")
                print(title.contents[0])

            # page = soup.select('#body-left > ul.paging-section ')
            pages = len(soup.select('#body-left > ul.paging-section > li'))

            page = soup.select('#body-left > ul.paging-section > li > a')
            # page3 = soup.find_all("a")
            # print("===",page)
            # pagewk = []
            for j in range(len(page)):
                if page[j].text.isnumeric():
                    pagewk.append(int(page[j].text))
            # print(pagewk)
            page_max = max(pagewk)
            # print(page_max)
            num += 1
            if num > page_max :
                sw = False


            k = len(soup.select('#spot-list > ul > li'))
            for l in range(1,k + 1):
                wk = f'#spot-list > ul > li:nth-child({str(l)}) > div.spot-content > div.spot-text > dl > dt > a > span'
                # print(wk)
                csstab = soup.select_one(wk)
                jin.append(str(csstab.contents[0]))
                # print(csstab.contents)
        print(jin)



    # レスポンスの HTML から BeautifulSoup オブジェクトを作る
    # csstab = soup.select('#spot-list > ul > li')
    # csstab = soup.select_one('#spot-list > ul > li:nth-of-type(1) > div.spot-content > div.spot-text > dl > dt > a > span')
    # jinjya = soup.find_all('#spot-list > ul > li:nth-of-type(1) > div.spot-content > div.spot-text > dl > dt > a > span')
    #
    # print(jinjya)

    # table_data = extract_table_data(res.text)
    #
    # with open("exchange_rates2.csv", "w", newline="") as f:
    #     writer = csv.writer(f)
    #     writer.writerows(table_data)
    #
    # print("=== CSV file created successfully ===")
    # print("=== End   Reuters rates scraping  ===")
    print("=== End   Scraping ===")

if __name__ == '__main__':
    main()
