def findCount(l,num, ar):
    y = 0
    comp = []
    for n in range(0,num):
        comp.append(num-n)
    for a in range(0,l-len(comp)+1):
        if ar[a:-(l-len(comp)-a)] == comp:
            y = y+1
        if a == l-len(comp):
            if ar[a:] == comp:
                y = y + 1
    return y

n = int(input())
for x in range(1,n+1):
    N, K = map(int, input().split())
    array = list(map(int, input().rstrip().split()))
    y = findCount(N,K,array)
    print("Case #{}: {}".format(x, y), flush=True)

