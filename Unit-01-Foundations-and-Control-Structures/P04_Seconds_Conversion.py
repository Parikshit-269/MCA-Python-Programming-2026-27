seconds = int(input("Enter time in seconds: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
sec = seconds % 60
print(hours, "hours", minutes, "minutes", sec, "seconds")
