# -*- coding:utf-8 -*-
import os
import json
import random
import numpy as np
from tqdm import tqdm
from itertools import groupby

from datetime import datetime, timedelta

name_list = [
    "정호준",
    "봉홍석",
    "예문수",
    "성보연",
    "최민하",
    "손진희",
    "남병희",
    "임시정",
    "신명훈",
    "황명우",
    "하민규",
    "배주은",
    "임인영",
    "황보범석",
    "전원웅",
    "전범준",
    "최선아",
    "설영재",
    "추시영",
    "배유영",
    "고예영",
    "김주미",
    "류보연",
    "노윤진",
    "정원숙",
    "류윤숙",
    "최원옥",
    "장병하",
    "안재빈",
    "정기환",
    "유빛가람",
    "서미르",
    "고우람",
    "남미르",
    "하한결",
    "표샘",
    "심힘찬",
    "남나길",
    "탁나길",
    "송다운",
    "노으뜸",
    "설다운",
    "노한길",
    "백나라우람",
    "신우람",
    "전빛가람",
    "성달",
    "신으뜸",
    "신믿음",
    "권달",
    "최한길",
    "봉샘",
    "백미르",
    "허미르",
    "황보다운",
    "허나라우람",
    "예믿음",
    "양빛가람",
    "정우람",
    "최우람",
    "고꽃",
    "복이슬",
    "남나라빛",
    "류민들레",
    "황누리",
    "황비",
    "황보나봄",
    "최새롬",
    "문라온",
    "성아리",
    "백자람",
    "류누리",
    "탁비",
    "배나빛",
    "김단비",
    "하보름",
    "유새론",
    "홍단비",
    "풍별찌",
    "탁산다라",
    "남다래",
    "임라움",
    "정나비",
    "예조은",
    "신조은",
    "류한별",
    "서비",
    "심꽃",
    "송여름",
    "서한샘",
    "손철",
    "한웅",
    "강혁",
    "정호",
    "성웅",
    "김훈",
    "황광",
    "표건",
    "심건",
    "김훈",
    "서훈",
    "권광",
    "사공웅",
    "풍광",
    "손건",
    "안건",
    "유웅",
    "정철",
    "황철",
    "제갈혁",
    "봉혁",
    "제갈혁",
    "백훈",
    "장건",
    "윤훈",
    "송호",
    "윤웅",
    "서건",
    "설광",
    "박훈",
    "문설",
    "류리",
    "하은",
    "배은",
    "한린",
    "허성",
    "홍란",
    "한상",
    "노재",
    "탁린",
    "한리",
    "송리",
    "정지",
    "양성",
    "심은",
    "장은",
    "복설",
    "문재",
    "풍설",
    "조진",
    "서성",
    "정현",
    "남궁성",
    "정재",
    "정지",
    "심리",
    "추설",
    "이현",
    "황상",
    "풍진",
    "사공승헌",
    "안광조",
    "강철순",
    "백무열",
    "황재범",
    "최이수",
    "배남규",
    "이철순",
    "황동건",
    "풍재범",
    "강무열",
    "윤병헌",
    "양승헌",
    "권경택",
    "노무영",
    "윤철순",
    "추경구",
    "하동건",
    "최경택",
    "풍일성",
    "풍무열",
    "한현승",
    "안재범",
    "오이수",
    "하무영",
    "사공재범",
    "조오성",
    "이오성",
    "배승헌",
    "표철순",
    "정재인",
    "남궁혜림",
    "장애정",
    "강은채",
    "윤은채",
    "강영신",
    "황보이경",
    "장영신",
    "제갈유리",
    "성영애",
    "사공지해",
    "백재인",
    "신재인",
    "예숙자",
    "정자경",
    "성영신",
    "노나영",
    "이경님",
    "제갈재신",
    "전지해",
    "홍지해",
    "예재인",
    "남궁영신",
    "탁재인",
    "추재인",
    "노남순",
    "복미란",
    "김지해",
    "황보장미",
    "허미래",
]


location_list = [
    "서울특별시",
    "부산광역시",
    "대구광역시",
    "인천광역시",
    "광주광역시",
    "대전광역시",
    "울산광역시",
    "세종특별자치시",
    "경기도",
    "강원도",
    "충청북도",
    "충청남도",
    "전라북도",
    "전라남도",
    "경상북도",
    "경상남도",
    "제주특별자치도",
]


