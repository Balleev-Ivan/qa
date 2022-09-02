import sys
nn = sys.argv[1]
mm = sys.argv[2]
n=int(nn)
m=int(mm)
i = 1
while True:
    print(i, end='')
    i = 1 + (i + m - 2) % n
    if i == 1:
        break
print(sep = '\n')
