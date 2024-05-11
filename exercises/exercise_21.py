string = input()

day = string[3:5]
year = string[6:]
month_number = string[0:2]
month = ""
if month_number == "01":
    month = "January"
elif month_number == "02":
    month = "February"	
elif month_number == "03":
    month = "March"
elif month_number == "04":
    month = "April"
elif month_number == "05":
    month = "May"
elif month_number == "06":
    month = "June"
elif month_number == "07":
    month = "July"
elif month_number == "08":
    month = "August"
elif month_number == "09":
    month = "September"
elif month_number == "10":
    month = "October"
elif month_number == "11":
    month = "November"
elif month_number == "12":
    month = "December"


print(f"{month} {day}, {year}")