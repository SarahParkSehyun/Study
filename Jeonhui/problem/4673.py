NUM = [0 for _ in range(10001)]


def createNUM(n):
    sumN = int(n)
    for i in range(len(n)):
        sumN += int(n[i])
    if sumN < 10001:
        NUM[sumN] += 1


for i in range(10001):
    createNUM(str(i))
print("\n".join([str(i) for i in range(10001) if NUM[i] == 0]))
