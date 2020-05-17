def su(ar):
    summa = 0
    for m in range(0,len(ar)):
        if m%2==0:
            summa = summa + (ar[m] * (m+1))
        else:
            summa = summa - (ar[m] * (m+1))
    return summa

def solve(c,op,ar):
    summa = 0
    for i in range(1,c+1):
        f = op[str(i)]
        if f[0] == 'Q':
            sub_ar = ar[(int(f[1])-1):(int(f[2]))]
            summa = summa + su(sub_ar)
        elif f[0] == 'U':
            ar[(int(f[1])-1)] = int(f[2])
    return summa

n = int(input())
for x in range(1,n+1):
    N,O = map(int, input().split())
    array = list(map(int, input().rstrip().split()))
    operations = {}
    for i in range(1, O + 1):
        operations[str(i)] = list((map(int and str, input().rstrip().split())))
    #print("\n" + str(operations))
    y = solve(O,operations,array)
    print("Case #{}: {}".format(x, y), flush=True)
