# -*- coding:utf-8 -*-
import json
import random
import numpy as np
from tqdm import tqdm

with open("result.json", "r", encoding="utf-8") as f:
    rows = json.load(f)


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

sql = "INSERT INTO Company (company_id, company_name, year_estbl) VALUES (:1, :2, TO_DATE(:3, 'YYYY'));"

company_sql = "\n".join(
    [
        sql.replace(":1", str(idx)).replace(":2", name).replace(":3", year)
        for _, (idx, name, year) in enumerate(company_list)
    ]
)

result += company_sql + "\n\n"

artist_sql = "\n".join(
    [
        f"INSERT INTO Artist (artist_id, company_id, artist_name, solo_act_status) VALUES ({artist_idx_list[idx][0]}, {random.choice(company_idx_list)}, '{row['artist']}', FALSE);"
        for idx, row in enumerate(rows)
    ]
)

result += artist_sql + "\n\n"


with open("./CREATE.sql", "w", encoding="utf-8") as f:
    f.writelines(result)
