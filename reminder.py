import json
import sys
from datetime import date, datetime

print("Checking for valid JSON file . . .")

while True:
    try:
        with open('deadlines.json', 'r') as infile:
            deadlines = json.load(infile)
    except FileNotFoundError:
        continue

    today = date.today().strftime("%Y-%m-%d")
    today = datetime.strptime(today, "%Y-%m-%d")

    upcoming_deadlines = {}

    for deadline in deadlines:
        d1 = datetime.strptime(deadline, "%Y-%m-%d")
        delta = d1 - today
        if delta.days <= 3:
            # Change conditional to get deadlines within given (int) days.
            upcoming_deadlines[deadline] = deadlines[deadline]

    with open('reminder.json', 'w') as outfile:
        json.dump(upcoming_deadlines, outfile)

    print("Reminder for upcoming deadlines returned.")
    sys.exit()

    