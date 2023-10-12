#Функции


#Задание 1 (Длина отрезка)
from math import sqrt
def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())
print(distance(x1, x2, y1, y2))


#Задание 2 (Отрицательная степень)
def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res
print(power(float(input()), int(input())))


#Задание 3 (Числа Фибоначчи)
def func(n):
    if n == 1 or n == 2:
        return 1
    else:
        return func(n - 1) + func(n - 2)
print(func(int(input())))


#Задание 4 (Високосный год)
def is_year_leap(year):
    year = int(input())
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return True
    else:
        return False


#Задание 5 (Квадрат)
def square(a):
    return 4 * a, a * a, a * 2 ** 0.5


#Задание 6 (Времена года)
def season(month):
    if month in [12, 1, 2]:
     return "зима"
    elif month in [3, 4, 5]:
     return "весна"
    elif month in [6, 7, 8]:
     return "лето"
    elif month in [9, 10, 11]:
     return "осень"
    else:
     return "Неверный номер месяца"


#Задание 7 (Банковский вклад)
def func(a, years):
    for a in range(years):
        a = a * 1.1
    return a


#Задание 8 (Простые числа)
def function(a):
    if a % a == 0 and a != 0:
        return True
    else:
        return False
a = int(input("Введите номер: "))
print(function(a))


#Задание 9 (Правильная дата)
def check_date(d,m,y):
    if d<0 or m<0 or y<0:
        return False
    mon=[31,28,31,30,31,30,31,31,30,31,30,31]
    if y%400==0 or ((y%4==0) and (y%100 != 0)):
        mon[1]=29
    if m>=1 and m<=12:
       if d>0 and d<=mon[m-1]:
           return True
    return False
