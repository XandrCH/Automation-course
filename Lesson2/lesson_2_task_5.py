n = int(input("Введите номер месяца:"))

def month_to_season(n):
    if n in [12,1,2]:
        print ('Winter')
    if n in [3,4,5]:
        print('Spring')
    if n in [6,7,8]:
        print('Summer')
    if n in [9,10,11]:
        print('Autumn')
    else:
        print('Error: There is only 12 months in the year')
month_to_season(n)
