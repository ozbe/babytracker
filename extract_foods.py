#!/usr/bin/env python3

import csv
import gspread
import io
import os
import sqlite3
from functools import reduce
from pathlib import Path

export_path = os.environ['EXPORT_PATH']
sheet_id = os.environ['SHEET_ID']

print('Querying food... ', end='')
db_path = Path(export_path) / "Easylog.db"
conn = sqlite3.connect(db_path)
cursor = conn.execute("SELECT Name FROM OtherFeedSelection")
data = cursor.fetchall()
conn.close()
print('done')

print('Generating content... ', end='')

# map and reduce
def parse(row):
    name = row[0]
    row_foods = set(map(lambda x: x.strip().capitalize(), name.replace(", and ", ", ").split(",")))
    return row_foods

foods = reduce(lambda acc, row: acc.union(parse(row)), data, set())

# write csv
rows = map(lambda x: [x], sorted(foods))
output = io.StringIO()
writer = csv.writer(output)
writer.writerows(rows)
content = output.getvalue()
output.close()

print('done')

print('Authenticating... ', end='')
gc = gspread.oauth()
print('done')

print('Opening sheet... ', end='')
sh = gc.open_by_key(sheet_id)
print('done')

print(f'Importing content to sheet \'{sh.title}\'... ', end='')
gc.import_csv(sh.id, content)
print('done')

print(f'Updated \'{sh.title}\' ({sh.url})')