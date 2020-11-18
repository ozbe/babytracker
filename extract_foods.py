#!/usr/bin/env python3

import gspread
import os

csv_path = os.environ['CSV_PATH']
sheet_id = os.environ['SHEET_ID']

print('Authenticating... ', end='')
gc = gspread.oauth()
print('done')

print('Opening CSV... ', end='')
content = open(csv_path, 'r').read()
print('done')

print('Opening sheet... ', end='')
sh = gc.open_by_key(sheet_id)
print('done')

print(f'Importing CSV to sheet \'{sh.title}\'... ', end='')
gc.import_csv(sh.id, content)
print('done')

print(f'Updated \'{sh.title}\'')