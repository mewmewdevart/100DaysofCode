# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# the data
days = 365
weeks = 52
months = 12

# the old woman
oldDays = 90 * 365
oldWeeks = 90 * 52
oldMonths = 90 * 12

# your age
yourDays = int(age) * 365
yourWeeks = int(age) * 52
yourMonths = int(age) * 12

print(f"You have {oldDays-yourDays} days, {oldWeeks-yourWeeks} weeks, and {oldMonths-yourMonths} months left.")

