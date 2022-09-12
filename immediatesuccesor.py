import datetime
date_entry = input('')
year, month, day = map(int, date_entry.split('-'))
date1 = datetime.date(year, month, day)
NextDay_Date = date1  + datetime.timedelta(days=1)
print ("Next Date:",NextDay_Date)

