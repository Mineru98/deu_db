# -*- coding:utf-8 -*-
import json
import random
import numpy as np
from tqdm import tqdm
from itertools import groupby

with open("result.json", "r", encoding="utf-8") as f:
    rows = json.load(f)


def list_chunk(lst, n):
    return [lst[i : i + n] for i in range(0, len(lst), n)]


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

with open("./CREATE_Company.sql", "w", encoding="utf-8") as f:
    f.writelines(result)

result = ""

artist_list = []
song_list = []
song_idx = 1
for idx, row in enumerate(rows):
    artist_id = idx + 1
    artist_list.append(
        {
            "artist_id": artist_id,
            "company_id": random.choice(company_idx_list),
            "artist_name": row["artist"].replace("'", ""),
        }
    )
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

with open("./CREATE_Artist.sql", "w", encoding="utf-8") as f:
    f.writelines(result)

result = ""

song_sql = "\n".join(
    [
        f"INSERT INTO \"Song\" (\"song_id\", \"song_name\", \"play_time\") VALUES ({row['song_id']}, '{row['song_name']}', {row['play_time']});"
        for idx, row in enumerate(song_list)
    ]
)

result += song_sql + "\n\n"

with open("./CREATE_Song.sql", "w", encoding="utf-8") as f:
    f.writelines(result)

result = ""

album_list = []
album_tract_list = []
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
        album_list.append(album_item)
        items = list(items)
        random.shuffle(items)
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

with open("./CREATE_Album.sql", "w", encoding="utf-8") as f:
    f.writelines(result)

result = ""


album_tract_sql = "\n".join(
    [
        f"INSERT INTO \"AlbumTract\" (\"album_id\", \"song_id\", \"order_num\") VALUES ({row['album_id']}, {row['song_id']}, {row['order_num']});"
        for idx, row in enumerate(album_tract_list)
    ]
)

result += album_tract_sql + "\n\n"

with open("./CREATE_AlbumTract.sql", "w", encoding="utf-8") as f:
    f.writelines(result)

result = ""
