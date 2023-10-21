
def upsidedown(n, store = 0):
    if n < 10:
        return store+n
    else:
        store += n%10
        return upsidedown(n//10, store*10)

n = int(input())
for i in range(1,n+1):
    if upsidedown(i) ==i and upsidedown(i*7) == i*7 and upsidedown(i*i*3) == i*i*3:
        print(f'{i} ')