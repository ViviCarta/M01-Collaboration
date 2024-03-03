# 13.1

from datetime import date

# Get the current date
current_date = date.today()

# Convert the date to a string
date_string = current_date.strftime("%Y-%m-%d")

# Write the date string to the file
with open("today.txt", "w") as file:
    file.write(date_string)
