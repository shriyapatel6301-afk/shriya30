from datetime import datetime

# Get the current date and time
now = datetime.now()

# Print the full datetime object to the console
print("now =", now)

# Format the date and time into a specific string (e.g., DD/MM/YYYY H:M:S)
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)
