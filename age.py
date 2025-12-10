year = int(input("Please Enter Birth Year:"))  # to obtain the birth year


age_in_years = 2025 - year   # to calculate age in years
age_in_months = age_in_years*12 # to calculate age in months
age_in_seconds = age_in_years*365*24*60*60 # to calculate age in seconds

output = 'This is your age in years; {}, in months; {}, and in seconds; {}'.format(age_in_years, age_in_months, age_in_seconds) # producing the output
print(output) # printing the output