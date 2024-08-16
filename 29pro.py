p = int(input("enter starting range:"))
r = int(input("enter ending range:"))
h = []
for x in range(p,r):
    for i in range(2,x):
        if x%i == 0:
            break
    else:
        print(x,end = '')
        h.append(x)
        print()
        length = len(h)
        mid = length // 2
        print(h[mid] + h[mid-1])