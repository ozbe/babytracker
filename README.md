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

## Run

### Commands
```
$ ./extract_foods.py <SHEET_ID>
```

### Arguments

* `SHEET_ID` - The Google Sheet to *override* with the exported foods. A sheet id can be found in the sheet's url https://docs.google.com/spreadsheets/d/[SHEET_ID]/

## References
* [Access Nighp Baby Tracker Data from Latest Backup on a Mac](https://gist.github.com/ozbe/fe5c2f692122cdc7e219ad3ec8444b85)