def generate_random_gender():
    genders = ["남자", "남자", "남자", "여자", "여자", "여자", "여자", "여자", "여자", "여자"]  # 가능한 성별 목록

    random_gender = random.choice(genders)  # 성별 목록에서 랜덤으로 선택

    return random_gender


def generate_random_cancel():
    is_cancel = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]  # 가능한 성별 목록

    random_gender = random.choice(is_cancel)  # 성별 목록에서 랜덤으로 선택

    return random_gender


def generate_random_date():
    start_date = datetime(2019, 1, 1)  # 시작 날짜 설정
    end_date = datetime(2023, 12, 31)  # 종료 날짜 설정

    # 시작 날짜와 종료 날짜 사이에서 랜덤으로 날짜 선택
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

    return random_date.strftime("%Y-%m-%d")


def generate_random_birthday():
    start_date = datetime(1980, 1, 1)  # 시작 날짜 설정
    end_date = datetime(2005, 12, 31)  # 종료 날짜 설정

    # 시작 날짜와 종료 날짜 사이에서 랜덤으로 날짜 선택
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

    return random_date.strftime("%Y-%m-%d")


def generate_number_array(start=10000, end=30000, step=1000):
    number_array = list(range(start, end + 1, step))
    return random.choice(number_array)


def list_chunk(lst, n):
    return [lst[i : i + n] for i in range(0, len(lst), n)]


with open("result.json", "r", encoding="utf-8") as f:
    rows = json.load(f)


year_list = [2023, 2022, 2021, 2020, 2019]
result = ""
company_list = [
    (1, "HYBE Corporation", "2005"),
    (2, "SM Corporation", "1995"),
    (3, "JYP Corporation", "1990"),
    (4, "Cube Entertainment", "1996"),
    (5, "Stone Music Entertainment", "1996"),
    (6, "FNC Entertainment", "1996"),
    (7, "Starship Entertainment", "1996"),
    (8, "Pledis Entertainment", "2007"),
]
company_idx_list = list(map(lambda x: x[0], company_list))
artist_idx_list = np.arange(1, len(rows) + 1)
artist_idx_list = artist_idx_list.tolist()
for idx, row in enumerate(rows):
    artist_idx_list[idx] = (artist_idx_list[idx], row["artist"])

sql = 'INSERT INTO "Company" ("company_id", "company_name", "year_estbl") VALUES (:1, \':2\', TO_DATE(:3, \'YYYY\'));'

company_sql = "\n".join(
    [
        sql.replace(":1", str(idx)).replace(":2", name).replace(":3", year)
        for _, (idx, name, year) in enumerate(company_list)
    ]
)

result += company_sql + "\n\n"

with open("./01_CREATE_Company.sql", "w", encoding="utf-8") as f:
    f.writelines(result)

result = ""

artist_list = []
song_list = []
concert_list = []
song_idx = 1
concert_idx = 1
for idx, row in enumerate(rows):
    artist_id = idx + 1
    company_idx = random.choice(company_idx_list)
    artist_list.append(
        {
            "artist_id": artist_id,
            "company_id": company_idx,
            "artist_name": row["artist"].replace("'", ""),
        }
    )
    for concert in row["concert"]:
        concert_date = "TO_DATE('" + generate_random_date() + "', 'YYYY-MM-DD')"
        concert_list.append(
            {
                "concert_id": concert_idx,
                "concert_title": concert.split("(")[0],
                "concert_date": concert_date,
                "capacity": generate_number_array(100, 1000, 1),
                "artist_id": artist_id,
                "company_id": company_idx,
            }
        )
        concert_idx += 1
    for song in row["song"]:
        play_time_split = song["playtime"].split(":")
        if len(play_time_split) == 2:
            minute, sec = play_time_split
            minute = int(minute)
            sec = int(sec)
            play_time = minute * 60 + sec
            song_list.append(
                {
                    "artist_id": artist_id,
                    "song_id": song_idx,
                    "song_name": song["song_name"].replace("'", ""),
                    "play_time": play_time,
                }
            )
            song_idx += 1
artist_sql = "\n".join(
    [
        f"INSERT INTO \"Artist\" (\"artist_id\", \"company_id\", \"artist_name\", \"solo_act_status\") VALUES ({row['artist_id']}, {row['company_id']}, '{row['artist_name']}', 0);"
        for idx, row in enumerate(artist_list)
    ]
)

