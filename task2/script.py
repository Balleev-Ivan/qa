import sys
f = open (sys.argv[1], "r")
str = f.read().splitlines()
#print('Массив0', str)
f.close()
n = [int(str[i]) for i in range(len(str))]
#print('Массив1', n)
from statistics import mean
sr = mean(n)
#print('среднее', round(sr))
mod=[abs(n[i]-round(sr)) for i in range(len(n))]
#print('пути', mod)
#m=min(mod)
#print('min', m)
s=sum(mod)
print(s)
