import sys

T = int(sys.stdin.readline().strip())
sum = 0

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)