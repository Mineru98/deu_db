# -*- coding:utf-8 -*-
import json
import time
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup

from selenium import webdriver
import chromedriver_autoinstaller


def 가수_공연_수집():
    result = {}
    beginPage = 1
    endPage = 1

    cookies = {
        'ASPSESSIONIDQABRCRSB': 'HALBJOACGFEOGIBKMBHHOEIH',
        'pcid': '168433348568136130',
        "ab.storage.deviceId.cd97b079-ff05-4967-873a-324050c2a198": "%7B%22g%22%3A%2269fc662d-cd51-e4bd-af74-ca176b081212%22%2C%22c%22%3A1681697712586%2C%22l%22%3A1683646298430%7D",
        "ab.storage.sessionId.cd97b079-ff05-4967-873a-324050c2a198": "%7B%22g%22%3A%22780c740b-4768-ba5a-ab19-b528eb613a0e%22%2C%22e%22%3A1683648101855%2C%22c%22%3A1683646298430%2C%22l%22%3A1683646301855%7D",
    }

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Referer": "http://www.playdb.co.kr/artistdb/list.asp?code=013001",
        "Upgrade-Insecure-Requests": "1",
    }

    params = {
        "code": "013001",
        "sub_code": "",
        "ImportantSelect": "",
        "ClickCnt": "Y",
        "NameSort": "",
        "Country": "Y",
        "Page": str(beginPage),
        "TKPower": "",
        "WeekClickCnt": "",
        "NameEnd": "",
        "NameStart": "",
    }
    res = requests.get(
        "http://www.playdb.co.kr/artistdb/list_iframe.asp",
        params=params,
        cookies=cookies,
        headers=headers,
        verify=False,
    )
    soup = BeautifulSoup(res.content, "lxml")
    rows = soup.find_all("tr")
    last_row = rows[len(rows) - 1].text
    endPage = int(last_row.split("/")[1].replace("]", ""))
    for page in tqdm(range(beginPage, endPage + 1)):
        params["Page"] = str(page)
        res = requests.get(
            "http://www.playdb.co.kr/artistdb/list_iframe.asp",
            params=params,
            cookies=cookies,
            headers=headers,
            verify=False,
        )
        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text, "lxml")
        tbody = soup.find("table")
        try:
            rows = list(tbody.children)
            rows = rows[5 : len(rows) - 11]
            for idx in range(0, len(rows), 8):
                item = rows[idx].find("table").find_all("td")
                Artist = str(item[0].find_all("a")[1].text).strip()
                result[Artist] = list(map(lambda x: x.text, item[6].find_all("a")))
        except Exception as e:
            print(page)

    with open("Artist.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)


def 가수_곡_수집():
    chromedriver_autoinstaller.install()
    song_list = {}
    with open("Artist.json", "r", encoding="utf-8") as f:
        rows = json.load(f)
    count = 0
    for Artist in tqdm(list(rows.keys())):
        song_list[Artist] = []
        params = {
            "strType": "2",
            "natType": "KOR",
            "strText": Artist,
            "strCond": "0",
            "searchOrderType": "",
            "searchOrderItem": "",
            "intPage": 1,
        }

        res = requests.get(
            "https://www.tjmedia.com/tjsong/song_search_list.asp",
            params=params,
        )
        soup = BeautifulSoup(res.content, "lxml")
        pagination = soup.find("div", {"id": "page1"})
        try:
            pages = pagination.find_all("a")
            endPage = int(pages[len(pages) - 1].text.replace("[", "").replace("]", ""))
            for page in range(1, endPage + 1):
                params["intPage"] = page
                if count % 25 == 0 and count != 0:
                    time.sleep(4)
                res = requests.get(
                    "https://www.tjmedia.com/tjsong/song_search_list.asp",
                    params=params,
                )
                res.encoding = "utf-8"
                soup = BeautifulSoup(
                    res.text,
                    "lxml",
                )
                table = soup.find("div", {"id": "BoardType1"})
                rows = table.find_all("tr")[1:]
                count += 1
                for row in rows:
                    song_list[Artist].append(
                        {
                            "song_name": row.find_all("td")[1].text,
                            "youtube_url": "https://www.youtube.com/@TJKaraoke/search?query="
                            + row.find_all("td")[0].text,
                        }
                    )
        except:
            pass
    

    with open("SongList.json", "w", encoding="utf-8") as f:
        json.dump(song_list, f, ensure_ascii=False, indent=4)
        
def 곡_재생시간_수집():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("headless")
    chrome_options.add_argument("--start-minimized")
    driver = webdriver.Chrome(options=chrome_options)
    
    with open("SongList.json", "r", encoding="utf-8") as f:
        song_list = json.load(f)
    
    for key in tqdm(song_list.keys()):
        for idx in range(len(song_list[key])):
            song = song_list[key][idx]
            driver.get(song["youtube_url"])
            soup_source = BeautifulSoup(driver.page_source, "lxml")
            try:
                items = soup_source.find_all("span", {"id": "text"})
                if len(items) > 0:
                    song_list[key][idx]["playtime"] = str(items[0].text).strip()
            except Exception as e:
                print(e)
                break

    with open("SongList_with_playtime.json", "w", encoding="utf-8") as f:
        json.dump(song_list, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    곡_재생시간_수집()
