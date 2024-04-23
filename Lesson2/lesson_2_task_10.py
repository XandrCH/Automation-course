import math
x = float(input('Введите сумму депозита:'))
y = int(input('На сколько лет вы хотите открыть депозит:'))
percent = 0.1
def bank(x,y):
    for i in range (1, y+1):
        x = x + (x * percent)
        print(round(x,2))
bank(x,y)