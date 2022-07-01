n = input()
cnt = 0
if int(n) < 10:
    n = "0" + n
c = n
while True:
    c = c[1] + str(int(c[0]) + int(c[1]))[-1]
    cnt += 1
    if c == n: break
print(cnt)