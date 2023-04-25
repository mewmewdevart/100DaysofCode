# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

age = input("What is your current age? ")

# Standard
daysPerYear = 365
weeksPerYear = 52
monthsPerYear = 12

# User data
yourAge = int(age)
yourMonths = monthsPerYear * yourAge
yourDays = daysPerYear * yourAge
yourWeeks = weeksPerYear * yourAge

# 90 Years data
oldAge = 90
oldMonths = monthsPerYear * oldAge
oldDays = daysPerYear * oldAge
oldWeeks = weeksPerYear * oldAge

print(f"You have {oldDays - yourDays} days, {oldWeeks - yourWeeks} weeks, and {oldMonths - yourMonths} months left.")
