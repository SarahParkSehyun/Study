def sequence(n):
    cnt = 0
    for i in range(1, n + 1):
        if i < 100:
            cnt += 1
        elif 100 <= i < 1000:
            i = str(i)
            if int(i[0]) + int(i[2]) == 2 * int(i[1]):
                cnt += 1
    return cnt


n = int(input())
print(sequence(n))
