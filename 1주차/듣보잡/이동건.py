import sys
inp = lambda : sys.stdin.readline().rstrip()
N, M = map(int, inp().split())
names = [inp() for _ in range(N+M)]
non_heard = set(names[:N])
non_seen = set(names[N:])
res = set(non_heard & non_seen)
print(len(res))
for name in sorted(res):
    print(name)