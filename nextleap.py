def is_leap_year(year):

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


year = int(input('Enter the year: '))

next_leap_year = year
while not is_leap_year(next_leap_year):
    next_leap_year += 1

print(f"The next leap year after {year} is {next_leap_year}")
