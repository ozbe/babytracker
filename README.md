# Baby Tracker Foods to Google Sheets

Extract foods (supplements) from [Baby Tracker](https://nighp.com/babytracker/) and import them into an existing Google Sheet on a Mac.

## Setup

### Baby Tracker

* You must have iCloud Sync enabled in the Baby Tracker app
* You must be signed into iCloud on you Mac
* If you want the latest data from Baby Tracker, I’d recommend you do a manual backup from the Baby Tracker app

### gspread

[gpspread](https://github.com/burnash/gspread) is used to access Google Sheets. The user must do the following one-time setups:
1. Run `$ pip3 install --user gspread`
2. Set [OAuth Client Id](https://gspread.readthedocs.io/en/latest/oauth2.html#for-end-users-using-oauth-client-id) - Must be done before the [Run commands](#commands).
3. Authenticate user - this will happen automatically on the first run of `extract_foods.py`.

### .env file

The [Run commands](#commands) and source reference the following environment variables:
* `SHEET_ID` - The Google Sheet to *override* with the exported foods. A sheet id can be found in the sheet's url https://docs.google.com/spreadsheets/d/[SHEET_ID]/
* `EXPORT_PATH` - Path to temporarily save a copy of the BabyTracker backup.

The [Run commands](#commands) load these environment variables from `.env`, which is not included with the project source. The user must configure their own `.env` with the forementioned environment variables.

Here is an example `.env`:
```
export SHEET_ID=abc123
export EXPORT_PATH=data
```

## Run

### Commands
```
$ source .env
$ ls -dt ~/Library/Mobile\ Documents/iCloud\~com\~nighp\~babytracker/Documents/backups/* | \
head -1 | \
xargs -I{} cp {} ./babytracker.zip && \
unzip -o babytracker.zip -d $EXPORT_PATH
$ ./extract_foods.py
```

### Steps
1. Load environment variables
2. Copy and unzip latest Baby Tracker backup
4. Query and upload foods to existing Google Sheet

## References
* [Access Nighp Baby Tracker Data from Latest Backup on a Mac](https://gist.github.com/ozbe/fe5c2f692122cdc7e219ad3ec8444b85)