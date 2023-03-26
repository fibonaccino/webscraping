import requests
from bs4 import BeautifulSoup
import csv
import datetime

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
    start = datetime.datetime.now()
    print(f"=== Start Scraping {start} ===")

    for i in range(1,48):
        ken = str(i).zfill(2)
        sw = True
        num = 1
        data = []
        pagewk = {1}
        while sw:
            res = requests.get(f"https://www.navitime.co.jp/category/0705002/{ken}/?page={num}")
            soup = BeautifulSoup(res.text, 'html.parser')

            titlewk = soup.select_one('#main-title')          # 都道府県
            # print("==A==")
            if num == 1:
                # print("==B==")
                if titlewk.contents[0] is None:
                    title = ""
                else:
                    title = titlewk.contents[0]
                print(title)
            # page = soup.select('#body-left > ul.paging-section ')
            pages = len(soup.select('#body-left > ul.paging-section > li'))

            page = soup.select('#body-left > ul.paging-section > li > a')
            # page3 = soup.find_all("a")
            # print("===",page)
            pagewk2 = []
            for j in range(len(page)):
                if page[j].text.isnumeric():
                    # pagewk.append(int(page[j].text))
                    pagewk2.append(int(page[j].text))
            # print(pagewk)
            pagewk = pagewk | set(pagewk2)
            page_max = max(pagewk)
            # print(page_max)
            num += 1
            if num > page_max :
                sw = False

            k = len(soup.select('#spot-list > ul > li'))
            for l in range(1,k + 1):
                wk = f'#spot-list > ul > li:nth-child({str(l)}) > div.spot-content > div.spot-text > dl > dt > a > span'
                # print(wk)
                name_text = soup.select_one(wk)
                name = str(name_text.contents[0])
                wk = f'#spot-list > ul > li:nth-child({str(l)}) > div.spot-content > div.spot-text > dl > dt > a '
                hp_text = soup.select_one(wk)
                # print(hp_text)
                hp = hp_text.get("href")
                # print("●：",hp)
                # name_text = soup.select_one(wk) 
                # name = str(name_text.contents[0])
                # print(name)
                # wk = f'#spot-list > ul > li:nth-child({str(l)}) > div.spot-content > div.spot-text > dl > dd > dl > dd'
                wk = f'#spot-list > ul > li:nth-child({str(l)}) > div.spot-content > div.spot-text > dl > dd > dl > dd:nth-child(2) > span'
                dd = soup.select_one(wk)
                if str(dd.contents[0]) is None :
                    jusyo = ""
                else:
                    jusyo = str(dd.contents[0])
                # print(jusyo)
                # wk = f'#spot-list > ul > li:nth-child({str(l)}) > div.spot-content > div.spot-text > dl > dd > dl > dd:nth-child(3) > span'
                wk = f'#spot-list > ul > li:nth-child({str(l)}) > div.spot-content > div.spot-text > dl > dd:nth-child(2) > dl > dd:nth-child(4) > span'
                dd = soup.select_one(wk)
                if dd is None:
                    tel = ""
                # print(dd)
                # print(str(dd.contents[0]))
                elif str(dd.contents[0]) is None :
                    tel = ""
                else:
                    tel = str(dd.contents[0])
                # print(tel)
                data.append([title,name,hp,jusyo,tel])

                # print('---')
                # print(dd[0].contents[0],"-",dd[1].contents[0])
                # print('===')
                # print(csstab.contents)

        # print(data)
        with open('jinjya_list.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerows(data)
        f.close()


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

    print(f"=== End   Scraping {datetime.datetime.now()} Eraps : {datetime.datetime.now() - start} ===")

if __name__ == '__main__':
    main()
