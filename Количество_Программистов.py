x = int(input())
if x % 100 in (11, 12, 13, 14) or x % 10 in (5, 6, 7, 8, 9, 0): print(x, 'программистов')
elif x % 10 in (2, 3, 4): print(x, 'программиста')
else: print(x, 'программист')