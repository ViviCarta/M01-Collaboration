# 13.2

from datetime import datetime

# Read the content of the file into a string
with open("today.txt", "r") as file:
    today_string = file.read()

# 13.3

# Parse the date from the string
parsed_date = datetime.strptime(today_string, "%Y-%m-%d").date()

print(parsed_date)
