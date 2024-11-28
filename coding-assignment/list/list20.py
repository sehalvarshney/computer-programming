#   Write a program that converts a given number of days into weeks and days.
# Input: Total number of days
total_days = int(input("Enter the number of days: "))

# Calculate weeks and remaining days
weeks = total_days // 7
days = total_days % 7

# Store the results in a list
result = [weeks, days]

# Output the result
print(f"{total_days} days is equivalent to {result[0]} week(s) and {result[1]} day(s).")
