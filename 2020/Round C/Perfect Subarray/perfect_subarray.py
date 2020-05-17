def squareFinder(ar_len, ar):
    y = 0
    for i in range(0,ar_len):
        for n in range(0,ar_len):
            c = -(ar_len-n-1)
            if c == 0:
                c = None
            sub_ar = ar[i:c]
            if not sub_ar:
                y = y-1
            b = sum(sub_ar)
            x = b ** .5
            if x >= 0 and x % 1 == 0:
                y = y+1
    return y

n = int(input())
for x in range(1,n+1):
    length = int(input())
    array = list(map(int, input().rstrip().split()))
    y = squareFinder(length,array)
    print("Case #{}: {}".format(x, y), flush=True)
