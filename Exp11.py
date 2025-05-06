#Write a Write a Python program that prompts the user to input a date (year, month, and day) and checks if it is a valid date. If the entered date is valid, the program should increment the date by one day and display the incremented date. The program should take into account leap years when determining the number of days in February.
import datetime
def increment_date(year,month,day):
	try:
		date_obj = datetime.date(year,month,day)
		increment_date = date_obj + datetime.timedelta(days=1)
		return increment_date.strftime("%Y-%m-%d")
	except ValueError:
		return "invalid"
year = int(input("year: "))
month = int(input("month: "))
day = int(input("day: "))
result = increment_date(year, month, day)
if result != "invalid":
	print("valid")
	print(f"incremented date: {result}")
else:
	print("invalid")
