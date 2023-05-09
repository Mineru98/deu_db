# -*- coding:utf-8 -*-
import json
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup


def 가수수집():
    result = {}
    beginPage = 1
    endPage = 1

    cookies = {
        "pcid": "168169771036894987",
        "ASPSESSIONIDQAQSAAQC": "JEGDJIMAOLOIMGLJPJJANJBL",
        "ASPSESSIONIDSACRARTB": "BIJABNKANMDJNBKOCPOBJEOE",
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
        soup = BeautifulSoup(res.content, "lxml")
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


가수수집()