result += artist_sql + "\n\n"

with open("./02_CREATE_Artist.sql", "w", encoding="utf-8") as f:
    f.writelines(result)

result = ""

song_sql = "\n".join(
    [
        f"INSERT INTO \"Song\" (\"song_id\", \"song_name\", \"play_time\") VALUES ({row['song_id']}, '{row['song_name']}', {row['play_time']});"
        for idx, row in enumerate(song_list)
    ]
)

result += song_sql + "\n\n"

with open("./03_CREATE_Song.sql", "w", encoding="utf-8") as f:
    f.writelines(result)

result = ""

album_list = []
album_tract_list = []
artist_with_song_dic = {}
album_price_dic = {}
concert_price_dic = {}
group = groupby(song_list, lambda x: x["artist_id"])
album_id = 1
for artist_id, items in group:
    artist_item = list(filter(lambda x: x["artist_id"] == artist_id, artist_list))
    if len(artist_item) == 1:
        album_item = {
            "album_id": album_id,
            "album_title": "앨범_" + str(album_id),
            "album_pbl_date": "TO_DATE(" + str(random.choice(year_list)) + ", 'YYYY')",
            "artist_id": artist_id,
            "company_id": artist_item[0]["company_id"],
        }
        album_price_dic[album_id] = generate_number_array(10000, 40000, 2500)
        album_list.append(album_item)
        items = list(items)
        random.shuffle(items)
        artist_with_song_dic[artist_id] = items
        list_chunked = list_chunk(items, 5)
        for _, row in enumerate(list_chunked):
            for idx, item in enumerate(row):
                album_tract_list.append(
                    {"album_id": album_id, "song_id": item["song_id"], "order_num": idx + 1}
                )
        album_id += 1

album_sql = "\n".join(
    [
        f"INSERT INTO \"Album\" (\"album_id\", \"album_title\", \"album_pbl_date\", \"artist_id\", \"company_id\") VALUES ({row['album_id']}, '{row['album_title']}', {row['album_pbl_date']}, {row['artist_id']}, {row['company_id']});"
        for idx, row in enumerate(album_list)
    ]
)

result += album_sql + "\n\n"

with open("./04_CREATE_Album.sql", "w", encoding="utf-8") as f:
    f.writelines(result)

result = ""

album_tract_sql = "\n".join(
    [
        f"INSERT INTO \"AlbumTract\" (\"album_id\", \"song_id\", \"order_num\") VALUES ({row['album_id']}, {row['song_id']}, {row['order_num']});"
        for idx, row in enumerate(album_tract_list)
    ]
)

result += album_tract_sql + "\n\n"

with open("./05_CREATE_AlbumTract.sql", "w", encoding="utf-8") as f:
    f.writelines(result)

result = ""

concert_tract_list = []
group = groupby(concert_list, lambda x: x["artist_id"])
concert_id = 1
for artist_id, items in group:
    for _, concert in enumerate(items):
        try:
            song_list = artist_with_song_dic[artist_id]
            for idx, song in enumerate(song_list[:6]):
                concert_price_dic[concert["concert_id"]] = generate_number_array(
                    30000, 100000, 5000
                )
                concert_tract_list.append(
                    {
                        "song_id": song["song_id"],
                        "concert_id": concert["concert_id"],
                        "order_num": idx + 1,
                    }
                )
        except:
            pass

concert_sql = "\n".join(
    [
        f"INSERT INTO \"Concert\" (\"concert_id\", \"concert_title\", \"concert_date\", \"capacity\", \"artist_id\", \"company_id\") VALUES ({row['concert_id']}, '{row['concert_title']}', {row['concert_date']}, {row['capacity']}, {row['artist_id']}, {row['company_id']});"
        for idx, row in enumerate(concert_list)
    ]
)

result += concert_sql + "\n\n"

with open("./06_CREATE_Concert.sql", "w", encoding="utf-8") as f:
    f.writelines(result)

result = ""

concert_tract_sql = "\n".join(
    [
        f"INSERT INTO \"ConcertTract\" (\"concert_id\", \"song_id\", \"order_num\") VALUES ({row['concert_id']}, {row['song_id']}, {row['order_num']});"
        for idx, row in enumerate(concert_tract_list)
    ]
)

result += concert_tract_sql + "\n\n"

