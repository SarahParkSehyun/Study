import sys


def NandM(k):
    if k >= m:
        print(" ".join(x))
        return
    for i in range(1, n + 1):
        if str(i) not in x[:k]:
            x[k] = str(i)
            NandM(k + 1)


n, m = map(int, sys.stdin.readline().split())
x = ["0"] * m
NandM(0)
