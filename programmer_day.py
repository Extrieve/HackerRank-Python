def dayOfProgrammer(year):
    # Write your code here
    if(year >= 1700 and year <= 1917):
        if(year % 4 != 0):
            return f'13.09.{year}'
        else:
            return f'12.09.{year}'
    elif(year == 1918):
        return '26.09.1918'
    else:
        if((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            return f'12.09.{year}'
        else:
            return f'13.09.{year}'

print(2016 % 400 == 0)
print(dayOfProgrammer(2016))