with open("./07_CREATE_ConcertTract.sql", "w", encoding="utf-8") as f:
    f.writelines(result)


fan_list = []

fan_idx = 1
for idx, name in enumerate(name_list):
    for _ in range(50):
        fan_list.append(
            {
                "fan_id": fan_idx,
                "fan_name": name,
                "gender": generate_random_gender(),
                "birthday": "TO_DATE('" + str(generate_random_birthday()) + "', 'YYYY-MM-DD')",
                "location": random.choice(location_list),
            }
        )
        fan_idx += fan_idx

random.shuffle(fan_list)

new_fan_list = []
for fan_id, row in enumerate(fan_list):
    new_fan_list.append(
        {
            "fan_id": fan_id,
            "fan_name": row["fan_name"],
            "gender": row["gender"],
            "birthday": row["birthday"],
            "location": row["location"],
        }
    )

fan_list = new_fan_list

result = ""

fan_sql = "\n".join(
    [
        f"INSERT INTO \"Fan\" (\"fan_id\", \"fan_name\", \"gender\", \"birthday\", \"birthday\") VALUES ({row['fan_id']}, '{row['fan_name']}', '{row['gender']}', {row['birthday']}, '{row['location']}');"
        for idx, row in enumerate(fan_list)
    ]
)

result += fan_sql + "\n\n"

with open("./08_CREATE_Fan.sql", "w", encoding="utf-8") as f:
    f.writelines(result)


album_sales_list = []

for _, album in tqdm(enumerate(album_list), total=len(album_list)):
    price = album_price_dic[album["album_id"]]
    for _ in range(0, random.randint(100, 1000)):
        fan = random.choice(fan_list)
        album_sales_list.append(
            {
                "fan_id": fan["fan_id"],
                "album_id": album["album_id"],
                "price": price,
                "payment_date": album["album_pbl_date"],
                "is_canceled": generate_random_cancel(),
            }
        )

result = ""
album_sales_sql = "\n".join(
    [
        f"INSERT INTO \"AlbumSales\" (\"fan_id\", \"album_id\", \"price\", \"payment_date\", \"is_canceled\") VALUES ({row['fan_id']}, '{row['album_id']}', '{row['price']}', {row['payment_date']}, '{row['is_canceled']}');"
        for idx, row in tqdm(enumerate(album_sales_list), total=len(album_sales_list))
    ]
)
result += album_sales_sql + "\n\n"

with open("./09_CREATE_AlbumSales.sql", "w", encoding="utf-8") as f:
    f.writelines(result)

concert_ticket_list = []

for idx, concert in tqdm(enumerate(concert_list), total=len(concert_list)):
    try:
        price = concert_price_dic[concert["concert_id"]]
        for _ in range(0, random.randint(100, 1000)):
            sheet_level = generate_number_array(1, 4, 1)
            fan = random.choice(fan_list)
            concert_ticket_list.append(
                {
                    "fan_id": fan["fan_id"],
                    "concert_id": concert["concert_id"],
                    "ticket_price": price + sheet_level * 10000,
                    "sheet_level": sheet_level,
                    "sheet_num": "A" + str(idx + 1),
                    "payment_date": concert["concert_date"],
                    "is_canceled": generate_random_cancel(),
                }
            )
    except:
        pass
result = ""
concert_ticket_sql = "\n".join(
    [
        f"INSERT INTO \"ConcertTicket\" (\"fan_id\", \"concert_id\", \"ticket_price\", \"sheet_level\", \"sheet_num\", \"payment_date\", \"is_canceled\") VALUES ({row['fan_id']}, '{row['concert_id']}', '{row['ticket_price']}', {row['sheet_level']}, {row['sheet_num']}, {row['payment_date']}, '{row['is_canceled']}');"
        for idx, row in tqdm(enumerate(concert_ticket_list), total=len(concert_ticket_list))
    ]
)
result += concert_ticket_sql + "\n\n"

with open("./10_CREATE_ConcertTicket.sql", "w", encoding="utf-8") as f:
    f.writelines(result)

sql_files = [file for file in os.listdir("./") if file.endswith(".sql") and file != "CREATE.sql"]
sql_files.sort(reverse=False)

with open("./CREATE.sql", "w") as output:
    for file in tqdm(sql_files):
        file_path = os.path.join("./", file)
        with open(file_path, "r") as input_file:
            output.write(input_file.read())
